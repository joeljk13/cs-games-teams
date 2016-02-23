#!/usr/bin/env pypy

import random
from pprint import pprint
import itertools

def main():
    people = [
        "JK",
        "CW",
        "JA",
        "MJ",
        "DR",
        "ZP",
        "NB",
        "DH",
        "SM",
        "MK",
        "JJ",
        "AS",
        "HT",
        "GM",
        "NC",
        "CP",
        "AC",
        "JD",
        "LK",
        "JB"
    ]

    comps = {
        'alg': ["JA", "DR", "MJ", "ZP"],
        'extreme': ["NB", "DH", "LK", "SM"],
        'ai': ["MK", "JJ", "AS", "HT", "GM", "NC"],
        'web': ["DH", "JD", "ZP", "CW"],
        'os': ["AC", "JK", "JB", "CP"],
        'relay': ["ZP", "HT", "JJ", "NB", "AC", "MJ"],
        'parallel': ["CP", "JK", "JA", "JB"],
        'theory': ["AS", "LK", "DR", "SM"],
        'debug': ["GM", "CP", "JK", "DR"],
        'soft': ["MK", "JA", "SM", "JJ"],
        'mobile': ["NB", "CW", "DH", "NC"],
        # 'sg': ["AS", "CW", "JD", "NC"],
        'rev': ["CW", "JK", "CP", "DR"],
        'comp': ["MJ", "JB", "AC", "LK"]
    }

    for person in people:
        s = ""
        c = 0
        for x in comps.keys():
            if person in comps[x]:
                s += " " + x
                c += 1
        print person + " " + str(c + (person in comps['ai'])) + s

    def test_team(team1):
        team2 = list(set(range(20)) - set(team1))
        team1 = map(lambda x: people[x], team1)
        team2 = map(lambda x: people[x], team2)
        conflicts = 0
        cp = []
        for c in comps.keys():
            players = comps[c]
            conflicts += abs(len([p for p in players if p in team1]) - len(players) / 2)
            if abs(len([p for p in players if p in team1]) - len(players) / 2) != 0:
                cp.append(c)
            # assert len([p for p in players if p in team2]) == len(players) / 2
        team1.sort()
        team2.sort()
        return team1, team2, conflicts, cp

    L = map(lambda x:
        test_team(x), itertools.combinations(range(20), 10))
    L = filter(lambda x: people[0] in x[0], L)
    L.sort(key=lambda x: x[2])
    pprint(list(itertools.takewhile(lambda x: x[2] <= 1, L)))

if __name__ == "__main__":
    main()
