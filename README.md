# Pull ICD services binding from Code Engine

Python container to pull ICD services binding from Code Engine Environment Variables and then write them to an instance of IBM Cloud Databases for Etcd.

```python
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
```