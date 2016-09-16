def bars(line):
    count = 0
    for c in line:
        if c == '|':
            count += 1
    return count


def data(file):
    return [(i, bars(line)) for (i, line) in enumerate(file)]


with open('11.dprint') as f:
    data11 = data(f)


with open('47.dprint') as f:
    data47 = data(f)


import matplotlib.pyplot as plt

x11, y11 = zip(*data11)

x47, y47 = zip(*data47)

plt.plot(x11, y11)
plt.plot(x47, y47)

plt.show()