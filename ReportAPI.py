from flask import Flask, send_file, jsonify, request
from pathlib import Path


class ApiService14:
    def __init__(self):
        self.app = Flask(__name__)
        self.files = ["hist.png", "box.png", "scatter.png"]
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/manifest")
        def manifest():
            return jsonify(self.files)

        @self.app.route("/fig")
        def fig():
            n = int(request.args.get("n", 1))
            filename = self.files[n - 1]

            if not Path(filename).exists():
                return {"error": f"{filename} not found"}, 404

            return send_file(filename, mimetype="image/png")

    def run(self):
        self.app.run(debug=True)