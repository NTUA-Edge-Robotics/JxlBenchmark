import sys
import re

input = sys.argv[1]

pattern = re.compile(r"Compressed to (?P<size>\d+) bytes \((?P<bpp>\d+\.\d+) bpp\)\.\s+(?P<width>\d+) x (?P<height>\d+), (geomean: ){0,1}(?P<enc_speed>\d+.\d+) MP\/s")
matches = pattern.search(input)

size = int(matches.group("size"))
pixels = int(matches.group("width")) * int(matches.group("height"))
enc_speed = float(matches.group("enc_speed"))
dec_speed = ""
bpp = float(matches.group("bpp"))
dist = ""
psnr = ""
p = ""
bppp = ""
qabpp = ""

print(size, pixels, enc_speed, dec_speed, bpp, dist, psnr, p, bppp, qabpp, sep=",")
