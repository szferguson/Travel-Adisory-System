from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
import pymongo 
from app import db


# index field
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

# login field
@app.route('/')
@app.route('/login.html', methods=['GET','POST'])
def login():
    form = LoginForm()
   
    if form.validate_on_submit():
        # flash('Login requested for user {}'.format(form.email.data))
        username = form.email.data
        password = form.password.data
        # print(username)
        # print(form.password.data)

        for user in db.mycollection.find():
            for u, p in user.items():
                if username == u:
                    if db.hashGenerator(password) == p:
                        return redirect(url_for('index'))
                    else:
                        flash("Username and password pair didn't match")

    return render_template('login.html', form=form)
