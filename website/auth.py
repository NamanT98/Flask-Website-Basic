from flask import Blueprint,render_template

auth=Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html',text='testing',user='Naman Trisoliya')

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/signup')
def signup():
    return render_template('signup.html')