from app import app
from flask import render_template

import forms

# If root is accessed, run the following function
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print('Submitted title', form.title.data)
        return render_template('about.html', form=form, title=form.title.data)
    return render_template('about.html', form=form)