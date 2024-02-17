from app import app
from flask import render_template

# If root is accessed, run the following function
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')