from flask import Flask
from flask_cors import CORS, cross_origin
import entityHandler
import messageHandler   


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/DB')

# function which connects the SQL controler with the flask messageHandler
def messageCallback(type,action, data):
    result = None
    if action == 'create' : 
        result = entity_handler.create(type,data)
    elif action == 'get' : 
        result = entity_handler.get(type,data)
    elif action == 'getAll' : 
        result = entity_handler.getAll(type,data)
    elif action == 'update' : 
        result = entity_handler.update(type,data)
    elif action == 'delete' : 
        result = entity_handler.delete(type,data)
    print ('result', result)
    return result 


# init of the handler classes
entity_handler = entityHandler.entityHandler()
message_handler = messageHandler.messageHandler(messageCallback,app,cross_origin)

# create the 3 required tables
# TODO check if the tabels are already created
entity_handler.build_table('books')
entity_handler.build_table('customers')
entity_handler.build_table('loans')