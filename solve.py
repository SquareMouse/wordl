from utils import *


optimalFirstWord = Word("aesir")

if __name__ == "__main__":
    querySpace: List[Word] = getWordBank("queries.txt")
    solutionSpace: List[Word] = getWordBank("solutions.txt")
    query: Word = optimalFirstWord
    filt: Filter = None
    while len(solutionSpace) > 1:
        print("Next Word To Try:", query)
        filterToSolutionSpace = compute(query, solutionSpace)
        while not filt:
            filt = filterFromInput()
        solutionSpace = filterToSolutionSpace[filt]
        filt = None
        query = findBestWord(querySpace, solutionSpace)

    print("Found:", solutionSpace[0])
