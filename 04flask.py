from flask import Flask
my_app = Flask(__name__)

@my_app.route('/')
def root():
	return "<h1>Welcome!</h1>"
	
@my_app.route('/next')
def page1():
	return "Hello!"
	
@my_app.route('/page2')
def page2():
	return "Hi!"

@my_app.route('/page3')
def page3():
	return "Testing!"
	
if __name__ == '__main__':
	#my_app.debug = True
	my_app.run()


	