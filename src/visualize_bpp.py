import argparse
import pandas
from matplotlib import pyplot

from extract_quality import extract_convert_quality
from color_mapping import effort_color_mapping

parser = argparse.ArgumentParser(description="Plots and shows the BPP according to quality for each effort.")
parser.add_argument("results", help="The CSV results to plot. Must be in the benchmark_xl format.")

args = parser.parse_args()

frame = pandas.read_csv(args.results)

# Convert distance to quality
frame["quality"] = frame["method"].apply(extract_convert_quality)

# Extract effort
frame["effort"] = frame["method"].apply(lambda m: m.split(":")[1])

# Aggregate results by effort and quality
frame = frame.groupby(["effort", "quality"], as_index=False).mean()

# Plot BPP according to quality for each effort
pyplot.figure()

for effort in effort_color_mapping.keys():
    series = frame.query("effort == @effort")
    x = series["quality"]
    y = series["bpp"]

    pyplot.scatter(x, y, edgecolors=effort_color_mapping[effort], facecolors="none", label=effort)

#pyplot.semilogy() # For log scale

pyplot.title("Bits per pixel according to quality factor for each effort", wrap = True)
pyplot.xlabel("Quality factor")
pyplot.ylabel("Bits per pixel")
pyplot.legend()
pyplot.show()
