import unittest
from user import User
import random
import string


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class

    Args:
        unittest.TestCase :TestCase class that helps in creating a test class
    '''

    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_user = User('mari', 'james', '0712345678')

    def test_init(self):
        '''
        test_init case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name, "mari")
        self.assertEqual(self.new_user.last_name, "james")
        self.assertEqual(self.new_user.password, "0712345678")

    def test_save_user(self):
        '''
        Function to test if a newly created user instance is saved
        '''
        User.users_list.append(self)


    # def test_check_user(self,cls,first_name,password):
    #     '''
	# 	Method that checks if the name and password entered match entries in the users_list
	# 	'''
    #     current_user = ''
    #     for user in User.users_list:
	# 		if (user.first_name == first_name and user.password == password):
    #             current_user = user.first_name
    #     return current_user

if __name__ =='__main__':
    unittest.main()
