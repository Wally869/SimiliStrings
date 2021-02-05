from Parameters import Parameters, DEFAULT_PARAMETERS  


def CheckDistance(word1: str, word2: str, parameters: Parameters = DEFAULT_PARAMETERS):
    word1 = word1.lower()
    word2 = word2.lower()
    # Start by checking word lengths?
    # check which is smallest
    if (len(word1) > len(word2)):
        # swap if needed
        word1, word2 = word2, word1
    # I'll assume windows of size 3 for quick writeup
    # will I need to use padding?
    scores = [0]
    for i in range(1, len(word1) - 1): 
        temp = [0]  # padding temp with 0 to ensure no error with max
        deltas = [-1, 0, 1]
        for idDelta in range(len(deltas)):
            currId = i + deltas[idDelta]
            # check if still in word 2
            if currId >= len(word2):
                break
            if word1[i] == word2[currId]:
                temp.append(parameters.Scores[idDelta])
        scores.append(max(temp))
    return sum(scores)/len(scores)   #len(word2)   # for lower scores?



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("word1")
    parser.add_argument("word2")
    args = parser.parse_args()
    print(CheckDistance(args.word1, args.word2))



