from database import DataSave
import pyautogui
import time
import os


class Runtime:
    
    def __init__(self):
        pass
    
        # Timer access
        self.time_remaining = None
        self.game_running = True
    
    
    def set_run_time(self, old_timer):
        '''User will enter a time to set run timer'''
        
        os.system("cls||clear")
        
        # Graphics for display
        print('*' * 33)
        print(" ------  Timer Selection  ------")
        print('*' * 33 + '\n')
        
        print("Enter time to play between 1-10 minutes: e.g 5 for 5 minutes\n")
        
        while True:
            
            
            timer = input("Minutes: ")
            
            if timer == '':
                print("Enter a number between 1-10")
            
            try:
                
                timer = float(timer)
                if timer > 10:
                    
                    print('Enter a number lower than 10!')     
                elif timer <= 0:
                    
                    print("Enter a number higher than 0!")          
                else:
                    
                    timer = DataSave().update_timer(old_timer, timer)
                    return timer
                
            except ValueError:
                print('Value error, enter a correct value!')
            except TypeError:
                print('Type Error, Enter a correct number!')
                
                
    def run_time(self):
    
        ''' Using Epoch Time (seconds) to count and follow the timers
            simple conversions will be used.
            Running a seperate thread to keep time.'''
            
        
        timer_total = float(DataSave().get_timer()) * 60
        start_timer = time.time()
        timer_end = start_timer + timer_total
        
        while start_timer <= timer_end:
            
            start_timer = time.time()
            self.time_remaining = timer_end - start_timer
            time.sleep(1)

        self.game_running = False
        os.system("cls||clear")
        print('Timer Finished')
        time.sleep(1)
        for i in range(5):
            pyautogui.press('backspace')
        pyautogui.press('enter')
        
