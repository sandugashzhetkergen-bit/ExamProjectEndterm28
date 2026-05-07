from flask import Flask, jsonify, send_file, request
import json

class ReportAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.routes()

    def routes(self):

        @self.app.route("/manifest")
        def manifest():
            with open("manifest.json") as f:
                return jsonify(json.load(f))

        @self.app.route("/fig")
        def fig():
            n = request.args.get("n")

            if n == "1":
                return send_file("fig1.png", mimetype="image/png")
            elif n == "2":
                return send_file("fig2.png", mimetype="image/png")
            elif n == "3":
                return send_file("fig3.png", mimetype="image/png")
            else:
                return {"error": "wrong number"}

    def run(self):
        self.app.run(debug=True, port=5001)