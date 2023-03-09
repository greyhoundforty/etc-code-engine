import os
import sys
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibm_schematics.schematics_v1 import SchematicsV1
import base64
import etcd3

# Set up IAM authenticator and pull refresh token
authenticator = IAMAuthenticator(
    apikey=os.environ.get('IBMCLOUD_API_KEY'),
    client_id='bx',
    client_secret='bx'
    )

refreshToken = authenticator.token_manager.request_token()['refresh_token']

# Set up Schematics service client and declare workspace ID
workspaceId = os.environ.get('WORKSPACE_ID')
schematicsService = SchematicsV1(authenticator=authenticator)
schematicsURL = "https://us.schematics.cloud.ibm.com"
schematicsService.set_service_url(schematicsURL)

# Pull database connection details via Code Engine environment variable
# do some base64 decoding and type manipulation to get everything humming along
etcdServiceVars = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')
connectionJson = json.loads(etcdServiceVars)
connectionVars = list(connectionJson.values())[1]
certDetails = connectionVars['certificate']['certificate_base64']
ca_cert=base64.b64decode(certDetails)
decodedCert = ca_cert.decode('utf-8')
certname = '/etc/ssl/certs/db-ca.crt'

# Write etcd certificate to file
with open(certname, 'w+') as output_file:
    output_file.write(decodedCert)

# Set up etcd service client
etcdClient = etcd3.client(
    host=connectionVars['hosts'][0]['hostname'], 
    port=connectionVars['hosts'][0]['port'], 
    ca_cert='/etc/ssl/certs/db-ca.crt', 
    timeout=10, 
    user=connectionVars['authentication']['username'], 
    password=connectionVars['authentication']['password']
)

# Function to pull specific output value from Schematics workspace based on `instance` parameter
def getWorkspaceOutputs(schematicsService, workspaceId, instance):
    wsOutputs = schematicsService.get_workspace_outputs(
        w_id=workspaceId,
    ).get_result()

    outputValue = str(wsOutputs[0]['output_values'][0][instance]['value'])
    return outputValue

# Pull instance IDs from Schematics workspace
def pullOutput(instance):
    instanceId = getWorkspaceOutputs(schematicsService, workspaceId, instance=instance)
    return instanceId

# Write instance IDs to etcd service
def etcdWrite(etcdClient):

    print("Connected to etcd service")

    ubuntuInstanceID = str(pullOutput(instance = 'ubuntu_instance_id'))
    rockyInstanceID = str(pullOutput(instance = 'rocky_instance_id'))
    windowsInstanceID = str(pullOutput(instance = 'windows_instance_id'))

    print("Attempting to write instance IDs to etcd")
    etcdClient.put('/current_servers/ubuntu/id', ubuntuInstanceID)
    etcdClient.put('/current_servers/rocky/id', rockyInstanceID)
    etcdClient.put('/current_servers/windows/id', windowsInstanceID)
    print("Keys written to etcd service")
try:
    etcdWrite(etcdClient)

except KeyError():
    print("KeyError: Unable to write to etcd service")
# except ApiException as e:
#     print("Etcd write failed " + str(e.code) + ": " + e.message)
