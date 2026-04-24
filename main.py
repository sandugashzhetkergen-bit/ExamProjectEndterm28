from ChartBuilder import ChartBuilder
from ReportAnalyzer import ReportAnalyzer
if __name__=="__main__":
    print("Zhetkergen Sandugash")
    ra = ReportAnalyzer("report.csv")
    ra.load()
    result=ra.calc_mean()
    print(result)

from ChartBuilder import ChartBuilder
if __name__ == "__main__":
    print("Zhetkergen Sandugash")
cb = ChartBuilder("report.csv")
cb.load()

cb.graph1()
cb.graph2()
cb.graph3()

from ReportSummary import ReportSummary
if __name__ == "__main__":
    print("Zhetkergen Sandugash")
rs = ReportSummary("report.csv")
rs.load()
summary = rs.get_summary()
print(summary)


