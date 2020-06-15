from flask import Flask, jsonify, request
from flask_restful import Api, Resource

import logging

app = Flask(__name__)
api = Api(app)

logging.basicConfig(level=logging.INFO)

class Add(Resource):
    def post(self):
        dataDict = request.get_json()
        logging.info(f"data received: {dataDict}")
        #return jsonify(dataDict)
        if ('x' in dataDict) and ('y' in dataDict):       
            x = dataDict["x"]
            y = dataDict["y"]
            retJson = {"message": x+y, 
                         "Status Code": 200}
            return jsonify(retJson)
        else: 
            retJson = {"message": "Error! Cannot find either x or y in JSON Post message", 
                         "Status Code": 301}
            return jsonify(retJson)

api.add_resource(Add, '/add')

@app.route('/')
def hello_world():
    return "Hello World!"
    
@app.route('/apipost', methods=["POST"]) # GET request will fail
def post_api():
    # get x and y 
    dataDict = request.get_json()
    logging.info(f"data received: {dataDict}")
    return "Received Data!", 200
    
@app.route('/ip')
def get_ip():
    return f"Remote address {request.remote_addr}", 200

@app.route('/test')
def get_test():
    return "Success", 200

if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0', port=5000)