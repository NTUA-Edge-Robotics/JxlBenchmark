import argparse
import pandas

from extract_quality import extract_convert_quality

parser = argparse.ArgumentParser(description="Prints the encoding speed according to the quality factor and effort.")
parser.add_argument("results", help="The CSV results produced by benchmark_xl.")

args = parser.parse_args()

frame = pandas.read_csv(args.results)

# Convert distance to quality
frame["quality"] = frame["method"].apply(extract_convert_quality)

# Extract effort
frame["effort"] = frame["method"].apply(lambda m: m.split(":")[1])

# Aggregate results by effort and quality
frame = frame.groupby(["effort", "quality"], as_index=False).mean()

print(frame[["effort", "quality", "enc_speed"]])
