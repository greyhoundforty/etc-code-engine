import os
import sys
import json

etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

json_object = json.loads(etcdServiceVar)
connectionVars = list(json_object.values())[1]

try:
    print("Pulling composed connection info for etcd instance")
    print(connectionVars['composed'][0])
    print("Pulling hosts for etcd instance")
    print(connectionVars['hosts'])
    print("Pulling port for etcd instance")
    print(connectionVars['port'])
    print("Pulling hostname for etcd instance")
    print(connectionVars['hosts'][0]['hostname'])
except KeyError:
    print("Key not found")
