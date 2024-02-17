from flask import Flask

app = Flask(__name__)

from routes import *

# name is main when executed from command line
if __name__ == '__main__':
    app.run(debug=True) 