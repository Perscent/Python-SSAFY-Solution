def countX(m, x):
    count = 0
    for ele in m:
        if (ele == x):
            count = count + 1
    return count
n = input()
m = list(map(int, str(n)))
o = []
i = 0
while i < 10:
    o.append(countX(m, i))
    i += 1

print("0 1 2 3 4 5 6 7 8 9\n{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}" .format(*o))

