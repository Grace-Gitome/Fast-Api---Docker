from flask import Flask, render_template

app = Flask(__name__)

#defining route
@app.route('/')
def hello():
	return render_template('index.html', name = 'John') # sending a variable to the template

#serving form webpage
@app.route('/form')
def form():
	return render_template('form.html')

#creating an endpoint to handle form request
@app.route('/form-handler', methods=['POST'])
def handle_data():
    
    return "Request received successfully!"

if __name__ == '__main__':
	app.run(debug = True)