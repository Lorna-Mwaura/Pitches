from . import auth
from .. import db
from flask import render_template,redirect,url_for, flash,request,abort
from ..models import User
from .forms import LoginForm,RegistrationForm
from flask_login import login_user,logout_user,login_required
from ..email import mail_message
from werkzeug.security import generate_password_hash,check_password_hash


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to Pitches","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        
        if user == None:
            flash('Invalid email or Password')
            return redirect (url_for('auth.register'))
        correct_password = check_password_hash(user.password_hash,login_form.password.data)

        if correct_password == False:
            flash('Invalid email or Password')
            return redirect (url_for('auth.register'))
        else:
            return redirect (url_for('main.index'))


        # user.verify_password(login_form.password.data):
        #     login_user(user,login_form.remember.data)
        #     return redirect (url_for('main.index'))


    title = "Pitches login"
    return render_template('auth/login.html',login_form = login_form,title=title)
