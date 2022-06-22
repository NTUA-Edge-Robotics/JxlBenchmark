import pandas
from matplotlib import pyplot

efforts = {"lightning": 0, "thunder": 1, "falcon": 2, "cheetah": 3, "hare": 4, "wombat": 5, "squirrel": 6, "kitten": 7}
frame = pandas.read_csv("2022_06_21.csv")

# Extract effort
frame["effort"] = frame["method"].apply(lambda m: m.split(":")[1])
frame["effort"] = frame["effort"].apply(lambda e: efforts[e])

group = frame.groupby(["effort"], as_index=False).mean()
#error = frame.groupby(["effort"], as_index=False).sem()

group.plot(kind="scatter", x="effort", y="bpp", title="Bits per pixel according to effort", xlabel="Effort", ylabel="Bits per pixel")

#pyplot.errorbar(group["effort"], group["bpp"], yerr = error["bpp"])

pyplot.show()
