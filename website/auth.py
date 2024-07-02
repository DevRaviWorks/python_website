from flask import Blueprint,render_template

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/sign-up')
def sign_up():
    return render_template("sign-up.html")

@auth.route('/forgot-password')
def forgot_password():
    return "<h1>forgot-password works</h1>"