import argparse
import pandas
from matplotlib import pyplot, ticker

from extract_quality import extract_convert_quality
from color_mapping import effort_color_mapping

parser = argparse.ArgumentParser(description="Plots and shows the bpp according to the quality factor for each effort.")
parser.add_argument("results", help="The CSV results produced by benchmark_xl.")
parser.add_argument("figure", help="Path and filename of the resulting figure")

args = parser.parse_args()

frame = pandas.read_csv(args.results)

# Convert distance to quality
frame["quality"] = frame["method"].apply(extract_convert_quality)

# Extract effort
frame["effort"] = frame["method"].apply(lambda m: m.split(":")[1])

# Aggregate results by effort and quality
frame = frame.groupby(["effort", "quality"], as_index=False).mean(numeric_only=True)

# Plot bpp according to quality for each effort
pyplot.figure()

for effort in effort_color_mapping.keys():
    series = frame.query("effort == @effort")
    x = series["quality"]
    y = series["bpp"]

    pyplot.scatter(x, y, edgecolors=effort_color_mapping[effort], facecolors="none", label=effort)

pyplot.xlabel("Quality factor")
pyplot.xticks(frame["quality"].unique())
pyplot.ylabel("Bitrate (bits per pixel)")
pyplot.legend()
pyplot.grid(alpha=0.2)

# Log scale
pyplot.yscale("log")
log_locator = ticker.LogLocator(base=2)
pyplot.gca().get_yaxis().set_major_locator(log_locator)
pyplot.gca().get_yaxis().set_major_formatter(ticker.ScalarFormatter())

pyplot.tick_params(axis="both", which="both", labelsize=8)
pyplot.gcf().set_size_inches(3.4, 4)

pyplot.savefig(args.figure, bbox_inches="tight")
