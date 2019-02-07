from flask import Flask

server = Flask(__name__)

@server.route("/")
def home():
    return hello("World")

@server.route("/<name>", methods=['GET'])
def hello(name):
    return ("Hello, %s!" % name)

if __name__ == "__main__":
    server.run(host='0.0.0.0')