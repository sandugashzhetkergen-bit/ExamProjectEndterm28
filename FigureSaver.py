import pandas as pd
import matplotlib.pyplot as plt


class FigureSaver:
    def __init__(self, path):
        self.path = path
        self.data = None

    def load(self):
        self.data = pd.read_csv(self.path)

    def save_hist(self):
        col = self.data.select_dtypes(include="number").columns[0]

        plt.figure()
        plt.hist(self.data[col])
        plt.title("Histogram")
        plt.savefig("fig1.png")
        plt.close()

    def save_box(self):
        col = self.data.select_dtypes(include="number").columns[1]

        plt.figure()
        plt.boxplot(self.data[col])
        plt.title("Boxplot")
        plt.savefig("fig2.png")
        plt.close()

    def save_scatter(self):
        cols = self.data.select_dtypes(include="number").columns[:2]

        plt.figure()
        plt.scatter(self.data[cols[0]], self.data[cols[1]])
        plt.title("Scatter")
        plt.savefig("fig3.png")
        plt.close()