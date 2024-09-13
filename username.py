from database import DataSave
import os


class Username:    
    
    
    ''' Username will be handled in own class'''
    
    def __init__(self):
        
        pass

                    
    
    def create_user_name(self, old_name):
        
        ''' Enter a username: (This will also be the filename) 
            With some basic error checking'''
            
        
        os.system("cls||clear")
        # Graphics for display
        print('*' * 33)
        print("  ------ Enter Username  ------")
        print('*' * 33 + '\n')
        
        attemps = 0
        while True:
            
            if attemps > 3:
                os.system("cls||clear")
                attemps = 0
                
            name = str(input("Enter Username: "))
            
            if len(name) > 20:
                print("Enter a shorter name!")
                attemps += 1
            elif len(name) == 0:
                print('Enter a User Name!')
                attemps += 1
            elif name.isalpha() == False:
                print("Enter a Valid User Name! (no numbers)")
                attemps += 1
            elif name == '':   
                return old_name    
            else:
                self.user_name = name.lower()
                self.new_name = DataSave().update_username(old_name, self.user_name)

                return self.new_name



