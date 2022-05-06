from flask import render_template, request, redirect,url_for,abort,flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User, Comment, Upvote, Downvote

# views
@main.route('/')
def index():
  '''
  view root page function that returns index page
  '''
  return render_template('index.html')
  