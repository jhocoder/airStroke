from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.routes import setup_routes

app = Flask(__name__)
setup_routes(app)


CORS(app)

if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=3030)