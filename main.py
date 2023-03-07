import os
import sys
import json

ceServicesVar = os.environ.get('CE_SERVICES')
etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

# print("CE services env var type")
# print(type(ceServicesVar))
# print("CE services env var value: " + ceServicesVar)

# print("ETCD env var type")
json_object = json.loads(etcdServiceVar)
# print(type(json_object))
# print(json_object)

# print(type(etcdServiceVar))
# print("ETCD env var value: " + etcdServiceVar)
# print("seeing if we can pull all values from json object")
# for values in json_object.values():
#    print(values)


# authCreds = json_object.values()

authCreds = list(json_object.values())[0]

try:
    print(authCreds)
except KeyError:
    print("Key not found")
