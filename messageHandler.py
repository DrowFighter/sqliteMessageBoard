from flask import Flask, request, jsonify


# app = None
messageCallback = None

class messageHandler:

    def __init__(self, callback,app,cross_origin):
        # app = Flask(__name__)
        messageCallback = callback

        @app.route('/add')
        def add():         
            print(request.args)
            data = request.args
            callType = request.args.get('callType')
            action = 'create'
            return messageCallback(callType, action, data)

        @app.route('/loan_book')           
        def loan_book():         
            print(request.args)
            data = request.args
            callType = 'loans'
            action = 'create'
            return messageCallback(callType, action, data)

        @app.route('/return_book')           
        def return_book():         
            print(request.args)
            data = request.args
            callType = 'loans'
            action = 'delete'
            return messageCallback(callType, action, data)

        @app.route('/get')           
        def get():         
            print(request.args)
            data = request.args
            callType = request.args.get('callType')
            action = 'get'
            return messageCallback(callType, action, data)

        @app.route('/get_late_loans')           
        def get_late_loans():         
            print(request.args)
            data = request.args
            callType = 'loans'
            action = 'get'
            return messageCallback(callType, action, data)

        @app.route('/getAll')       
        def getAll():         
            print(request)
            print(request.args)
            data = request.args
            callType = request.args.get('callType')
            action = 'getAll'
            return messageCallback(callType, action, data)
            # return jsonify( data = messageCallback(callType, action, data))


        @app.route('/delete')           
        def delete():         
            print(request.args)
            data = request.args
            callType = request.args.get('callType')
            action = 'delete'
            return messageCallback(callType, action, data)

        if __name__ == '__main__':
            # run app in debug mode on port 5000
            app.run(debug=True, port=5000)
