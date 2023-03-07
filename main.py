import os
import sys
import json

etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

json_object = json.loads(etcdServiceVar)
connectionVars = list(json_object.values())[1]

try:
    print("Pulling composed connection information for etcd")
    print(connectionVars['composed'][0])
except KeyError:
    print("Key not found")
