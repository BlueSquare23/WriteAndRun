import os
import json
import requests 
import Algorithmia
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Our app is this file
app = Flask(__name__)
algo_api_key = os.environ['ALGO_API_KEY']

# Webroot is '/'
@app.route('/', methods=['POST', 'GET'])

# Index page contents
def index():
	if request.method == 'POST':
		content = request.form['code']
		if len(content) != 0:
			lang = detect_lang(content)
			output = query_rce(lang, content)
			lang = f'Language: {lang}'
			return render_template('index.html', lang=lang, output=output, content=content)
		else:
			return "content empty"
	else:
		content='Write any code here...'
		return render_template('index.html', content=content)

def detect_lang(content):
	input = content

	client = Algorithmia.client(algo_api_key)
	algo = client.algo('PetiteProgrammer/ProgrammingLanguageIdentification/0.1.3')
	algo.set_options(timeout=300) # optional
	result = algo.pipe(input).result
	language = result[0][0]

	print(language)

	return language

def query_rce(language, content):
	rce_engine_url = "https://emkc.org/api/v1/piston/execute"

	language = language.lower()

	my_dict = {
	  "language": language,
	  "source": content
	}
	
	data = json.dumps(my_dict)

	r = requests.post(rce_engine_url, data)

	if r.status_code == 200:
		json_response = r.json()
		if json_response["stderr"] == "":
			return json_response["stdout"]
		else:
			return json_response["stderr"]
	else:
		return r.json()

# Run the app, w/ debug
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
