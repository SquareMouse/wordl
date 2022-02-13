
from os import linesep
from utils import *
from timeit import default_timer as timer

solvedFilter: Filter = Filter(Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN, Color.GREEN)

def enumerateOutput(queries, solutions: Dict[str,List[str]], filterToSolutionSpace):
    for filt, solutionSpace in filterToSolutionSpace.items():
        if len(solutionSpace) == 1:
            solution = solutionSpace[0]
            solutions[str(solution)].extend([str(filt), str(solution)])
            continue
        query = findBestWord(queries, solutionSpace)
        nextFilterToSolutionSpace = compute(query, solutionSpace)
        for s in solutionSpace:
            solutions[str(s)].extend([str(filt), str(query)])
        enumerateOutput(queries, solutions, nextFilterToSolutionSpace)
    
optimalFirstWord = Word("aesir")

if __name__ == "__main__":
    # solution, numTries, path...
    querySpace: List[Word] = getWordBank("queries.txt")
    solutionSpace: List[Word] = getWordBank("solutions.txt")
    solutions = {str(w):[optimalFirstWord] for w in solutionSpace}

    start = timer()
    enumerateOutput(querySpace, solutions, compute(optimalFirstWord, solutionSpace))
    end = timer()

    print("Time elapsed:  ", end - start, " seconds")
    
    for solution, paths in solutions.items():
        assert solution == paths[-1]

    solutionPaths = sorted(list(solutions.values()))
    with open('solutionMap.txt', 'w') as f:
        f.write(linesep.join([' '.join(map(str, row)) for row in solutionPaths]))
        f.write(linesep)
