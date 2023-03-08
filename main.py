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

etcdClient = etcd.Client(
    composedConnection,
    allow_reconnect=True,
    protocol='https',
    ca_cert=base64.b64decode(certDetails)
)

getLeader = etcdClient.leader

try:
    print(connectionVars['composed'][0])
    print(getLeader)
    # print("Pulling password connection info for etcd instance")
    # print(connectionVars['authentication']['password'])
    # print("Pulling hosts for etcd instance")
    # print(connectionVars['hosts'])
    # # print("Pulling hostname for etcd instance")
    # # print(connectionVars['hosts'][0]['hostname'])
    # # print("Pulling port for etcd instance")
    # # print(connectionVars['hosts'][0]['port'])
    # # print("Pulling password for etcd instance")
    # print("attempting to pull cert info for etcd instance")
    # 

    # print(certDetails)
    # print("attempting to decode cert info for etcd instance")
    # certDetailsDecoded = base64.b64decode(certDetails)
except KeyError:
    print("Error in code")
