import sqlite3
from entities import books
from entities import customers
from entities import loans

dbname = 'sql.db'

class entityHandler:

    def __init__(self):
        try:
            
            # Connect to DB and create a cursor
            self.sqliteConnection = sqlite3.connect(dbname)
            self.cursor = self.sqliteConnection.cursor()
            print('DB Init')
        # Handle errors
        except sqlite3.Error as error:
            print('Error occured - ', error)
    
    def build_table(self, type, data):
        result = None 
        query_string=""
        if type == "books" : 
            query_string=books.build_table(data)
        elif type == "customers" : 
            query_string=customers.build_table(data)
        elif type == "loans" : 
            query_string=loans.build_table(data)
        if query_string != "" :result = self.cursor.execute(query_string)
        return  result

    def create(self, type, data):
        result = None 
        query_string=""
        if type == "books" : 
            query_string=books.create(data)
        elif type == "customers" : 
            query_string=customers.create(data)
        elif type == "loans" : 
            query_string=loans.create(data)
        if query_string != "" : result = self.cursor.execute(query_string)
        return  result

    def get(self, type, data):
        result =None
        query_string=""
        if type == "books" : 
            query_string=books.get(data)
        elif type == "customers" : 
            query_string=customers.get(data)
        elif type == "loans" : 
            query_string=loans.get(data)
        if query_string != "" : result = self.cursor.execute(query_string)
        return   result

    def getAll(self, type, data):
        result = None
        query_string=""
        if type == "books" : 
            query_string=books.getAll(data)
        elif type == "customers" : 
            query_string=customers.getAll(data)
        elif type == "loans" : 
            query_string=loans.getAll(data)
        if query_string != "" : result = self.cursor.execute(query_string)
        return   result

    def update(self, type, data):
        result = None 
        query_string=""
        if type == "books" : 
            query_string=books.update(data)
        elif type == "customers" : 
            query_string=customers.update(data)
        elif type == "loans" : 
            query_string=loans.update(data)
        if query_string != "" : result = self.cursor.execute(query_string)
        return   result

    def delete(self, type, data):
        result =None
        query_string=""
        if type == "books" : 
            query_string=books.delete(data)
        elif type == "customers" : 
            query_string=customers.delete(data)
        elif type == "loans" : 
            query_string=loans.delete(data)
        if query_string != "" : result = self.cursor.execute(query_string)
        return     result      

