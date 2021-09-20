from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)
version = '2'
devs = [
            {
                'name':'Wanderson Fontes',
                'techStack': ['Python', 'PHP', 'JavaScript'],
                'level': 'Full'
            },
            {
                'name':'Thiago Navarro',
                'techStack': ['Ruby', 'C', 'Delphi'],
                'level': 'Full'
            },
        ]


class AllDevs(Resource):
    def __init__(self):
        self.devs = devs

    def get(self):
        try:
            return jsonify(self.devs)
        except Exception as e:
            return e          

    def post(self):
        try:
            self.devs.append(json.loads(request.data))
        except Exception as e:
            return e  
        return jsonify(self.devs)

    def delete(self):
        try:
            self.devs.clear()
        except Exception as e:
            return e  
        return jsonify(self.devs)


class Developer(Resource):
    def __init__(self):
        self.devs = devs

    def get(self, id):
        try:
            return jsonify(self.devs[id])
        except Exception as e:
            return e          


api.add_resource(AllDevs, f'/api/v{version}/devs/')
api.add_resource(Developer, f'/api/v{version}/dev/<id>')

if __name__ == '__main__':
    app.run(debug=True)