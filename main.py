import os
import json
import base64

etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

json_object = json.loads(etcdServiceVar)
argVars = list(json_object.values())[0]
connectionVars = list(json_object.values())[1]

try:
    print("Pulling auth connection info for etcd instance")
    print(connectionVars['authentication'])
    print("Pulling hosts for etcd instance")
    print(connectionVars['hosts'])
    # print("Pulling hostname for etcd instance")
    # print(connectionVars['hosts'][0]['hostname'])
    # print("Pulling port for etcd instance")
    # print(connectionVars['hosts'][0]['port'])
    # print("Pulling password for etcd instance")
    print("attempting to pull cert info for etcd instance")
    certDetails = connectionVars['certificate']
    print(decodedCert)
except KeyError:
    print("Key not found")
