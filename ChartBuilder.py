import pandas as pd
import matplotlib.pyplot as plt
class ChartBuilder:
    def __init__(self, path):
        self.path = path
        self.data = None

    def load(self):
        self.data = pd.read_csv(self.path)

    def style(self, title, x, y):
        plt.title(title)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.grid()

    def graph1(self):
        col = self.data.select_dtypes(include="number").columns[0]
        plt.figure()
        plt.plot(self.data[col])
        self.style("Graph 1", "Index", col)
        plt.show()

    def graph2(self):
        col = self.data.select_dtypes(include="number").columns[1]
        plt.figure()
        plt.plot(self.data[col])
        self.style("Graph 2", "Index", col)
        plt.show()

    def graph3(self):
        col = self.data.select_dtypes(include="number").columns[2]
        plt.figure()
        plt.plot(self.data[col])
        self.style("Graph 3", "Index", col)
        plt.show()