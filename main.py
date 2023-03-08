import os
import json
import base64
import etcd3
import socket

# os.environ['GRPC_TRACE'] = 'all'
# os.environ['GRPC_VERBOSITY'] = 'DEBUG'

etcdServiceVar = os.environ.get('DATABASES_FOR_ETCD_CONNECTION')

json_object = json.loads(etcdServiceVar)
connectionVars = list(json_object.values())[1]

certDetails = connectionVars['certificate']['certificate_base64']
ca_cert=base64.b64decode(certDetails)
decodedCert = ca_cert.decode('utf-8')

certname = '/etc/ssl/certs/db-ca.crt'
with open(certname, 'w+') as output_file:
    output_file.write(decodedCert)

etcdHost = connectionVars['hosts'][0]['hostname']
etcdPort =connectionVars['hosts'][0]['port']
etcdUser = connectionVars['authentication']['username']
etcdPass = connectionVars['authentication']['password']
etcdCert = '/etc/ssl/certs/db-ca.crt'

# def clientConnect():
#     ectdClient = etcd3.client(
#         host=etcdHost, 
#         port=etcdPort, 
#         ca_cert=etcdCert, 
#         timeout=10, 
#         user=etcdUser, 
#         password=etcdPass
#     )

#     pullThing = print(ectdClient.get('foo'))
#     return ectdClient


lookupHostname = socket.getnameinfo(etcdHost)

try:
    # print("Pulling username connection info for etcd instance")
    # print(connectionVars['authentication']['username'])
    # print("Pulling password connection info for etcd instance")
    # print(connectionVars['authentication']['password'])
    # print("Pulling hostname for etcd instance")
    # print(connectionVars['hosts'][0]['hostname'])
    # print("Pulling port for etcd instance")
    # print(connectionVars['hosts'][0]['port'])
    print("checking DNS resolution for etcd instance")
    print(lookupHostname)
    # clientConnect()
    print("Connection to etcd instance successful")
    
except KeyError:
    print("Error in code")
