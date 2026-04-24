import pandas as pd
class ReportSummary:
    def __init__(self, path):
        self.path = path
        self.data = None

    def load(self):
        self.data = pd.read_csv(self.path)

    def get_summary(self):
        result = self.data.describe().to_dict()
        return result
