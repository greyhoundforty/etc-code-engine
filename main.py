import os
import sys
import json

ceServicesVar = os.environ.get('CE_SERVICES')
etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

jls_extract_var = type
print("CE Services environment variable is type: " + jls_extract_var(ceServicesVar))
print("CE Services environment variable value is: " + ceServicesVar)

print("ETCD Services environment variable is type: " + jls_extract_var(etcdServiceVar))
print("ETCD Services environment variable value is: " + etcdServiceVar)