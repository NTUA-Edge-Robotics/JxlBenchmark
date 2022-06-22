import argparse
import pandas
from matplotlib import pyplot

from extract_quality import extract_convert_quality
from color_mapping import effort_color_mapping

parser = argparse.ArgumentParser(description="Plots and shows a field according to quality for each effort.")
parser.add_argument("results", help="The CSV results to plot. Must be in the benchmark_xl format.")
parser.add_argument("metric", help="The CSV metric that will be used for the Y values")
parser.add_argument("-y_label", help="The Y label. Defaults to the field name.")
parser.add_argument("-title", help="The title of the graph. Default to <field> according to quality factor for each effort.")

args = parser.parse_args()

frame = pandas.read_csv(args.results)
metric = args.metric
y_label = args.y_label or metric
title = args.title or f"{metric} according to quality factor for each effort"

# Convert distance to quality
frame["quality"] = frame["method"].apply(extract_convert_quality)

# Extract effort
frame["effort"] = frame["method"].apply(lambda m: m.split(":")[1])

# Aggregate results by effort and quality
frame = frame.groupby(["effort", "quality"], as_index=False).mean()

# Plot field according to quality for each effort
pyplot.figure()

for effort in effort_color_mapping.keys():
    series = frame.query("effort == @effort")
    x = series["quality"]
    y = series[metric]

    pyplot.scatter(x, y, edgecolors=effort_color_mapping[effort], facecolors="none", label=effort)

pyplot.title(title, wrap = True)
pyplot.xlabel("Quality factor")
pyplot.ylabel(y_label)
pyplot.legend()
pyplot.show()
