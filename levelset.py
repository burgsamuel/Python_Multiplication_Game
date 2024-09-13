from database import DataSave
import time
import os


class SetLevel:
    
    
    def __init__(self):
        
        
        # Setting of levels
        self.game_running = None
        
        
        self.levels = {1 : 1, 2 : 2, 3 : 10, 4 : 5, 5 : 11, 6 : 3, 7 : 4, 8 : 6, 9 : 7,
                       10 : 8, 11 : 9, 12 : 12, 
                       13 : [1, 2, 5, 10, 11],
                       14 : [3, 4, 6, 7],
                       15 : [3, 4, 6, 7, 8, 9, 12],
                       16 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]} 



    def set_level(self, old_level):
        
        '''Select a level from levelset.py, this is in a dictionary.
           level 1-12 returns a single value.
           level 13 and up returns a list of levels'''
             
        while True:
            os.system("cls||clear")
            
            # Graphics for display
            print('*' * 33)
            print(" ------  Level Selection  ------")
            print('*' * 33 + '\n')
            
            #loop over the levels dict to output levels to a user
            for key, value in self.levels.items():   
                if key <= 12:
                    print(f'Level: {str(key).rjust(2)} - {str(value).rjust(2)} X Tables') 
                elif key == 16:
                    print(f"Level: {str(key).rjust(2)} - ", end='')
                    print(' All times tables 1 - 12.')
                else:
                    print(f"Level: {str(key).rjust(2)} - ", end='')
                    print(*value, end='')
                    print(' X Tables')
            print('')

            # User Enter a level 
            user_level_selected = input("Please select your level: ")
            
            # Make sure the user enters a valid level
            try:
                user_level_selected = int(user_level_selected)
                
                if user_level_selected >= 1 and user_level_selected <= 12:
                    self.game_running = True
                    DataSave().update_level(old_level, user_level_selected)
                    return self.levels[user_level_selected], user_level_selected
                
                # If the higher levels are select (These return a list)
                elif user_level_selected >= 13 and user_level_selected <= 16:
                    self.game_running = True
                    DataSave().update_level(old_level, user_level_selected)
                    return list(self.levels[user_level_selected]), user_level_selected
                
                else:
                    print('Invalid level selection!')
                    time.sleep(1)
                    
            except ValueError:
                print('Enter a proper a number!')               
                time.sleep(1)
                

    def level_setup(self, level):
        
        if level >= 1 and level <= 12:
            return self.levels[level], level
                
        # If the higher levels are select (These return a list)
        elif level>= 13 and level <= 16:
            return list(self.levels[level]), level