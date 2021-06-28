from flask import Flask, jsonify, make_response
from flask import request
import jwt
import datetime

app = Flask(__name__)

SECRET_KEY = "gjdbjksqad"


@app.route("/login", methods=['GET'])
def login():
    data = "Garima"
    token = jwt.encode({
        'public_id': data,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(1)
    }, SECRET_KEY)
    authenticated = test(token)
    return make_response(jsonify({'token': token, 'authenticated': authenticated}), 201)


def test(token):
    decoced = jwt.decode(token, SECRET_KEY, options={"verify_signature": False})
    date_time = datetime.datetime.utcfromtimestamp(
        int(decoced['exp']))
    if decoced['public_id'] == "Garima" and date_time > datetime.datetime.utcnow():
        return True
    else:
        return False


@app.route("/hello", methods=['POST'])
def hello1():
    data = request.data
    return data


@app.route("/", methods=['GET'])
def hello():
    data = request.args
    return data

# app.add_url_rule('/hello', endpoint=None, view_func=hello1)

if __name__ == "__main__":
    app.run(debug=True)
