import unittest
from app.models import User, Comment
from app import db

class TestComment(unittest.TestCase):

  def setUp(self):
    self.new_comment = Comment(Comment_content = "This is a comment", user=self.user_jane)

  def tearDown(self):
    db.session.delete(self)
    User.query.commit()

  def test_instance(self):
    self.assertTrue(isinstance(self.new_comment,Comment))

  def test_check_instance_variable(self):
    self.assertEqual(self.new_comment_content, "This is a comment")     