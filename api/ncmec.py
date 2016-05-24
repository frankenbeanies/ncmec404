from flask import Flask
from flask.ext.cors import cross_origin
import json
import random
import requests

app = Flask(__name__)

@app.route("/query/<state>")
@cross_origin()
def query(state):
	session = requests.Session()
	session.trust_env = False

	response = session.get("http://www.missingkids.com/missingkids/servlet/JSONDataServlet?action=publicSearch&searchLang=en_US&search=new&subjToSearch=child&missState=" + state + "&missCountry=US")
	dct = json.loads(response.text)
	return json.dumps(dct, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == "__main__":
	app.run()