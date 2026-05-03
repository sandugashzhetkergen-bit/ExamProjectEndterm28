from flask import Flask

class ApiService14:
    def __init__(self):
        self.app = Flask(__name__)

    def run(self):
        self.app.run(debug=True)