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
# etcdClient = etcd.Client(
#     host=connectionVars['hosts'][0]['hostname'],
#     port=connectionVars['hosts'][0]['port'],
#     username=connectionVars['authentication']['username'],
#     password=connectionVars['authentication']['password'],
#     allow_reconnect=True,
#     protocol='https',
#     ca_cert=base64.b64decode(certDetails)
# )

# getLeader = etcdClient.leader

etcdHost = connectionVars['hosts'][0]['hostname']
etcdPort=connectionVars['hosts'][0]['port']
etcdUsername=connectionVars['authentication']['username']
etcdPassword=connectionVars['authentication']['password']

try:
    print("Pulling username connection info for etcd instance")
    print(connectionVars['authentication']['username'])
    print("Pulling password connection info for etcd instance")
    print(connectionVars['authentication']['password'])
    print("Pulling hostname for etcd instance")
    print(connectionVars['hosts'][0]['hostname'])
    print("Pulling port for etcd instance")
    print(connectionVars['hosts'][0]['port'])
    print("Pulling decoded cert for etcd instance")
    print(ca_cert)
    print("Pulling corrected decoded cert for etcd instance")
    print(cert2ElectricBoogaloo)
    # # print("Pulling password for etcd instance")
    # print("attempting to pull cert info for etcd instance")
    # 

    # print(certDetails)
    # print("attempting to decode cert info for etcd instance")
    # certDetailsDecoded = base64.b64decode(certDetails)
except KeyError:
    print("Error in code")
