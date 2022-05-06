from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField, BooleanField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
  title =StringField('Title' , validators=[DataRequired()])
  description = TextAreaField('What would you like to pitch?', validator=[DataRequired()])
  category = RadioField('Label', choices=[ ('promotionpitch','promotionpitch'), ('interviewpitch','interviewpitch'),('pickuplines','pickuplines'),('productpitch','productpitch')],validators=[DataRequired()])
  submit = SubmitField('submit')
  
class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[DataRequired()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()