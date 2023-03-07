import os
import json
import base64

etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

json_object = json.loads(etcdServiceVar)
connectionVars = list(json_object.values())[1]

try:
    # print("Pulling password connection info for etcd instance")
    # print(connectionVars['authentication']['password'])
    print("Pulling hosts for etcd instance")
    print(connectionVars['hosts'])
    # print("Pulling hostname for etcd instance")
    # print(connectionVars['hosts'][0]['hostname'])
    # print("Pulling port for etcd instance")
    # print(connectionVars['hosts'][0]['port'])
    # print("Pulling password for etcd instance")
    print("attempting to pull cert info for etcd instance")
    certDetails = base64.b64decode(connectionVars['certificate']['certificate_base64']).decode('utf-8')

    print(certDetails)
except KeyError:
    print("Key not found")
