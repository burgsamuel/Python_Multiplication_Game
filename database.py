import sqlite3
import time


class DataSave:
    
    """Use a database to store the scores, the trouble areas 
        and to save user information"""
           
    def __init__(self):
        
        self.filename = 'data.db'
        self.username = None
        self.timer = None
        self.level = None
        
        
        
    def create_db(self):
        
        ''' Check if data base has been created.
            Create one if it has not.'''
            
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        
        try:    
            # Create a user table
            c.execute('CREATE TABLE User (name TEXT, level INTEGER, timer Real)')
            conn.commit()
            
            c.execute("INSERT INTO User VALUES (:name, :level, :timer)", {'name':'Guest', 'level': 1, 'timer': 1 })
            conn.commit()
        
        except sqlite3.OperationalError:
            print('Table [User] already exists')

             
        
            # Create a table for data and progress
        c.execute('''CREATE TABLE IF NOT EXISTS userdata (
                    Time_Completed REAL, Name TEXT, Level INTEGER, Timer REAL, Actual_Time REAL,
                    Total_Questions INTEGER, Correct INTEGER, Incorrect INTEGER, QPM REAL)''')     
        
        
            # Creater a table to track incoorect answers
        c.execute('CREATE TABLE IF NOT EXISTS incorrect (first INTEGER, second INTEGER, counter INTEGER)')
        conn.commit()
        
        c.close()

        
        
    def update_username(self, oldname, newname):
        
        ''' This method updates the username, first arg is the oldername, second arg is the new username, 
            this updates the User table'''

        
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("UPDATE User SET name = :name WHERE name = :olduser", {'name': newname, 'olduser': oldname})
        conn.commit()
        
        c.close()
        
        return str(newname)
      
        
    def get_username(self):
        
        '''Retrive the username from the database to set variables with in the program'''
        
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("SELECT name FROM User")
        self.username = c.fetchone()[0]
        
        conn.commit()
        
        c.close()
        
        return self.username
        

    def update_level(self, oldlevel, newlevel):
        
        '''This updates the level selected, first arg is the old level, second arg
            is the new level required {User table updated}'''
        
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("UPDATE User SET level = :level WHERE level = :oldlevel", {'level': newlevel, 'oldlevel': oldlevel})
        conn.commit()
        
        c.close()
 
    
    
    def get_level(self):
    
        '''Retrive the level setting from the database to set variables with in the program'''
        
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("SELECT level FROM User")
        self.level = c.fetchone()[0]
        
        conn.commit()
        
        c.close()  
          
        return self.level  
            
    
    def update_timer(self, oldtimer, newtimer):
        
        '''This updates the run timer, first arg is the old timer, second arg
            is the new timer required {User table updated}'''
        
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("UPDATE User SET timer = :timer WHERE timer = :oldtimer", {'timer': newtimer, 'oldtimer': oldtimer})
        conn.commit()
        
        c.close()
    
    
    
    def get_timer(self):
    
        '''Retrive the timer setting from the database to set variables with in the program'''
        
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("SELECT timer FROM User")
        self.timer = c.fetchone()[0]
        
        conn.commit()
        
        c.close()  

        return self.timer


    def save_results(self, name, level, timer, actual_time, totalquestions, correct, incorrect):
        
        '''Save the results of played games into the database for later anaylasis'''
        
        time_completed = time.time()
        name = str(name).title()
        
        if actual_time > 0 and actual_time < 1:
            actual_time = actual_time
        else:
            actual_time = round(actual_time / 60, 2)
        
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("""INSERT INTO userdata VALUES(
                    :Time_Completed, :Name, :Level, :Timer, :Actual_Time, :Total_Questions, :Correct, :Incorrect, :QPM) """, 
                    {'Time_Completed': time_completed, 'Name': name, 'Level': level, 'Timer': timer, 'Actual_Time' : actual_time, 'Total_Questions': totalquestions,
                     'Correct': correct, 'Incorrect': incorrect, 'QPM' : round((totalquestions) / timer, 1)})
        conn.commit()
        
        c.close()
        

    def store_incorrect(self, first, second):
        
        ''' Store the table by first and second that the user incorrectly answered.
            This will be used as a level to imprve areas where the user needs work
            CREATE TABLE IF NOT EXISTS incorrect (first INTEGER, second INTEGER)'''   
            
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("INSERT INTO incorrect VALUES (:first, :second)", 
                  {'first' : first, 'second' : second})
        
        conn.commit()
        
        c.close()



    def incorrect_questions(self):
        
        '''Retrieve incorrect questions from the database and store into questions list
            these will be used to play the troubles level.'''
        
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("SELECT * FROM incorrect")
        questions = c.fetchall()
        
        conn.commit()
        c.close()  
          
        return questions
        


    def retrive_actual_time(self):
        
        ''' Retrive last actual time for results screen'''   
            
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("SELECT Actual_Time FROM userdata")
        result = c.fetchall()
        c.close()
        
        numbers = []
        for i in result:
            numbers.append(i)
        
        
        return numbers[-1]
    
    
    def troublescoreupdate(self, first, second):
    
        '''Delete from the trouble table questions that have been answered correctly
            multiple times. So the table doesnt constantly grow massive over time'''
        
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("DELETE FROM incorrect WHERE first = :first AND second = :second", {'first' : first, 'second' : second}) 
        
        conn.commit() 
        c.close()  

        
    def check_if_in_incorrect(self, first, second):
        '''Check if the incorrect is already in the database so another isnt duplicated'''
        
        conn = sqlite3.connect(self.filename)
        c = conn.cursor()
        
        c.execute("SELECT * FROM incorrect WHERE first = :first AND second = :second", {'first' : first, 'second' : second}) 
        ifin = c.fetchone()
         
        c.close() 
        
        return ifin

