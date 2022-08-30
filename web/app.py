from http import client
from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

#connect to mongodb
client = MongoClient('localhost', 27017)

db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert_one({
    "num_of_users":0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]["num_of_users"]
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"nums_of_users":new_num}})
        return str("Hello user" + str(new_num))

api.add_resource(Visit, '/visit')

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
        