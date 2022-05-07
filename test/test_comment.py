import unittest
from app.models import User, Comment, Pitch
from app import db
from flask_login import current_user

class TestPitch(unittest.TestCase):

  def setUp(self):
    self.new_pitch = Pitch(pitch_content = "This is a pitch", pitch_category='Product',user=self.user_jane)
    self.new_comment = Comment(comment_content = "This is a comment", pitch=self.new_pitch, user=self.user_jane)

  def tearDown(self):
    db.session.delete(self)
    User.query.commit()

  def test_instance(self):
    self.assertTrue(isinstance(self.new_comment,Comment))

  def test_check_instance_variable(self):
    self.assertEqual(self.new_comment_content, "This is a comment")
    self.assertEqual(self.new_comment.pitch, self.new_pitch)     