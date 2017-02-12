#!/usr/bin/env python3

import sys

def main():
    lines = tuple(map(lambda x: x.strip(), sys.stdin.readlines()))
    direction, ncols = map(int, lines[0].split(' '))
    nrows = len(lines) - 1 - ncols
    rows = []
    bounds = []
    cols = []
    rhs = []

    for i in range(ncols):
        low, high = lines[i + 1].split(' ')
        use_int = '.' not in low and '.' not in high
        if low == "-INF" and high == "INF":
            bounds.append(("FR", i, None))
        elif low == high:
            bounds.append(("FX", i, (int if use_int else float)(low)))
        elif low == "0" and high == "1":
            bounds.append(("BV", i, None))
        else:
            if low == "-INF":
                bounds.append(("MI", i, None))
            else:
                if use_int:
                    bounds.append(("LI", i, int(low)))
                else:
                    bounds.append(("LO", i, float(low)))
            if high == "INF":
                bounds.append(("PL", i, None))
            else:
                if use_int:
                    bounds.append(("UI", i, int(high)))
                else:
                    bounds.append(("HI", i, float(high)))

    row_splits = list(map(lambda x: x.split(' '), lines[ncols + 1:]))

    for i in range(nrows):
        array = row_splits[i]
        rows.append((array[-2], i))
        if array[-2] != "N":
            rhs.append((i, float(array[-1])))

    for i in range(ncols):
        for j in range(nrows):
            array = row_splits[j][:-2]
            elem = array[i]
            if elem != "0":
                cols.append((i, j, float(elem)))

    s = "NAME ILP\nROWS\n"
    for row in rows:
        s += " " + row[0] + " R" + str(row[1]) + "\n"
    s += "COLUMNS\n"
    for col in cols:
        s += " X" + str(col[0]) + " R" + str(col[1]) + " " + str(col[2]) + "\n"
    s += "RHS\n"
    for r in rhs:
        s += " RHS1 R" + str(r[0]) + " " + str(r[1]) + "\n"
    s += "BOUNDS\n"
    for b in bounds:
        s += " " + b[0] + " BND1 X" + str(b[1])
        if b[2] is not None:
            s += " " + str(b[2])
        s += "\n"
    s += "ENDATA"
    print(s)

if __name__ == "__main__":
    main()
