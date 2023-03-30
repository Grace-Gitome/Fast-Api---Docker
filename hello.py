#Importing the Flask class and instance of the class will be our WSGI application
from flask import Flask

#Creating an instance of the class.
app = Flask(__name__)

#Using the route() decorator to thell Flask what URL should trigger out function
@app.route("/")
def hello_world():
	return '<p>Hello, World!</p>'

if __name__ == '__main__':
	app.run(debug=True)
