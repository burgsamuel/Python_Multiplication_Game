from database import DataSave
from results import Results
import multiprocessing
import instructions
import mainmenu
import levelset
import username
import runtime
import report
import random
import time
import sys
import os



class Tables_in_10:
    
    
    def __init__(self):
        
        
        
        # Game Running  
        
        self.levels = levelset.SetLevel()      
        self.intro = instructions.Intro()  
        self.menu = mainmenu.Mainmenu()
        self.runtime = runtime.Runtime()
        self.user = username.Username()     
        self.results = Results()
        
        #check this variable for reports in trouble areas
        self.trouble = True  
        self.troubleupdaterindex = 1
        self.troubleupdater = {}
          
    
    
    
    def play_tables(self, level, second_list):
        
        '''Gameplay will start here 
            need to bring the level selected into here '''
         
        u1.results.counter = 1
        u1.results.correct_answsers = 0 
        u1.results.incorrect_answers = 0
        
        if level == 17:
            # Create a dictonary to count correct times a single answer is correct
            for item in second_list:
                self.troubleupdater[item] = 0
        else:
            pass
        
        timer_process = multiprocessing.Process(target=u1.runtime.run_time, daemon=True)
        timer_process.start()
          

        while timer_process.is_alive():
            
            os.system("cls||clear")
            
            # Graphics for display
            print('*' * 43)
            print("          ------  Game on  ------")
            print('*' * 43 + '\n')
            
            
            print(f'Total Answered: {u1.results.counter - 1}. Correct: {u1.results.correct_answsers}. Incorrect: {u1.results.incorrect_answers}\n')
            print(' --Enter [q] or [quit] to exit at anytime--\n')         
               
             
            # Using the level selected funtion to set the tables parameter
            if level == 17:
                '''This is the area for the trouble Questions'''
                try:
                    
                    questions = random.choice(second_list)
                    
                    # Have to have a certain amount of incorrect questions to play
                    if len(second_list) < 5:
                        os.system("cls||clear")
                        print("You have less than 10 incorrect answers!")
                        print("Come back later! ")
                        
                        # Kill the timer process early 
                        timer_process.kill()
                        
                        # This is used to make a report 
                        self.trouble = False
                        time.sleep(3)
                        break  
                    
                    else:
                        first = questions[0]
                        second = questions[1]
                        # This is used to make a report 
                        self.trouble = True
                        
                        
                except IndexError:
                    os.system("cls||clear")
                    print("You havent got any wrong!")
                    print("Come back later!")
                    timer_process.kill()
                    
                    # This is used to make a report 
                    self.trouble = False
                    time.sleep(3)   
                    break
                
                
            elif DataSave().get_level() < 13 and DataSave().get_level() >= 1:    
                first = level
                # Second variable will be randomaly between 1 and 12    
                second = random.randint(1, 12)
            
            
            elif DataSave().get_level() > 12 and DataSave().get_level():
                
                first = random.choice(list(level))
                # Second variable will be randomaly between 1 and 12    
                second = random.randint(1, 12)   
                
            else:    
                pass           
            
            self.answer = first * second
            
            # Asking for user input
            user_answer = input(f'{u1.results.counter}:     {first} X {second} = ')
            
            
            if timer_process.is_alive():
                
                pass
                
            else:
                break
            
            if user_answer == "q" or user_answer == "Q" or user_answer == 'quit':
                timer_process.kill()
                break
            # checking input to avoid a crash and also game logic and counters 
            try:
                              
                user_answer = int(user_answer)
                
                if user_answer != self.answer:    
                    print(f'Answer is: {self.answer}')
                    u1.results.counter += 1
                    u1.results.incorrect_answers += 1
                    
                    #check if is already in database before storing
                    if data.check_if_in_incorrect(first, second) == None:
                        DataSave().store_incorrect(first, second)
                        
                    time.sleep(1)
                    
                else:
                    print(f'Correct!')
                    u1.results.counter += 1
                    u1.results.correct_answsers += 1
                    
                    # count a correct answer for trouble question in dictonary to later
                    # delete the question if answered correct enough
                    if level == 17:
                        for key, value in self.troubleupdater.items():
                            if questions == key:
                                self.troubleupdater[questions] = value + 1
                            else:
                                pass
                    else:
                        pass        
                            
                    time.sleep(.5)
                    
                    
                
            except ValueError:
                print('')     
                time.sleep(1)                      
 
        


if __name__ == '__main__': 

    if sys.platform.startswith('win'):
        # On Windows calling this function is necessary. to prevent glitches
        multiprocessing.freeze_support()
    
    # Initlize classes
    data = DataSave()
    u1 = Tables_in_10()
    
    # Defaults to start game 
    
    
    data.create_db()
    
    name = data.get_username()
    timer = data.get_timer()
    user_level = data.get_level()
    level = levelset.SetLevel().level_setup(user_level)[0]
    
    second_list = None
    
    while True:
    
        selection = u1.menu.menu_screen()

        if selection == 1:
            name = u1.user.create_user_name(name)
            
        elif selection == 2:
            timer = data.get_timer()
            timer = u1.runtime.set_run_time(timer)
            
        elif selection == 3:
            level, user_level = u1.levels.set_level(user_level)
            
        elif selection == 4:
            u1.intro.intro_screen(name)
   
        elif selection == 5:
            
            actual_time = data.retrive_actual_time()
            for i in actual_time:
                actual_time = i
            u1.results.results_screen(timer, user_level, actual_time)
   
        elif selection == 6:
            
            timer = data.get_timer() 
            
            # Time the actual gameplay for database results
            actual_time_start = time.perf_counter()
            u1.play_tables(level, second_list)      
            actual_time = round(time.perf_counter() - actual_time_start, 2)
            
            # Save the game results into the database
            data.save_results(name, user_level, timer, actual_time, u1.results.counter -1, 
                                    u1.results.correct_answsers, u1.results.incorrect_answers)   
            u1.results.results_screen(timer, user_level, actual_time)
            
        elif selection == 7:
           
            first = 17
            second_list = data.incorrect_questions()
            timer = data.get_timer() 
            
            # Time the actual gameplay for database results
            actual_time_start = time.perf_counter()
            u1.play_tables(first, second_list) 
            actual_time = round(time.perf_counter() - actual_time_start, 2)
            
            if u1.trouble:
                data.save_results(name, 17, timer, actual_time, u1.results.counter -1, 
                                        u1.results.correct_answsers, u1.results.incorrect_answers)        
                u1.results.results_screen(timer, user_level, actual_time)
            
            # Delete Values from data base that have been successfully answered    
            for key, value in u1.troubleupdater.items():
                if value >= 3:
                    first = key[0]
                    second = key[1]
                    data.troublescoreupdate(first, second)        
                else:
                    pass
                
        elif selection == 8: 
               
            report.Report().result_html(name)
            print('Report created...')
            time.sleep(2)
                  
        elif selection == 'play':
            pass
        
        elif selection == 'q':
            break
        
        
            

