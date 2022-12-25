import sqlite3
import entityHandler

# TODO: enter correct sql querys into each of the functions with the inputed data
# Customers
# · Id (PK)
# · Name
# · City
# · Age


def build_table(data):
    query_string="CREATE TABLE customers(id INTEGER AUTO_INCREMENT PRIMARY KEY, cName VARCHAR(255), city VARCHAR(255), age int())"
    return query_string 

def create(data):
    query_string=f"INSERT INTO TABLE customers(cName, city, age) {'VALUES' (data(str))}"
    return query_string 

def get(data):
    data=[data]   
    cat=data[0]
    value=data[1]
    query_string=f"SELECT * FROM TABLE customers WHERE {cat} ={value}"
    return query_string 

def getAll(data): 
    query_string=f"SELECT * FROM TABLE customers"
    return query_string 

def update(data):
    data=[data]
    cat=data[0]
    oldvalue=data[1]
    newvalue=data[2]
    query_string=f"UPDATE TABLE customers SET{cat} ={newvalue} WHERE {cat} ={oldvalue}"
    return query_string 

def delete(data):
    data=[data]
    cat=data[0]
    value=data[1]
    query_string=f"DELETE FROM TABLE customers WHERE {cat} ={value}"
    return query_string         