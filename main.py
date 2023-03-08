import os
import json
import base64
import etcd

etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

json_object = json.loads(etcdServiceVar)
argVars = list(json_object.values())[0]
connectionVars = list(json_object.values())[1]

composedConnection = connectionVars['composed'][0]
certDetails = connectionVars['certificate']['certificate_base64']
ca_cert=base64.b64decode(certDetails)
cert2ElectricBoogaloo = ca_cert.decode('utf-8')

certname = '/etc/ssl/certs/db-ca.crt'
with open(certname, 'w+') as output_file:
    output_file.write(ca_cert.decode('utf-8'))

etcdClient = etcd.Client(
    host=connectionVars['hosts'][0]['hostname'],
    port=connectionVars['hosts'][0]['port'],
    username=connectionVars['authentication']['username'],
    password=connectionVars['authentication']['password'],
    allow_reconnect=True,
    protocol='https',
    ca_cert='/etc/ssl/certs/db-ca.crt'
)

# getLeader = etcdClient.leader



try:
    print("Pulling username connection info for etcd instance")
    print(connectionVars['authentication']['username'])
    print("Pulling password connection info for etcd instance")
    print(connectionVars['authentication']['password'])
    print("Pulling hostname for etcd instance")
    print(connectionVars['hosts'][0]['hostname'])
    print("Pulling port for etcd instance")
    print(connectionVars['hosts'][0]['port'])
except KeyError:
    print("Error in code")
