import sqlite3
import entityHandler

# TODO: enter correct sql querys into each of the functions with the inputed data
# Customers
# · Id (PK)
# · Name
# · City
# · Age


def build_table():
    query_string='''CREATE TABLE if NOT EXISTS customers(id INTEGER AUTO_INCREMENT PRIMARY KEY, cName VARCHAR(255), city VARCHAR(255), age INT)'''
    return query_string 

def create(data):
    query_string=f"INSERT INTO customers(cName, city, age) VALUES {data['name'],data['city'],data['age']}"  
    return query_string 

def get(data):
    data=[data]   
    cat=data[0]
    value=data[1]
    query_string=f"SELECT * FROM customers WHERE {cat} ={value}"
    return query_string 

def getAll(): 
    query_string=f"SELECT * FROM customers"
    return query_string 

def update(data):
    data=[data]
    cat=data[0]
    oldvalue=data[1]
    newvalue=data[2]
    query_string=f"UPDATE customers SET{cat} ={newvalue} WHERE {cat} ={oldvalue}"
    return query_string 

def delete(data):
    data=[data]
    cat=data[0]
    value=data[1]
    query_string=f"DELETE FROM customers WHERE {cat} ={value}"
    return query_string         