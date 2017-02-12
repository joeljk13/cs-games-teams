#!/usr/bin/env python3

# import random
# import pprint
# import itertools

PEOPLE = [
    {
        'name': 'Antonio',
        'ai': 1,
        'relay': 9,
        'SE': 2,
        'extreme': 3,
        'theory': 7,
        'sport': 11,
        'gaming': 10,
        'RE': 6,
        'security': 4,
        'OS': 5,
        'mystery': 8,
        'ALL': 0
    },

    {
        'name': 'Ben',
        'ai': 4,
        'relay': 3,
        'SE': 1,
        'extreme': 2,
        'theory': -1,
        'sport': -1,
        'gaming': 7,
        'RE': 2,
        'security': 6,
        'OS': 1,
        'mystery': -1,
        'ALL': 0
    },

    {
        'name': 'Brandon',
        'ai': 1,
        'relay': 4,
        'SE': 2,
        'extreme': 2,
        'theory': 4,
        'sport': 8,
        'gaming': 8,
        'RE': 16,
        'security': 16,
        'OS': 8,
        'mystery': 6,
        'ALL': 0
    },

    {
        'name': 'Colin',
        'ai': 5,
        'relay': 4,
        'SE': -1,
        'extreme': 3,
        'theory': 2,
        'sport': -1,
        'gaming': 3,
        'RE': 1,
        'security': 1,
        'OS': 1,
        'mystery': 2,
        'ALL': 0
    },

    {
        'name': 'Dan',
        'ai': -1,
        'relay': -1,
        'SE': -1,
        'extreme': 6,
        'theory': 1,
        'sport': 6,
        'gaming': -1,
        'RE': 2,
        'security': 1,
        'OS': -1,
        'mystery': 6,
        'ALL': 0
    },

    {
        'name': 'Gayeon',
        'ai': 3,
        'relay': 1,
        'SE': 3,
        'extreme': 1,
        'theory': -1,
        'sport': 5,
        'gaming': 6,
        'RE': -1,
        'security': -1,
        'OS': -1,
        'mystery': -1,
        'ALL': 0
    },

    {
        'name': 'Grace',
        'ai': 5,
        'relay': 3,
        'SE': 3,
        'extreme': 5,
        'theory': 10,
        'sport': 2,
        'gaming': 5,
        'RE': 1,
        'security': 1,
        'OS': 5,
        'mystery': -1,
        'ALL': 0
    },

    {
        'name': 'Hassler',
        'ai': 2,
        'relay': 1,
        'SE': -1,
        'extreme': 5,
        'theory': 6,
        'sport': 3,
        'gaming': -1,
        'RE': -1,
        'security': -1,
        'OS': 5,
        'mystery': -1,
        'ALL': 0
    },

    {
        'name': 'Jack',
        'ai': 2,
        'relay': 3,
        'SE': 5,
        'extreme': 4,
        'theory': 11,
        'sport': 6,
        'gaming': 10,
        'RE': 7,
        'security': 9,
        'OS': 8,
        'mystery': 1,
        'ALL': 0
    },

    {
        'name': 'Jackson',
        'ai': 2,
        'relay': -1,
        'SE': 4,
        'extreme': 3,
        'theory': 1,
        'sport': -1,
        'gaming': 5,
        'RE': -1,
        'security': -1,
        'OS': -1,
        'mystery': -1,
        'ALL': 0
    },

    {
        'name': 'Jacob',
        'ai': 2,
        'relay': 1,
        'SE': 2,
        'extreme': 2,
        'theory': 1000000,
        'sport': 3,
        'gaming': 2,
        'RE': 4,
        'security': 1,
        'OS': 4,
        'mystery': -1,
        'ALL': 0
    },

    {
        'name': 'Joel',
        'ai': 2,
        'relay': 4,
        'SE': 10,
        'extreme': 5,
        'theory': 5,
        'sport': -1,
        'gaming': -1,
        'RE': 2,
        'security': 2,
        'OS': 2,
        'mystery': -1,
        'ALL': 0
    },

    {
        'name': 'Johnny',
        'ai': 1,
        'relay': 4,
        'SE': 1,
        'extreme': 5,
        'theory': -1,
        'sport': 3,
        'gaming': 3,
        'RE': 20,
        'security': 20,
        'OS': 20,
        'mystery': 6,
        'ALL': 0
    },

    {
        'name': 'Lia',
        'ai': 4,
        'relay': 5,
        'SE': 3,
        'extreme': 1,
        'theory': 2,
        'sport': 6,
        'gaming': -1,
        'RE': -1,
        'security': -1,
        'OS': -1,
        'mystery': -1,
        'ALL': 0
    },

    {
        'name': 'Maria',
        'ai': -1,
        'relay': -1,
        'SE': -1,
        'extreme': 3,
        'theory': 1,
        'sport': 7,
        'gaming': -1,
        'RE': -1,
        'security': 6,
        'OS': 1000000,
        'mystery': 7,
        'ALL': 0
    },

    {
        'name': 'Mikayla',
        'ai': 4,
        'relay': 5,
        'SE': 3,
        'extreme': 1,
        'theory': 2,
        'sport': -1,
        'gaming': 6,
        'RE': -1,
        'security': -1,
        'OS': -1,
        'mystery': -1,
        'ALL': 0
    },

    {
        'name': 'Nathan',
        'ai': 1,
        'relay': 8,
        'SE': 2,
        'extreme': 3,
        'theory': 3,
        'sport': 7,
        'gaming': 7,
        'RE': 5,
        'security': 4,
        'OS': 4,
        'mystery': 1000000,
        'ALL': 0
    },

    {
        'name': 'Ned',
        'ai': 3,
        'relay': 4,
        'SE': 5,
        'extreme': 6,
        'theory': 7,
        'sport': 8,
        'gaming': 9,
        'RE': 2,
        'security': 10,
        'OS': 1,
        'mystery': 11,
        'ALL': 0
    },

    {
        'name': 'Shir',
        'ai': 3,
        'relay': 4,
        'SE': 5,
        'extreme': 2,
        'theory': 1,
        'sport': -1,
        'gaming': -1,
        'RE': -1,
        'security': -1,
        'OS': -1,
        'mystery': 6,
        'ALL': 0
    },

    {
        'name': 'Zach',
        'ai': 6,
        'relay': 2,
        'SE': 7,
        'extreme': 1,
        'theory': 4,
        'sport': -1,
        'gaming': 3,
        'RE': -1,
        'security': -1,
        'OS': -1,
        'mystery': 5,
        'ALL': 0
    }
]

CATEGORIES = [
    {
        'name': 'ai',
        'people': 3,
        'slots': 1,
        'time': 1
    },
    {
        'name': 'relay',
        'people': 3,
        'slots': 1,
        'time': 2
    },
    {
        'name': 'SE',
        'people': 3,
        'slots': 1,
        'time': 3
    },
    {
        'name': 'extreme',
        'people': 2,
        'slots': 1,
        'time': 5
    },
    {
        'name': 'theory',
        'people': 2,
        'slots': 1,
        'time': 3
    },
    {
        'name': 'sport',
        'people': 2,
        'slots': 1,
        'time': 5
    },
    {
        'name': 'gaming',
        'people': 2,
        'slots': 1,
        'time': 4
    },
    {
        'name': 'RE',
        'people': 2,
        'slots': 1,
        'time': 1
    },
    {
        'name': 'security',
        'people': 2,
        'slots': 1,
        'time': 4
    },
    {
        'name': 'OS',
        'people': 2,
        'slots': 1,
        'time': 2
    },
    {
        'name': 'mystery',
        'people': 2,
        'slots': 1,
        'time': 5
    },
    {
        'name': 'ALL',
        'people': 10,
        'slots': 1,
        'time': 0
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
            eq[get_var(p, 0, c)] = 1
            eq[get_var(p, 1, c)] = 1
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
                if c1 == c2 or \
                        CATEGORIES[c1]['time'] != CATEGORIES[c2]['time']:
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
