import os
import sys
import json

etcdConnection = os.environ.get('CE_SERVICES')
print(json.dumps(etcdConnection, indent=2))
