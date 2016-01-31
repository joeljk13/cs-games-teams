#!/usr/bin/env pypy

import random
from pprint import pprint
import itertools

def main():
    people = [
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
        "JK",
        "LK",
        "JB"
    ]
    comps = {
        'alg': ["JA", "DR", "MJ", "ZP"],
        'extreme': ["NB", "DH", "LK", "SM"],
        'ai': ["MK", "JJ", "AS", "HT", "GM", "NC"],
        'web': ["DH", "JD", "ZP", "CW"],
        'os': ["AC", "JK", "JB", "CP"],
        'relay': ["ZP", "JB", "HT", "JJ", "DH", "NB"],
        'parallel': ["CP", "JK", "JA", "NC"],
        'theory': ["AS", "LK", "DR", "SM"],
        'debug': ["DH", "GM", "CP", "JK"],
        'soft': ["MK", "JA", "NB", "SM"],
        'db': ["MJ", "HT", "AC", "LK"],
        'sg': ["AS", "CW", "JD", "NC"],
        'rev': ["CW", "JK", "CP", "DR"],
        'comp': ["MK", "MJ", "JB", "AC"]
    }
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
        return team1, team2, conflicts, cp
    L = map(lambda x:
        test_team(x), itertools.combinations(range(20), 10))
    L.sort(key=lambda x: x[2])
    pprint(L[:10])

if __name__ == "__main__":
    main()
