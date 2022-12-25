import sqlite3
import entityHandler

# TODO: enter correct sql querys into each of the functions with the inputed data
# Loans
# · CustID
# · BookID
# · loanDate
# · returnDate


def build_table(data):
    query_string="CREATE TABLE loans(FOREIGN KEY (customers_id)  REFERENCES customers (id),FOREIGN KEY (book_id)  REFERENCES books (id), loanDate DATE() , returnDate DATE())" #fix me
    return query_string 

def create(data):
    query_string=f"INSERT INTO TABLE loans(id FROM customers as custID,id FROM books as bookID int(), loanDate, returnDate(type+loanDate)) {'VALUES' (data(str))}" #fix me
    return query_string 

def get(data):
    data=[data]   
    cat=data[0]
    value=data[1]
    query_string=f"SELECT * FROM TABLE loans WHERE {cat} ={value}"
    return query_string

def getAll(data): 
    query_string=f"SELECT * FROM TABLE loans"
    return query_string 

    
def update(data):
    data=[data]
    cat=data[0]
    oldvalue=data[1]
    newvalue=data[2]
    query_string=f"UPDATE TABLE loans SET{cat} ={newvalue} WHERE {cat} ={oldvalue}"
    return query_string 

def delete(data):
    data=[data]
    cat=data[0]
    value=data[1]
    query_string=f"DELETE FROM TABLE loans WHERE {cat} ={value}"
    return query_string     
