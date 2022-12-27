import sqlite3
import entityHandler
import datetime
from datetime import datetime, timedelta

# TODO: enter correct sql querys into each of the functions with the inputed data
# Loans
# · CustID
# · BookID
# · loanDate
# · returnDate


def build_table():
    query_string='''CREATE TABLE if NOT EXISTS loans(customers_id INTEGER NOT NULL,book_id INTEGER NOT NULL, loanDate TEXT , returnDate TEXT, FOREIGN KEY (customers_id) REFERENCES customers (id),FOREIGN KEY (book_id) REFERENCES books (id))'''
    # query_string='''CREATE TABLE if NOT EXISTS loans(FOREIGN KEY (customers_id)  REFERENCES customers (id),FOREIGN KEY (book_id)  REFERENCES books (id), loanDate TEXT , returnDate TEXT)''' #fix me
    return query_string 

def create(data):
    query_string=f"INSERT INTO loans(id FROM customers as custID INT,id FROM books as bookID INT, loanDate, returnDate(type+loanDate)) VALUES {data.load_date,data.return_date}" #fix me
    return query_string 

def get(data):
    data=[data]   
    cat=data[0]
    value=data[1]
    query_string=f"SELECT * FROM loans WHERE {cat} ={value}"
    return query_string

def getAll(): 
    query_string=f"SELECT * FROM loans"
    return query_string 

    
def update(data):
    data=[data]
    cat=data[0]
    oldvalue=data[1]
    newvalue=data[2]
    query_string=f"UPDATE loans SET{cat} ={newvalue} WHERE {cat} ={oldvalue}"
    return query_string 

def delete(data):
    data=[data]
    cat=data[0]
    value=data[1]
    query_string=f"DELETE FROM loans WHERE {cat} ={value}"
    return query_string     
