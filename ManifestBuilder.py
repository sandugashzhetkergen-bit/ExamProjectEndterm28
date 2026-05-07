import os
import json
class ManifestBuilder:
    def __init__(self):
        self.files = ["fig1.png", "fig2.png", "fig3.png"]

    def build(self):
        result = []

        for f in self.files:
            if os.path.exists(f):
                result.append({
                    "name": f,
                    "size": os.path.getsize(f)
                })

        with open("manifest.json", "w") as file:
            json.dump(result, file, indent=4)
        return result