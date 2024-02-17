from flask import Flask

app = Flask(__name__)

from routes import *
app.config['SECRET_KEY'] = 'secret-key'

# name is main when executed from command line
if __name__ == '__main__':
    app.run(debug=True) 