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
            files = {"1": "fig1.png", "2": "fig2.png", "3": "fig3.png"}
            if n in files:
                return send_file(files[n], mimetype="image/png")
            return jsonify({"error": "wrong number, use ?n=1, 2 or 3"}), 400

    def run(self, port=5001):
        self.app.run(debug=True, port=port)