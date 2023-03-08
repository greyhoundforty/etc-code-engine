import os
import json
import base64
import etcd

etcdClient = etcd.Client(
    host=connectionVars['hosts'][0]['hostname'],
    port=connectionVars['hosts'][0]['port'],
    username=connectionVars['authentication']['username'],
    password=connectionVars['authentication']['password'],
    allow_reconnect=True,
    protocol='https',
    ca_cert='db-ca.crt'
)