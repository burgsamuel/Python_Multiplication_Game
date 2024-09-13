import os

class Intro:
    
    def __init__(self):
            '''Intro Screen for information about the game'''
            
    
    def intro_screen(self, name):
               
        os.system("cls||clear")
        
        input(f'''
    ***************************************
        Welcome to Ten Minute Tables.
    ***************************************
    
    Welcome {str(name).title()}.
                
    Repetition is the key to remembering your times tables quickly. 
    
    You can start at level 1 and work your way through, or start from a level that you believe you need to practice. 
    
    To play, enter the level number and hit enter to start. Answer the given multiplication questions by typing your 
    answer with your keyboard and pressing enter. You will see correct and incorrect answers you have made. 

    You can play single times tables by choosing a level between 1 and 12.
    The questions will be in random order. 

    Mixed times tables are levels 13 to 16, or practicing personally challenging tables with level 17 once you have
    10 or more incorrect answers. 

    The personally challenging times tables level is a collection of questions that you have previously answered incorrectly.   

    The timer is adjustable between 1-10 minutes. 
    Once the timer is up the game will stop and you will see your results.
    But you don't have to stop there if you want to play again!

    Try and complete 10 minutes of times tables every day to see improvement in your times table recall!
    
    Generating a report creates a HTML (webpage) of all your results.
    
    Hit "Enter" to continue:''')