from utils import *
from timeit import default_timer as timer

if __name__ == "__main__":
    queries = getWordBank("queries.txt")
    solutions = getWordBank("solutions.txt")
    start = timer()
    optimalFirstWord = findBestWord(queries, solutions)
    end = timer()

    print("Optimal First Word:  ", optimalFirstWord)
    print("Time elapsed:  ", end - start, " seconds")
