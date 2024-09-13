import time
import os


class Results:
    
    def __init__(self):
    
        self.incorrect_answers = 0 
        self.correct_answsers = 0 
        self.counter = 1
        
        

    def results_screen(self, timer, level, actual_time):
        
        ''' Display a summary for the last game played
            Pass in the timer selection as an argument'''
        
        self.question_per_min = round((self.counter - 1) / timer, 1)
        
        try:
            percantage_correct = (self.correct_answsers / (self.counter - 1)) * 100
        except ZeroDivisionError:
            percantage_correct = 0
        
        actual_time = round(actual_time / 60, 2)
        
        os.system("cls||clear")
            
        # Graphics for display
        print('*' * 43)
        print("          ------ Results ------")
        print('*' * 43 + '\n')
        
        print(f'Level Selected     ---> : {level} ')
        print(f'Timer Min Set      ---> : {timer} min\n')
        if actual_time < 1 and actual_time > 0:
            print(f'Time Played        ---> : < 1 min\n')
        else:
            print(f'Time Played        ---> : {actual_time} min\n')
            
        print(f'Total Questions Answered: {self.counter - 1} ')
        
        print(f'Total Correct Answers   : {self.correct_answsers} ')
 
        print(f'Total Incorrect Answers : {self.incorrect_answers}\n')


        print(f'Total Correct Score as %: {round(int(percantage_correct), 1)}% \n')
        print(f'Total questions per min : {self.question_per_min}\n')




        # Prompts for ideas to what levels to try
        if level <= 15 and level and percantage_correct >= 85:
            print(f"With such a great score on level: {level}")
            print(f'It might be time to try level: {level + 1}\n')
            if self.question_per_min >= 25:
                print('Your speed is also blazing, nice work!\n')
        
        # If there are no more levels
        elif level == 16 and percantage_correct >= 75:
            print(f'Well done you have scored {percantage_correct}%')
            print('Keep up the good work!!!\n')
        elif level == 16 and percantage_correct >= 95:
            print(f'Well done you have scored {percantage_correct}%')
            print('Excellent score, you have mastered the game!')
            if self.question_per_min >= 25:
                print('Your speed is also blazing, nice work!\n')
            print('Maybe try playing your trouble areas from the main menu!\n')
        
        # Maybe suggesting easier levels    
        elif level > 1 and percantage_correct < 50:
            print(f"You played well on Level: {level}\n") 
            print(f"If this feels too hard maybe try level: {level - 1}\n")
            if self.question_per_min >= 25:
                print('Dont worry about going to fast, focus on the question!\n')
        elif level == 1 and percantage_correct < 50:
            print('Great try, remember to keep up regular practise!\n')
            
        # If a level wasnt selected and the results screen appeared
        elif level == 0:
            print(f"You actually didnt play, this is level: {level}\n")
        else:
            print(f"You played well on Level: {level}")
            print('Keep up the practise.\n')
        
        
        
        time.sleep(4)
        
        
        
        input('Hit "Enter" to continue')
        
        
    
        