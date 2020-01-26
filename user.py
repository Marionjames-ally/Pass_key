
class User:
    '''
    class that generates new instances of user

    '''
    
    users_list=[]
    def __init__(self,f_name,l_name,password):
        self.f_name = f_name
        self.l_name = l_name
        self.password = password

    def save_user(self):
        '''
        Function to save a newly created user instance
		'''
        User.users_list.append(self)
