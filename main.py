import os
import sys
import json

etcdConnection = os.environ.get('CE_SERVICES')
etcdDetails = etcdConnection[0]
# print(type(etcdConnection))
print(etcdDetails)


## print(json.dumps(etcdConnection, indent=2))
