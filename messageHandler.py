from flask import Flask, request


app = None
messageCallback = None

class messageHandler:

    def __init__(self, callback):
        app = Flask(__name__)
        messageCallback = callback

        @app.route('/add')
        def add():         
            print(request.args)
            data = request.args
            type = request.args.get('type')
            action = 'create'
            return messageCallback(type, action, data)

        @app.route('/loan_book')           
        def loan_book():         
            print(request.args)
            data = request.args
            type = 'loans'
            action = 'create'
            return messageCallback(type, action, data)

        @app.route('/return_book')           
        def return_book():         
            print(request.args)
            data = request.args
            type = 'loans'
            action = 'delete'
            return messageCallback(type, action, data)

        @app.route('/get')           
        def get():         
            print(request.args)
            data = request.args
            type = request.args.get('type')
            action = 'get'
            return messageCallback(type, action, data)

        @app.route('/get_late_loans')           
        def get_late_loans():         
            print(request.args)
            data = request.args
            type = 'loans'
            action = 'get'
            return messageCallback(type, action, data)

        @app.route('/getAll')           
        def getAll():         
            print(request.args)
            data = request.args
            type = request.args.get('type')
            action = 'getAll'
            return messageCallback(type, action, data)

        @app.route('/delete')           
        def delete():         
            print(request.args)
            data = request.args
            type = request.args.get('type')
            action = 'delete'
            return messageCallback(type, action, data)

        if __name__ == '__main__':
            # run app in debug mode on port 5000
            app.run(debug=True, port=5000)
