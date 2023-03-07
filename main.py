import os
import sys
import json

# etcdConnection = os.environ.get('CE_SERVICES')
# # etcdDetails = etcdConnection[0]
# # # print(type(etcdConnection))
# print(etcdDetails)


# etcdDetails =  print(json.dumps(etcdConnection, indent=2))

for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))