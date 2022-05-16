from flask import Flask, render_template
from . import main
from flask_login import login_required, current_user
from ..models import User
from .forms import UpdateProfile
from .. import db

@main.route('/')
def index():
   
    title = 'Welcome to Pitches'

    # business_pitches = Pitch.get_pitches('business')
    # product_pitches = Pitch.get_pitches('product')
    # promotion_pitches = Pitch.get_pitches('promotion')

    return render_template('index.html', title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

# @main.route('/new_pitch')
# def add_new():
#     return render_template('new_pitch.html')

@main.route('/pitches/business_pitches')
def business_pitches():
    return render_template('business.html')

def add_new():

    title = request.form.get('title')
    new_pitch = Pitch(title=title, complete=False)
    db.session.add(new_pitch)
    db.session.commit()
    return redirect(url_for('business'))

@main.route('/pitches/pickup-lines_pitches')
def pickup_pitches():

    return render_template('pickup_lines.html')

def add_new():

    title = request.form.get('title')
    new_pitch = Pitch(title=title, complete=False)
    db.session.add(new_pitch)
    db.session.commit()
    return redirect(url_for('pickup_pitches'))

@main.route('/pitches/product_pitches')
def product_pitches():
    return render_template('product.html')

def add_new():

    title = request.form.get('title')
    new_pitch = Pitch(title=title, complete=False)
    db.session.add(new_pitch)
    db.session.commit()
    return redirect(url_for('product_pitches'))