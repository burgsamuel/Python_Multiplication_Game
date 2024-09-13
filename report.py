import pandas as pd
import database
import datetime
import sqlite3


class Report:
    
    def __init__(self):
        '''Produce a report for the current user of their games played and scores'''
        
        self.filename = database.DataSave().filename
        
       
        
    def result_html(self, name):
        """Generate a HTML report of the users score"""
        
        name = str(name).title()
        
        conn = sqlite3.connect(self.filename)
        
        query = 'SELECT * FROM userdata WHERE Name = :Name'
        params = {'Name': name}
        
        df =pd.read_sql_query(query, conn, params=params)
        conn.close()

        df['Time_Completed'] = df['Time_Completed'].apply(lambda x: datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M'))
        html = df.to_html(classes='table table-stripped')

        with open(f'{str(name).title()}results.html', 'w') as file:
            file.write(html)

#

