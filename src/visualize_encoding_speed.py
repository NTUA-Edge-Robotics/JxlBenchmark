import pandas
from matplotlib import pyplot

frame = pandas.read_csv("2022_06_21.csv")

color_mapping = {"lightning": "C0", "thunder": "C1", "falcon": "C2", "cheetah": "C3", "hare": "C4", "wombat": "C5", "squirrel": "C6", "kitten": "C7"}

# Extract quality
def extract_quality(method:str):
    mapping = {"0": 100, "1":90, "1.9":80, "2.8":70, "3.7": 60, "4.6":50, "5.5":40}

    distance = method.split(":")[2][1:]

    return mapping[distance]

frame["quality"] = frame["method"].apply(extract_quality)

# Extract effort
frame["effort"] = frame["method"].apply(lambda m: m.split(":")[1])

# Aggregate results by effort and quality
frame = frame.groupby(["effort", "quality"], as_index=False).mean()

# Plot BPP according to quality for each effort
pyplot.figure()

for effort in color_mapping.keys():
    series = frame.query("effort == @effort")
    x = series["quality"]
    y = series["enc_speed"]

    pyplot.scatter(x, y, edgecolors=color_mapping[effort], facecolors="none", label=effort)

pyplot.title("Encoding speed according to quality factor for each effort", wrap = True)
pyplot.xlabel("Quality factor")
pyplot.ylabel("Encoding speed (megapixels per second)")
pyplot.legend()
pyplot.show()
