import sqlite3
import entityHandler

# TODO: enter correct sql querys into each of the functions with the inputed data
# Books
# · Id (PK)
# · Name
# · Author
# · Year Published
# · Type (1/2/3)


def build_table(data):
    query_string="CREATE TABLE books(id INTEGER AUTO_INCREMENT PRIMARY KEY, BookName VARCHAR(255), Autheor VARCHAR(255), YearPublished int(), Type int())"
    return query_string 

def create(data):
    query_string=f"INSERT INTO TABLE books(BookName, Autheor, YearPublished, Type) {'VALUES' (data(str))}"
    return query_string 

def get(data):
    data=[data]   
    cat=data[0]
    value=data[1]
    query_string=f"SELECT * FROM TABLE books WHERE {cat} ={value}"
    return query_string 

def getAll(data): 
    query_string=f"SELECT * FROM TABLE books"
    return query_string 

def update(data):
    data=[data]
    cat=data[0]
    oldvalue=data[1]
    newvalue=data[2]
    query_string=f"UPDATE TABLE books SET{cat} ={newvalue} WHERE {cat} ={oldvalue}"
    return query_string 

def delete(data):
    data=[data]
    cat=data[0]
    value=data[1]
    query_string=f"DELETE FROM TABLE books WHERE {cat} ={value}"
    return query_string         