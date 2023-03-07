import os
import sys
import json

etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

json_object = json.loads(etcdServiceVar)
argumentVars = list(json_object.values())[0]
connectionVars = list(json_object.values())[1]

try:
    print("Pulling all argument info for etcd instance")
    print(argumentVars)
    print("Pulling composed connection info for etcd instance")
    print(connectionVars['composed'][0])
    print("Dumping full json object")
    print(json_object)
except KeyError:
    print("Key not found")
