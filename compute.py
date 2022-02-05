from typing import List, Dict
from enum import Enum
from collections import defaultdict
from dataclasses import dataclass

class Color(Enum):
    GRAY   = 0
    YELLOW = 1
    GREEN  = 2

class Word(defaultdict):
    def __init__(self, s: str):
        super().__init__(lambda:set())
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
    output.sort(key=lambda x: x[0])
    return output

def filterFromInput() -> Filter:
    print("Enter lowerspaced colors with spaces in between: ", end='')
    i = input().split(" ")
    if len(i) != 5:
        print("entier 5 colors separated with spaces")
        return None
    strToEnum = {"green":Color.GREEN, "gray":Color.GRAY, "yellow":Color.YELLOW}
    enums = []
    for c in i:
        if c not in strToEnum:
            print(c, "not in ", strToEnum.keys())
            return None
        enums.append(strToEnum[c])
    return Filter(*enums)

with open("sgb-words.txt") as f:
    wordBank = [Word(s) for s in sorted(f.read().splitlines())]

# assert Filter.compute(Word("oooll"), Word("llool")) == Filter(Color.YELLOW,Color.GRAY,Color.GREEN,Color.YELLOW,Color.GREEN)

# Generated from findBestWord(wordBank, wordBank)[0][1], cached here since it takes a while. Need to rerun for new wordbank
optimalFirstWord = Word("aloes")

if __name__ == "__main__":
    secretSpace = wordBank
    query = optimalFirstWord
    filt = None
    while len(secretSpace) > 1:
        print("Next Word To Try:", query)
        filterToSecretSpace = compute(query, secretSpace)
        while(not filt):
            filt = filterFromInput()
        secretSpace = filterToSecretSpace[filt]
        filt = None
        query = findBestWord(wordBank, secretSpace)[0][1]
        
    print("Found:", secretSpace[0])
