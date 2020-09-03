from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

database = {100: {'id': 100, 'insurance': 10000}, 101: {'id': 101, 'insurance': 15000}}


class InsuranceController(Resource):
    def get(self, id):
        return database.get(id)


api.add_resource(InsuranceController, '/insurance/<int:id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9020)
