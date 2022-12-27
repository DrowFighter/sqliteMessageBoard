import sqlite3
import entityHandler

# TODO: enter correct sql querys into each of the functions with the inputed data
# Books
# · Id (PK)
# · Name
# · Author
# · Year Published
# · Type (1/2/3)


def build_table():
    query_string='''CREATE TABLE if NOT EXISTS books(id INTEGER AUTO_INCREMENT PRIMARY KEY, BookName VARCHAR(255), Author VARCHAR(255), YearPublished INT, Type INT)'''
    return query_string 

def create(data):
    query_string=f"INSERT INTO books(BookName, Author, YearPublished, Type) VALUES {data['name'],data['author'],data['year'],data['type']}"
    return query_string 

def get(data):
    data=[data]   
    cat=data[0]
    value=data[1]
    query_string=f"SELECT * FROM books WHERE {cat} ={value}"
    return query_string 

def getAll(): 
    query_string=f"SELECT * FROM books"
    return query_string 

def update(data):
    data=[data]
    cat=data[0]
    oldvalue=data[1]
    newvalue=data[2]
    query_string=f"UPDATE books SET{cat} ={newvalue} WHERE {cat} ={oldvalue}"
    return query_string 

def delete(data):
    data=[data]
    cat=data[0]
    value=data[1]
    query_string=f"DELETE FROM books WHERE {cat} ={value}"
    return query_string         