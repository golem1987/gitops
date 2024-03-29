from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route to display "Hello World"
@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    # Run the application
    app.run()
