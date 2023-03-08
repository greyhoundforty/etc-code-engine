import os
import json
import base64
import etcd3

etcdHost = '78e97ca8-e217-41be-8c89-782a177ad990.c00no9sd0hobi6kj68i0.databases.appdomain.cloud'
etcdPort = 31365
etcdUser = 'ibm_cloud_7e6f1acd_be19_42bd_aef0_b354ba31fdb3'
etcdPass = 'fe4f6268ad53d3ff1c0ed30f3396eb81345b50f82d52597eb6fda4cf2e2a4642'
etcdCert = './db-ca.crt'
result = etcd3.client(host=etcdHost, port=etcdPort, ca_cert=etcdCert, timeout=10, user=etcdUser, password=etcdPass)

# etcdClient = etcd.Client(
#     host=,
#     port=31365,
#     username='ibm_cloud_7e6f1acd_be19_42bd_aef0_b354ba31fdb3',
#     password='fe4f6268ad53d3ff1c0ed30f3396eb81345b50f82d52597eb6fda4cf2e2a4642',
#     allow_reconnect=True,
#     protocol='https',
#     ca_cert='./db-ca.crt'
# )

newThing = result.put('foo', 'bar')
pullThing = print(result.get('foo'))