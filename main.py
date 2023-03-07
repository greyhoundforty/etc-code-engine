import os
import sys
import json

etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

json_object = json.loads(etcdServiceVar)
argVars = list(json_object.values())[0]
connectionVars = list(json_object.values())[1]

try:
    print("Dumping full argVars")
    print(argVars)
    # print("Pulling hosts for etcd instance")
    # print(connectionVars['hosts'])
    print("Pulling hostname for etcd instance")
    print(connectionVars['hosts'][0]['hostname'])
    print("Pulling port for etcd instance")
    print(connectionVars['hosts'][0]['port'])
except KeyError:
    print("Key not found")
