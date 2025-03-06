import sys


data = list(map(str.strip, sys.stdin))

data = list(map(lambda x: x.split(), data))

data = data[:len(data) // 3 * 3]


while data:
    res = data[0] + data[1] + data[2]
    data = data[3:]
    res.sort(key=len)
    maxx = len(max(res, key=len))
    res = filter(lambda x: len(x) == maxx, res[::-1])
    print(": ".join(list(set(res))).lower())
