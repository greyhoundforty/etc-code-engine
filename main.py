import os
import sys
import json

ceServicesVar = os.environ.get('CE_SERVICES')
etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

print("CE Services environment variable is type")
print(type(ceServicesVar))
print("CE Services environment variable value is: " + ceServicesVar)

print("ETCD Services environment variable is type: " + type(etcdServiceVar))
print("ETCD Services environment variable value is: " + etcdServiceVar )