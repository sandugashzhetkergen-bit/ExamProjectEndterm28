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

from ManifestBuilder import ManifestBuilder
print("Zhetkergen Sandugash")
mb = ManifestBuilder()
result = mb.get_file_info()
print(result)
if __name__ == "__main__":
    print("Zhetkergen Sandugash")

#13 апта
from FigureSaver import FigureSaver
print("Zhetkergen Sandugash")

fs = FigureSaver("report.csv")
fs.load()

fs.save_hist()
fs.save_box()
fs.save_scatter()
if __name__ == "__main__":
    print("Zhetkergen Sandugash")
