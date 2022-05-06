from flask import render_template, request, redirect,url_for,abort,flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User, Comment, Upvote, Downvote
from flask.views import View, MethodView
from .. import db

# views
@main.route('/')
def index():
  '''
  view root page function that returns index page
  '''
  title ='Home'
  pitch =Pitch.query.filter_by().all()
  pickuplines = Pitch.query.filter_by(category="pickuplines")
  interviewpitch = Pitch.query.filter_by(category = "interviewpitch")
  promotionpitch = Pitch.query.filter_by(category = "promotionpitch")
  productpitch = Pitch.query.filter_by(category = "productpitch")

  return render_template('home.html', title=title, pitch = pitch,pickuplines=pickuplines, interviewpitch= interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch)
  