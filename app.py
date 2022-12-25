import entityHandler
import messageHandler   

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
    return result

# init of the handler classes
entity_handler = entityHandler.entityHandler()
message_handler = messageHandler.messageHandler(messageCallback)

# create the 3 required tables
# TODO check if the tabels are already created
entity_handler.build_table('books')
entity_handler.build_table('customers')
entity_handler.build_table('loans')