# JxlBenchmark

The project aims to visualize the bitrate and encoding speed of [libjxl](https://github.com/libjxl/libjxl) with data following the [benchmark_xl](https://github.com/libjxl/libjxl/blob/main/doc/benchmarking.md) format.

## Installation

1. Install the dependencies with `pip install -r requirements.txt`

## Primary Data Generation

Generate the primary data using `bash src/generate_primary_data.sh <path the images directory>` or using the `benchmark_xl` tool with the `--print_details_csv` option.

> :warning: Please note that `benchmark_xl` yields different results than `cjxl`.

## Bitrate Visualization

The following script will produce a graphic of the bitrate according to the quality factor and effort. The API of the script can be found using `python src/visualize_bpp.py -h`.

## Encoding Speed Visualization

The following script will produce a table of the encoding speed according to the quality factor and effort. The API of the script can be found using `python src/table_enc_speed.py -h`.
