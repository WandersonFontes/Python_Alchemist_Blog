from flask import Flask, jsonify, request
import json

app = Flask(__name__)
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

@app.route('/api/v1/devs', methods=['GET', 'POST', 'DELETE'])
def infoDevs():
    if request.method == 'POST':
        try:
            devs.append(json.loads(request.data))
        except Exception as e:
            return e      
    elif request.method == 'DELETE':
        try:
            devs.clear()
        except Exception as e:
            return e  
    elif request.method == 'GET':
        pass        
    return jsonify(devs)

@app.route('/api/v1/devs/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def infoDevID(id):
    if request.method == 'DELETE':
        # devs.pop(id)
        return jsonify({'status':'REMOVED SUCESSFULY'})
    if request.method == 'GET': 
        pass
    elif request.method == 'PUT':
        data = json.loads(request.data)
        devs[id] = data
    return jsonify(devs[id])


if __name__ == '__main__':
    app.run(debug=True)