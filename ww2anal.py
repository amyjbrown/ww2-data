# Test to check year of game coming
import statistics
from pprint import pprint


def strip(text):
    try:
        n = text.split(")")[0]  # get only final data
        z = n.split("(")
        # print(z)
        return z[0], int(z[1])
    except:
        return False

with open("ww2.txt", mode="r") as f:
    raw_data = f.read().split("\n")
    # pprint(data)
    data = [tuple(strip(p)) for p in raw_data if strip(p)]
    # pprint(data)
    data.sort(key = lambda d : int(d[1]))
    # pprint(data)
    # open("sorted.py", mode="w+")
    years = [d[1] for d in data]
    mean = statistics.mean(years)
    # mode = statistics.mode(years)
    std = statistics.pstdev(years)
    print(mean,  std)
    by_year = {}
    for t, d in data:
        if d in by_year:
            by_year[d].append(t)
        else:
            by_year[d] = [t,]
    # pprint(by_year)
    for y in by_year:
        print(y, ":", "X" * len(by_year[y]))
