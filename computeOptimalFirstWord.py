from utils import *
from timeit import default_timer as timer

if __name__ == "__main__":
    wordBank = getWordBank()
    start = timer()
    optimalFirstWord = findBestWord(wordBank, wordBank)
    end = timer()

    print("Optimal First Word:  ", optimalFirstWord)
    print("Time elapsed:  ", end - start, " seconds")
