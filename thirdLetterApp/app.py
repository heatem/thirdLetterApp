from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def route():
	return render_template('index.html')

@app.route('/test', methods = ['POST'])
def submit():
	string_to_cut = request.form['string_to_cut']
	data = {
		'return_string': cutString(string_to_cut)
	}

	return render_template('/test.html', data = data)

def cutString(string_to_cut):
	newString = ''
	for i,c in enumerate(string_to_cut):
		if(i + 1) % 3 == 0:
			newString += c
	return newString
	