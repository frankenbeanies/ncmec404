import json
import requests

session = requests.Session()
session.trust_env = False

response = session.get("http://www.missingkids.com/missingkids/servlet/JSONDataServlet?action=publicSearch&searchLang=en_US&search=new&subjToSearch=child&missState=CT&missCountry=US")
dct = json.loads(response.text)
print json.dumps(dct, sort_keys=True, indent=4, separators=(',', ': '))