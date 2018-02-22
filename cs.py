#!/usr/bin/env python3

# import random
# import pprint
# import itertools

import math
import sys

PEOPLE = [
{'name': 'Jackson', 'os': 13, 'embedded': 9, 'relay': 5, 'sport': 7, 'ai': 6, 'functional': 10, 'ml': 8, 'security': 15, 'swe': 3, 'theory': 1, 'mirego': 12, 'bell': 11, 'olympus': 4, 'cse-cts': 2, 'ALL': 0},
{'name': 'Gianna', 'os': 8, 'embedded': 9, 'relay': 12, 'sport': 1, 'ai': 7, 'functional': 14, 'ml': 6, 'security': 13, 'swe': 2, 'theory': 3, 'mirego': 10, 'bell': 4, 'olympus': 5, 'cse-cts': 11, 'ALL': 0},
{'name': 'Ben', 'os': 11, 'embedded': 10, 'relay': 3, 'sport': 2, 'ai': 7, 'functional': 14, 'ml': 1, 'security': 13, 'swe': 4, 'theory': 6, 'mirego': 9, 'bell': 5, 'olympus': 8, 'cse-cts': 12, 'ALL': 0},
{'name': 'Brandon', 'os': 13, 'embedded': 14, 'relay': 4, 'sport': 7, 'ai': 2, 'functional': 1, 'ml': 5, 'security': 10, 'swe': 8, 'theory': 3, 'mirego': 12, 'bell': 6, 'olympus': 9, 'cse-cts': 11, 'ALL': 0},
{'name': 'Alan', 'os': 5, 'embedded': 10, 'relay': 14, 'sport': 7, 'ai': 1, 'functional': 6, 'ml': 3, 'security': 12, 'swe': 4, 'theory': 8, 'mirego': 13, 'bell': 9, 'olympus': 2, 'cse-cts': 11, 'ALL': 0},
{'name': 'Nathan', 'os': 11, 'embedded': 13, 'relay': 4, 'sport': 5, 'ai': 9, 'functional': 7, 'ml': 12, 'security': 8, 'swe': 2, 'theory': 14, 'mirego': 1, 'bell': 3, 'olympus': 6, 'cse-cts': 10, 'ALL': 0},
{'name': 'Daniel', 'os': 11, 'embedded': 12, 'relay': 9, 'sport': 5, 'ai': 4, 'functional': 13, 'ml': 10, 'security': 14, 'swe': 1, 'theory': 3, 'mirego': 8, 'bell': 2, 'olympus': 6, 'cse-cts': 7, 'ALL': 0},
{'name': 'Colin', 'os': 5, 'embedded': 7, 'relay': 8, 'sport': 11, 'ai': 10, 'functional': 2, 'ml': 12, 'security': 1, 'swe': 13, 'theory': 6, 'mirego': 14, 'bell': 9, 'olympus': 4, 'cse-cts': 3, 'ALL': 0},
{'name': 'Shir', 'os': 14, 'embedded': 4, 'relay': 5, 'sport': 9, 'ai': 10, 'functional': 3, 'ml': 7, 'security': 12, 'swe': 11, 'theory': 1, 'mirego': 13, 'bell': 8, 'olympus': 6, 'cse-cts': 2, 'ALL': 0},
{'name': 'Xiaoya', 'os': 7, 'embedded': 9, 'relay': 4, 'sport': 14, 'ai': 1, 'functional': 10, 'ml': 5, 'security': 11, 'swe': 2, 'theory': 3, 'mirego': 6, 'bell': 8, 'olympus': 13, 'cse-cts': 12, 'ALL': 0},
{'name': 'Shengbo', 'os': 5, 'embedded': 12, 'relay': 8, 'sport': 14, 'ai': 3, 'functional': 9, 'ml': 2, 'security': 11, 'swe': 1, 'theory': 6, 'mirego': 4, 'bell': 7, 'olympus': 10, 'cse-cts': 13, 'ALL': 0},
{'name': 'Will', 'os': 12, 'embedded': 3, 'relay': 3, 'sport': 5, 'ai': 3, 'functional': 9, 'ml': 4, 'security': 10, 'swe': 4, 'theory': 1, 'mirego': 5, 'bell': 6, 'olympus': 6, 'cse-cts': 6, 'ALL': 0},
{'name': 'Shuyang', 'os': 3, 'embedded': 2, 'relay': 8, 'sport': 14, 'ai': 12, 'functional': 7, 'ml': 11, 'security': 3, 'swe': 5, 'theory': 10, 'mirego': 9, 'bell': 4, 'olympus': 3, 'cse-cts': 6, 'ALL': 0},
{'name': 'Pandrew', 'os': 7, 'embedded': 3, 'relay': 4, 'sport': 13, 'ai': 2, 'functional': 9, 'ml': 1, 'security': 12, 'swe': 5, 'theory': 6, 'mirego': 5, 'bell': 8, 'olympus': 11, 'cse-cts': 10, 'ALL': 0},
{'name': 'Jason', 'os': 13, 'embedded': 14, 'relay': 2, 'sport': 7, 'ai': 9, 'functional': 3, 'ml': 8, 'security': 10, 'swe': 1, 'theory': 12, 'mirego': 11, 'bell': 5, 'olympus': 4, 'cse-cts': 6, 'ALL': 0},
{'name': 'Yutong', 'os': 12, 'embedded': 8, 'relay': 5, 'sport': 14, 'ai': 3, 'functional': 13, 'ml': 1, 'security': 11, 'swe': 4, 'theory': 6, 'mirego': 9, 'bell': 2, 'olympus': 10, 'cse-cts': 7, 'ALL': 0},
{'name': 'Yujie', 'os': 10, 'embedded': 13, 'relay': 12, 'sport': 11, 'ai': 5, 'functional': 4, 'ml': 3, 'security': 15, 'swe': 2, 'theory': 1, 'mirego': 9, 'bell': 6, 'olympus': 7, 'cse-cts': 8, 'ALL': 0},
{'name': 'Zach', 'os': 8, 'embedded': 9, 'relay': 2, 'sport': 6, 'ai': 4, 'functional': 12, 'ml': 10, 'security': 11, 'swe': 3, 'theory': 14, 'mirego': 13, 'bell': 7, 'olympus': 5, 'cse-cts': 1, 'ALL': 0},
{'name': 'Michaela', 'os': 12, 'embedded': 8, 'relay': 5, 'sport': 3, 'ai': 10, 'functional': 9, 'ml': 13, 'security': 14, 'swe': 4, 'theory': 2, 'mirego': 11, 'bell': 1, 'olympus': 6, 'cse-cts': 7, 'ALL': 0},
{'name': 'Joel', 'os': 3, 'embedded': 2, 'relay': 4, 'sport': 10, 'ai': 5, 'functional': 1, 'ml': 10, 'security': 3, 'swe': 14, 'theory': 6, 'mirego': 14, 'bell': 14, 'olympus': 3, 'cse-cts': 5, 'ALL': 0},
]

CATEGORIES = [
    {
        'name': 'os',
        'people': 2,
        'time': [5]
    },
    {
        'name': 'embedded',
        'people': 2,
        'time': [4]
    },
    {
        'name': 'relay',
        'people': 3,
        'time': [3]
    },
    {
        'name': 'sport',
        'people': 2,
        'time': [4]
    },
    {
        'name': 'ai',
        'people': 2,
        'time': [1, 2]
    },
    {
        'name': 'functional',
        'people': 2,
        'time': [4]
    },
    {
        'name': 'ml',
        'people': 2,
        'time': [5]
    },
    {
        'name': 'security',
        'people': 2,
        'time': [5]
    },
    {
        'name': 'swe',
        'people': 3,
        'time': [2, 3]
    },
    {
        'name': 'theory',
        'people': 2,
        'time': [1],
    },
    {
        'name': 'mirego',
        'people': 2,
        'time': [4],
    },
    {
        'name': 'bell',
        'people': 2,
        'time': [2],
    },
    {
        'name': 'olympus',
        'people': 2,
        'time': [1],
    },
    {
        'name': 'cse-cts',
        'people': 2,
        'time': [2, 3],
    },
    {
        'name': 'ALL',
        'people': 10,
        'time': [0],
    }
]

N_PEOPLE = len(PEOPLE)
N_CATEGORIES = len(CATEGORIES)
N_TEAMS = 2

MIN_CATS = 3

# ILP Formation
#
# x_{p, t, c} -- person, team, category
# Binary indicator variables
#
# min SUM_{p, t, c} w_{p, c} * x_{p, t, c}
#
# Each person is on no more than 1 team:
# For each p, c1, c2: x_{p, 0, c1} + x_{p, 1, c2} <= 1
#
# Each person is in at least MIN_CATS categories on at least 1 team:
# For each p: SUM_{c} x_{p, 0, c} + x_{p, 1, c} >= MIN_CATS
#
# Each category has the right number of people from each team:
# For each c, t: SUM_{p} x_{p, t, c} = people_{c}
#
# No person is in 2 categories that are at the same time:
# For each c1, c2, p (with c1, c2 at the same time):
# x_{p, 0, c1} + x_{p, 1, c1} + x_{p, 0, c2} + x{p, 1, c2} <= 1
#
# No person is doing a category they don't want:
# For each p, c (that p doesn't want):
# x_{p, 0, c} = 0
# x_{p, 1, c} = 0

def get_var(person, team, cat):
    return person * N_TEAMS * N_CATEGORIES + team * N_CATEGORIES + cat

def str_eq(eq, rel, rhs):
    return ' '.join(map(str, eq)) + " " + rel + " " + str(rhs) + "\n"

def get_weight(w):
    if w >= 9:
        return -1
    return int(w ** (1.0 / 2) * 100)

def main():
    for w in range(1, 16):
        print(w, get_weight(w), file=sys.stderr)

    vars = []
    for p in range(N_PEOPLE):
        L1 = []
        for t in range(N_TEAMS):
            L2 = []
            for c in range(N_CATEGORIES):
                L2.append(str(get_var(p, t, c)))
            L1.append(L2)
        vars.append(L1)

    N_VARS = N_PEOPLE * N_TEAMS * N_CATEGORIES

    s = "-1 " + str(N_VARS) + "\n"

    for p in range(N_PEOPLE):
        for t in range(N_TEAMS):
            for c in range(N_CATEGORIES):
                w = PEOPLE[p][CATEGORIES[c]['name']]
                if w > 0:
                    w = get_weight(w)
                if w == -1:
                    s += "0 0\n"
                else:
                    s += "0 1\n"

    for p in range(N_PEOPLE):
        for t in range(N_TEAMS):
            for c in range(N_CATEGORIES):
                w = PEOPLE[p][CATEGORIES[c]['name']]
                if w > 0:
                    w = get_weight(w)
                if w < 0:
                    w = 0
                s += str(w) + " "
    s += "N 0\n"

    # For each p, c1, c2: x_{p, 0, c1} + x_{p, 1, c2} <= 1
    for p in range(N_PEOPLE):
        for c1 in range(N_CATEGORIES):
            for c2 in range(N_CATEGORIES):
                eq = [0] * N_VARS
                eq[get_var(p, 0, c1)] = 1
                eq[get_var(p, 1, c2)] = 1
                s += str_eq(eq, "L", 1)

    # For each p: SUM_{c} x_{p, 0, c} + x_{p, 1, c} >= MIN_CATS
    for p in range(N_PEOPLE):
        eq = [0] * N_VARS
        for c in range(N_CATEGORIES):
            eq[get_var(p, 0, c)] = len(CATEGORIES[c]['time'])
            eq[get_var(p, 1, c)] = len(CATEGORIES[c]['time'])
        s += str_eq(eq, "G", MIN_CATS)

    # For each c, t: SUM_{p} x_{p, t, c} = people_{c}
    for c in range(N_CATEGORIES):
        for t in range(N_TEAMS):
            eq = [0] * N_VARS
            for p in range(N_PEOPLE):
                eq[get_var(p, t, c)] = 1
            s += str_eq(eq, "E", CATEGORIES[c]['people'])

    # For each c1, c2, p (with c1, c2 at the same time):
    # x_{p, 0, c1} + x_{p, 1, c1} + x_{p, 0, c2} + x{p, 1, c2} <= 1
    for p in range(N_PEOPLE):
        for c1 in range(N_CATEGORIES):
            for c2 in range(N_CATEGORIES):
                if c1 == c2:
                    continue
                overlap = False
                for a in CATEGORIES[c1]['time']:
                    for b in CATEGORIES[c2]['time']:
                        if a == b:
                            overlap = True
                            break

                if not overlap:
                    continue

                eq = [0] * N_VARS
                eq[get_var(p, 0, c1)] = 1
                eq[get_var(p, 1, c1)] = 1
                eq[get_var(p, 0, c2)] = 1
                eq[get_var(p, 1, c2)] = 1
                s += str_eq(eq, "L", 1)

    print(s[:-1])

if __name__ == "__main__":
    main()
