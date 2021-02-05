from Parameters import Parameters, DEFAULT_PARAMETERS  


def CheckDistance(word1: str, word2: str, parameters: Parameters = DEFAULT_PARAMETERS):
    # put everything to lowercase
    word1 = word1.lower()
    word2 = word2.lower()

    # check which is smallest
    if (len(word1) > len(word2)):
        # swap if needed to get shortest first
        word1, word2 = word2, word1
    
    # compute deltas from window size
    idMiddle = parameters.WindowSize // 2 + 1
    deltas = [i - idMiddle + 1 for i in range(parameters.WindowSize)]

    scores = []
    # iterate on words letters
    for idLetterWord1 in range(len(word1)):
        tempScores = []
        for idDelta in range(len(deltas)):
            idLetterWord2 = idLetterWord1 + deltas[idDelta]
            if idLetterWord2 < 0 or idLetterWord2 >= len(word1):
                continue
            if word1[idLetterWord1] == word2[idLetterWord2]:
                tempScores.append(parameters.Scores[idDelta])
            else:
                tempScores.append(0.0)
        # ensure tempScores not empty
        tempScores.append(0)
        scores.append(max(tempScores))
    if len(scores) == 0:
        scores.append(0)
    return sum(scores) / len(scores)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("word1")
    parser.add_argument("word2")
    args = parser.parse_args()
    print(CheckDistance(args.word1, args.word2))



