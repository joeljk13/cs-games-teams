#!/usr/bin/env pypy

import random
from pprint import pprint
import itertools

def main():
    people = [
        "Antonio",
        "Ben",
        "Brandon",
        "Colin",
        "Dan",
        "Gayeon",
        "Grace",
        "Hassler",
        "Jack",
        "Jackson",
        "Jacob",
        "Joel",
        "Johnny",
        "Lia",
        "Maria",
        "Mikayla",
        "Nathan",
        "Ned",
        "Shir",
        "Zach"
    ]

    comps = {
        'AI': ['Nathan', 'Antonio', 'Brandon', 'Hassler', 'Shir', 'Jack'],
        'RE': ['Grace', 'Colin', 'Joel', 'Dan'],
        'SE': ['Johnny', 'Gayeon', 'Zach', 'Maria', 'Lia', 'Jackson'],
        'CSEC': ['Jacob', 'Dan', 'Colin', 'Grace'],
        'Extreme': ['Mikayla', 'Zach', 'Gayeon', 'Lia'],
        'Relay': ['Hassler', 'Jack', 'Zach', 'Johnny', 'Ben', 'Ned'],
        'Security': ['Grace', 'Colin', 'Dan', 'Antonio'],
        'Theoretical': ['Shir', 'Jackson', 'Maria', 'Mikayla'],
        'Sport': ['Maria', 'Grace', 'Johnny', 'Hassler'],
        'Web': ['Brandon', 'Gayeon', 'Nathan', 'Jack'],
        'OS': ['Jacob', 'Joel', 'Ned', 'Ben'],
        'Debugging': ['Joel', 'Ben', 'Jack', 'Ned'],
        'Mobile': ['Lia', 'Mikayla', 'Gayeon', 'Nathan'],
        'Gaming': ['Jacob', 'Colin', 'Johnny', 'Jackson']
    }

    for person in people:
        s = ""
        c = 0
        for x in comps.keys():
            if person in comps[x]:
                s += " " + x
                c += 1
        print person + " " + str(c + (person in comps['AI'])) + s

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
