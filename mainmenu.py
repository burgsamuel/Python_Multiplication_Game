from database import DataSave
import levelset
import time
import os

class Mainmenu:
    
    '''Create a Main Menu screen and display optoins for user to select'''

    def __init__(self):
        
        
        self.menu_selection = None
        self.menu_items = {1 : 'Set Username ', 2 : 'Set Timer', 3 : 'Set Level', 4 : 'Instruction Screen', 5 : 'Last Results',
                           6 : 'Play Game!', 7 : 'Your Personal Challenge', 8 : 'Generate Report'}

    def menu_screen(self):
        
        '''Draw graphics for main menu screen'''
    
        while True:
            
            os.system("cls||clear")

            # Graphics for display
            print('*' * 40)
            print("        ------  Main Menu  ------")
            print('*' * 40 + '\n')
            print("Enter [q] to quit!\n")
            
            user_level = DataSave().get_level()
            
            for key, value in self.menu_items.items():
                if key == 1:
                    print(f'[{key}]  {value}:       --> {str(DataSave().get_username()).title()}')
                elif key == 2:
                    print(f'[{key}]  {value}:           --> {DataSave().get_timer()} min')
                elif key == 3:
                    print(f'[{key}]  {value}:           --> {levelset.SetLevel().level_setup(user_level)[0]} x Tables ')
                elif key == 4:
                    print(f'[{key}]  {value}')
                elif key == 5:
                    print(f'[{key}]  {value}')
                elif key == 6:
                    print(f'[{key}]  {value}')
                else:
                    print(f'[{key}]  {value}')


            print('\n')
            print('Enter Selection and press [Enter]')
            self.menu_selection = input('Selection: ')
            
            try:
                
                if self.menu_selection == 'q' or self.menu_selection == "Q" or self.menu_selection == 'exit':
                    return str('q')
                elif self.menu_selection == '':
                    return 'play'
                selection = int(self.menu_selection)
            
            except ValueError:
                print('Enter a correct number')
            except TypeError:
                print('Enter a correct number')
            
            try:    
                if selection <= len(self.menu_items) and selection >= 1:
                    return selection
                else:
                    print('Enter a number that matches menu item, e.g "2"')
            except UnboundLocalError:
                print(f'Enter a valid number 1-{len(self.menu_items)} or "q" to quit')
                time.sleep(1.5)



            
