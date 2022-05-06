from flask import render_template, request, redirect,url_for
from . import main

# views
@main.route('/')
def index():
  '''
  view root page function that returns index page
  '''
  return render_template('index.html')
  