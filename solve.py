from utils import *


optimalFirstWord = Word("aloes")

if __name__ == "__main__":
    wordBank = getWordBank()
    secretSpace: List[Word] = wordBank
    query: Word = optimalFirstWord
    filt: Filter = None
    while len(secretSpace) > 1:
        print("Next Word To Try:", query)
        filterToSecretSpace = compute(query, secretSpace)
        while not filt:
            filt = filterFromInput()
        secretSpace = filterToSecretSpace[filt]
        filt = None
        query = findBestWord(wordBank, secretSpace)

    print("Found:", secretSpace[0])
