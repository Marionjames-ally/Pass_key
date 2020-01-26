import unittest
from user import User

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
        self.new_user = User('mari','james','0712345678')

    def test_init(self):
        '''
        test_init case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.f_name,"mari")
        self.assertEqual(self.new_user.l_name,"james")
        self.assertEqual(self.new_user.password,"0712345678")

    def test_save_user(self):
        '''
        Function to test if a newly created user instance is saved
		'''
        User.users_list.append(self)


if __name__ =='__main__':
    unittest.main()