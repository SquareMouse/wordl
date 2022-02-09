from typing import List, Dict
from enum import Enum
from collections import defaultdict
from dataclasses import dataclass


class Color(Enum):
    GRAY = 0
    YELLOW = 1
    GREEN = 2


class Word(defaultdict):
    def __init__(self, s: str):
        super().__init__(lambda: set())
        for idx, letter in enumerate(s):
            self[letter].add(idx)
        self._data = s

    def __str__(self):
        return self._data

    def __repr__(self):
        return self.__str__()


@dataclass(frozen=True)
class Filter:
    a: Color
    b: Color
    c: Color
    d: Color
    e: Color

    def __hash__(self):
        return int(self.a.value + 3 * self.b.value + 9 * self.c.value + 27 * self.d.value + 81 * self.e.value)

    @classmethod
    def compute(cls, query: Word, secret: Word):
        filter = [Color.GRAY] * 5
        for secretLetter, secretIdxSet in secret.items():
            if secretLetter not in query:
                continue
            queryIdxSet = query[secretLetter]
            greenIdxSet = secretIdxSet.intersection(queryIdxSet)
            for greenIdx in greenIdxSet:
                filter[greenIdx] = Color.GREEN

            numYellow = min(len(secretIdxSet), len(queryIdxSet))  - len(greenIdxSet)
            if numYellow == 0:
                continue
            for yellowIdx in sorted(list(queryIdxSet - greenIdxSet))[:numYellow]:
                filter[yellowIdx] = Color.YELLOW
        return cls(*filter)


def compute(query: Word, secretCandidates: List[Word]) -> Dict[Filter, List[Word]]:
    computed = defaultdict(lambda: [])
    for secret in secretCandidates:
        computed[Filter.compute(query, secret)].append(secret)
    return computed


def findBestWord(queryCandidates, secretCandidates):
    output = []
    for query in queryCandidates:
        d = compute(query, secretCandidates)
        t = (max([len(v) for v in d.values()]), query)
        output.append(t)
    return min(output, key = lambda x: x[0])[1]

def getWordBank(file:str) -> List[Word]:
        with open(file) as f:
            wordBank = [Word(s) for s in sorted(f.read().splitlines())]
        return wordBank


def filterFromInput() -> Filter:
    print("Enter lowercase colors with spaces in between: ", end='')
    i = input().split(" ")
    if len(i) != 5:
        print("Enter 5 colors separated with spaces")
        return None
    strToEnum = {"green": Color.GREEN, "gray": Color.GRAY, "yellow": Color.YELLOW}
    enums = []
    for c in i:
        if c not in strToEnum:
            print(c, "not in ", strToEnum.keys())
            return None
        enums.append(strToEnum[c])
    return Filter(*enums)

