 
import unittest
from app.models import Comment
from datetime import datetime
class CommentTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment(body = 'That is a great blog post', blog_id = 1 , posted ='2020-04-05 08:26:19.580874' ,author_id = 4)

    def tearDown(self):
        Comment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.body,'That is a great blog post')
        self.assertEquals(self.new_comment.posted,'2020-04-05 08:26:19.580874')
        self.assertEquals(self.new_comment.author_id,4)
        self.assertEquals(self.new_comment.blog_id,1)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(1)
        self.assertTrue(len(got_comments) == 1)
