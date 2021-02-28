from flask import Flask
from flask_cors import CORS

from src.apis.medicaments import medicaments_api
from src.apis.docs import docs_api

VERSION = '/v0.0.1'

app = Flask(__name__)
app.register_blueprint(medicaments_api, url_prefix=VERSION)
app.register_blueprint(docs_api, url_prefix=VERSION)
CORS(app)

if __name__ == '__main__':
    app.run('127.0.0.1', 5000)