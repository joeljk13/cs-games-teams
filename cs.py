#!/usr/bin/env python3

# import random
# import pprint
# import itertools

PEOPLE = [
{'name': 'Antonio', 'ai': 1, 'RE': 6, 'SE': 2, 'CSEC': 1000, 'extreme': 3, 'relay': 9, 'security': 4, 'theory': 4, 'sport': 7, 'web': 11, 'os': 1000, 'debugging': 5, 'mobile': 1000, 'gaming': 1000, 'mystery': 10, 'ALL': 0},
{'name': 'Ben', 'ai': 4, 'RE': 2, 'SE': 2, 'CSEC': 1000, 'extreme': 2, 'relay': 4, 'security': 6, 'theory': 6, 'sport': 1000, 'web': 1000, 'os': 1000, 'debugging': 1, 'mobile': 1, 'gaming': 1000, 'mystery': 7, 'ALL': 0},
{'name': 'Brandon', 'ai': 1, 'RE': 16, 'SE': 2, 'CSEC': 1000, 'extreme': 2, 'relay': 4, 'security': 16, 'theory': 16, 'sport': 4, 'web': 8, 'os': 1000, 'debugging': 8, 'mobile': 1000, 'gaming': 1000, 'mystery': 8, 'ALL': 0},
{'name': 'Colin', 'ai': 10, 'RE': 2, 'SE': 1000, 'CSEC': 1, 'extreme': 5, 'relay': 8, 'security': 1, 'theory': 1, 'sport': 3, 'web': 1000, 'os': 1000, 'debugging': 3, 'mobile': 4, 'gaming': 1000, 'mystery': 5, 'ALL': 0},
{'name': 'Dan', 'ai': 1000, 'RE': 2, 'SE': 1000, 'CSEC': 4, 'extreme': 6, 'relay': 1000, 'security': 1, 'theory': 1, 'sport': 1, 'web': 6, 'os': 1000, 'debugging': 1000, 'mobile': 1000, 'gaming': 1000, 'mystery': 1000, 'ALL': 0},
{'name': 'Gayeon', 'ai': 5, 'RE': 1000, 'SE': 4, 'CSEC': 1000, 'extreme': 1, 'relay': 2, 'security': 1000, 'theory': 1000, 'sport': 1000, 'web': 2, 'os': 1000, 'debugging': 1000, 'mobile': 6, 'gaming': 6, 'mystery': 6, 'ALL': 0},
{'name': 'Grace', 'ai': 7, 'RE': 1, 'SE': 3, 'CSEC': 2, 'extreme': 5, 'relay': 3, 'security': 1, 'theory': 1, 'sport': 10, 'web': 2, 'os': 6, 'debugging': 5, 'mobile': 5, 'gaming': 6, 'mystery': 5, 'ALL': 0},
{'name': 'Hassler', 'ai': 2, 'RE': 1000, 'SE': 1000, 'CSEC': 1000, 'extreme': 5, 'relay': 1, 'security': 1000, 'theory': 1000, 'sport': 6, 'web': 3, 'os': 1000, 'debugging': 5, 'mobile': 1000, 'gaming': 1000, 'mystery': 1000, 'ALL': 0},
{'name': 'Jack', 'ai': 0, 'RE': 2, 'SE': 9, 'CSEC': 6, 'extreme': 11, 'relay': 4, 'security': 3, 'theory': 3, 'sport': 10, 'web': 13, 'os': 7, 'debugging': 5, 'mobile': 12, 'gaming': 10, 'mystery': 8, 'ALL': 0},
{'name': 'Jackson', 'ai': 2, 'RE': 1000, 'SE': 4, 'CSEC': 1000, 'extreme': 3, 'relay': 1000, 'security': 1000, 'theory': 1000, 'sport': 1, 'web': 1000, 'os': 1000, 'debugging': 1000, 'mobile': 1000, 'gaming': 1000, 'mystery': 5, 'ALL': 0},
{'name': 'Jacob', 'ai': 2, 'RE': 4, 'SE': 2, 'CSEC': 1, 'extreme': 1, 'relay': 1, 'security': 1, 'theory': 1, 'sport': 1000, 'web': 3, 'os': 3, 'debugging': 4, 'mobile': 2, 'gaming': 5, 'mystery': 2, 'ALL': 0},
{'name': 'Joel', 'ai': 2, 'RE': 2, 'SE': 10, 'CSEC': 1000, 'extreme': 5, 'relay': 4, 'security': 2, 'theory': 2, 'sport': 5, 'web': 1000, 'os': 1000, 'debugging': 2, 'mobile': 1000, 'gaming': 1000, 'mystery': 1000, 'ALL': 0},
{'name': 'Johnny', 'ai': 1, 'RE': 20, 'SE': 1, 'CSEC': 1000, 'extreme': 5, 'relay': 4, 'security': 20, 'theory': 20, 'sport': 1000, 'web': 3, 'os': 1000, 'debugging': 20, 'mobile': 1000, 'gaming': 1000, 'mystery': 3, 'ALL': 0},
{'name': 'Lia', 'ai': 5, 'RE': 20, 'SE': 6, 'CSEC': 1000, 'extreme': 1, 'relay': 6, 'security': 1000, 'theory': 1000, 'sport': 5, 'web': 8, 'os': 1000, 'debugging': 1000, 'mobile': 6, 'gaming': 3, 'mystery': 1000, 'ALL': 0},
{'name': 'Maria', 'ai': 1000, 'RE': 1000, 'SE': 1000, 'CSEC': 1000, 'extreme': 3, 'relay': 1000, 'security': 6, 'theory': 6, 'sport': 1, 'web': 7, 'os': 1000, 'debugging': 1000, 'mobile': 1000, 'gaming': 1000, 'mystery': 1000, 'ALL': 0},
{'name': 'Mikayla', 'ai': 5, 'RE': 1000, 'SE': 3, 'CSEC': 1000, 'extreme': 1, 'relay': 6, 'security': 1000, 'theory': 1000, 'sport': 2, 'web': 1000, 'os': 1000, 'debugging': 1000, 'mobile': 1000, 'gaming': 4, 'mystery': 7, 'ALL': 0},
{'name': 'Nathan', 'ai': 1, 'RE': 5, 'SE': 2, 'CSEC': 1000, 'extreme': 3, 'relay': 8, 'security': 4, 'theory': 4, 'sport': 3, 'web': 7, 'os': 1000, 'debugging': 4, 'mobile': 1000, 'gaming': 1000, 'mystery': 7, 'ALL': 0},
{'name': 'Ned', 'ai': 3, 'RE': 2, 'SE': 5, 'CSEC': 1000, 'extreme': 6, 'relay': 4, 'security': 10, 'theory': 10, 'sport': 7, 'web': 8, 'os': 1000, 'debugging': 1, 'mobile': 1000, 'gaming': 1000, 'mystery': 9, 'ALL': 0},
{'name': 'Shir', 'ai': 3, 'RE': 1000, 'SE': 5, 'CSEC': 1000, 'extreme': 2, 'relay': 4, 'security': 1000, 'theory': 1000, 'sport': 1, 'web': 1000, 'os': 1000, 'debugging': 1000, 'mobile': 1000, 'gaming': 1000, 'mystery': 1000, 'ALL': 0},
{'name': 'Zach', 'ai': 6, 'RE': 7, 'SE': 1000, 'CSEC': 1, 'extreme': 2, 'relay': 1000, 'security': 3, 'theory': 3, 'sport': 1000, 'web': 1000, 'os': 1000, 'debugging': 1000, 'mobile': 1000, 'gaming': 4, 'mystery': 5, 'ALL': 0},
]

CATEGORIES = [
    {
        'name': 'ai',
        'people': 3,
        'time': [1, 2]
    },
    {
        'name': 'RE',
        'people': 3,
        'time': [1]
    },
    {
        'name': 'SE',
        'people': 3,
        'time': [1]
    },
    {
        'name': 'CSEC',
        'people': 2,
        'time': [2]
    },
    {
        'name': 'extreme',
        'people': 2,
        'time': [2]
    },
    {
        'name': 'relay',
        'people': 3,
        'time': [3]
    },
    {
        'name': 'security',
        'people': 2,
        'time': [3]
    },
    {
        'name': 'theory',
        'people': 2,
        'time': [3]
    },
    {
        'name': 'sport',
        'people': 3,
        'time': [4]
    },
    {
        'name': 'web',
        'people': 2,
        'time': [4],
    },
    {
        'name': 'os',
        'people': 2,
        'time': [4],
    },
    {
        'name': 'debugging',
        'people': 2,
        'time': [5],
    },
    {
        'name': 'mobile',
        'people': 2,
        'time': [5],
    },
    {
        'name': 'gaming',
        'people': 2,
        'time': [5],
    },
    {
        'name': 'mystery',
        'people': 2,
        'time': [6],
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

MIN_CATS = 2

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
    if w == 1:
        return 1
    if w >= 10:
        return -1
    return w + 1

def main():
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
                cont = False
                for a in CATEGORIES[c1]['time']:
                    for b in CATEGORIES[c2]['time']:
                        if a == b:
                            cont = True

                if cont:
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
