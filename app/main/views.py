from flask import render_template, request, redirect,url_for,abort,flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User, Comment, Upvote, Downvote
from flask.views import View, MethodView
from .. import db
from .forms import PitchForm, CommentForm, UpvoteForm, UpdateProfile

# views
@main.route('/')
def index():
    pitches = Pitch.query.all()
    job = Pitch.query.filter_by(category = 'Job').all() 
    event = Pitch.query.filter_by(category = 'Events').all()
    advertisement = Pitch.query.filter_by(category = 'Advertisement').all()
    
    return render_template('index.html', job = job,event = event, pitches = pitches,advertisement= advertisement)

@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('pitches.html',form=form)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)
  return render_template("profile/profile.html",user = user)

@main.route('/user/<uname>/update',methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username =uname).first()
  if user is None:
    abort(404)

  form = UpdateProfile()
  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

  return render_template('profile/update.html',form = form)    


  