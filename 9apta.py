# import numpy as np
import pandas as pd
class ReportAnalyzer:
    def __init__(self,path):
        self.path = path
        self.data = None
    def load(self):
        self.data = pd.read_csv(self.path)
    def calc_mean(self):
        cols = self.data.select_dtypes(include="number").columns[:3]
        means={}
        for c in cols:
            means[c] = float(round(self.data[c].mean(), 2))
        return means
if __name__=="__main__":
    print("Zhetkergen Sandugash")
    ra = ReportAnalyzer("report.csv")
    ra.load()
    result=ra.calc_mean()
    print(result)