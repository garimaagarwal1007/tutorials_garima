from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/hello", methods=['POST'])
def hello1():
    data = request.data
    return data

@app.route("/", methods=['GET'])
def hello():
    data = request.args
    return data

#app.add_url_rule('/hello', endpoint=None, view_func=hello1)

if __name__ == "__main__":
    app.run(debug=True)