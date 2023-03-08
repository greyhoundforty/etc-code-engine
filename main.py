import os
import sys
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibm_schematics.schematics_v1 import SchematicsV1
import base64
import etcd3

## Only uncomment if you need to debug gprc connection.
# os.environ['GRPC_TRACE'] = 'all'
# os.environ['GRPC_VERBOSITY'] = 'DEBUG'
workspaceId = os.environ.get('WORKSPACE_ID')
etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

authenticator = IAMAuthenticator(
    apikey=os.environ.get('IBMCLOUD_API_KEY'),
    client_id='bx',
    client_secret='bx'
    )

refreshToken = authenticator.token_manager.request_token()['refresh_token']

# Set up Schematics service client, endpoint, and workspace ID 
schematicsService = SchematicsV1(authenticator=authenticator)
schematicsURL = "https://us.schematics.cloud.ibm.com"
schematicsService.set_service_url(schematicsURL)

# ceServiceJson = json.loads(ceEnvVars)
# ceServiceVars = list(ceServiceJson.values())

connectionJson = json.loads(etcdServiceVar)
connectionVars = list(connectionJson.values())[1]

certDetails = connectionVars['certificate']['certificate_base64']
ca_cert=base64.b64decode(certDetails)
decodedCert = ca_cert.decode('utf-8')

certname = '/etc/ssl/certs/db-ca.crt'
with open(certname, 'w+') as output_file:
    output_file.write(decodedCert)

etcdHost = connectionVars['hosts'][0]['hostname']
etcdPort = connectionVars['hosts'][0]['port']
etcdUser = connectionVars['authentication']['username']
etcdPass = connectionVars['authentication']['password']
etcdCert = '/etc/ssl/certs/db-ca.crt'

def getWorkspaceOutputs(workspaceId, schematicsService):
    wsOutputs = schematicsService.get_workspace_outputs(
        w_id=workspaceId,
    ).get_result()

    allOutputs = wsOutputs[0]['output_values'][0]
    # print("All outputs are: " + str(pullAllOutputs))
    ubuntuInstanceID = str(allOutputs['ubuntu_instance_id']['value'])
    # ubuntuInstanceID = str(wsOutputs[0]['output_values'][0]['ubuntu_instance_id']['value'])
    rockyInstanceID = str(wsOutputs[0]['output_values'][0]['rocky_instance_id']['value'])
    windowsInstanceID = str(wsOutputs[0]['output_values'][0]['windows_instance_id']['value'])

    ectdClient = etcd3.client(
        host=etcdHost, 
        port=etcdPort, 
        ca_cert=etcdCert, 
        timeout=10, 
        user=etcdUser, 
        password=etcdPass
    )
    print("Connected to etcd service")
    print("Attempting to write instance IDs to etcd")
    ectdClient.put('/current_servers/ubuntu/id', ubuntuInstanceID)
    ectdClient.put('/current_servers/rocky/id', rockyInstanceID)
    ectdClient.put('/current_servers/windows/id', windowsInstanceID)
    print("Keys written to etcd service")
    print("Recursively reading keys from etcd service")
    allKeys = ectdClient.get_all(
        keys_only=True
    ).decode('utf-8')
    print(allKeys)
try:
    getWorkspaceOutputs(workspaceId, schematicsService)

except ApiException as e:
    print("Etcd write failed " + str(e.code) + ": " + e.message)
