from flask import Flask, jsonify
import json
import pymongo
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


app = Flask(__name__)

@app.route('/sam')
def hello_world():
    print "---"* 20
    print "san=jagsfjka"
    return 'Hello World'

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    print "payload", payload
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'


jwt = JWT(app, authenticate, identity)

@app.route('/alumnae')
@jwt_required()
def protected():
    return '%s' % current_identity

if __name__ == '__main__':
   app.run(debug = True)