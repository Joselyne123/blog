import unittest
from app.models import  Blog
from datetime import datetime
class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the blog post class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Blog(id=1, user_id=1, body='Python Must Be Crazy',title='Cryptography',posted='2020-04-05 08:26:19.580874')
                            

    def tearDown(self):

        Blog.query.delete()
        

    def test_instance(self):
        '''
        test case that uses the isinstance() to check if object is an instance of Comment class
        '''
        self.assertTrue(isinstance(self.new_post,Blog))
        