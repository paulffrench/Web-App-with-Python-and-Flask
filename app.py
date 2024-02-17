from flask import Flask, render_template

app = Flask(__name__)

# If root is accessed, run the following function
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
# name is main when executed from command line
if __name__ == '__main__':
    app.run(debug=True) 