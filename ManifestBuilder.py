import os
class ManifestBuilder:
    def __init__(self):
        self.files = ["fig1.png", "fig2.png", "fig3.png"]

    def get_file_info(self):
        result = []

        for f in self.files:
            if os.path.exists(f):
                info = {
                    "name": f,
                    "size": os.path.getsize(f)
                }
                result.append(info)
        return result