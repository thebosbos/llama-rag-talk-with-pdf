from flask import Flask, request
from database import *
import threading

app = Flask(__name__)

@app.route('/get_response')
def execute_python_file():
    # Execute the Python file and capture its output
    return main()


@app.route('/')
def hello():

    return 'Hello, World!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get port from environment variable or use default 5000
    flask_thread = threading.Thread( app.run(debug=True, host='0.0.0.0', port=port))# Explicitly set host and port
    flask_thread.start()   
