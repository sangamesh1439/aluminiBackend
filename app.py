from flask import Flask, jsonify
import json
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0-yf2bx.mongodb.net/test?retryWrites=true&w=majority")

db  = client.testdb
for college in db.colleges.find():
    print(college)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def getTasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
   app.run(debug = True)