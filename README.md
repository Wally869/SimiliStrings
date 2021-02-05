# SimiliStrings
Naïve Distance Computation of word distances using n-gram 


## How it works  
Input a pair of strings, check if letters are matching at a given index or at neighbouring indices.   
If it is matching, append a score based on distance from letter in the word, then get max for this letter and append to a tracker of scores.  
Finally get the mean of all characters score and return it.  

[I made a small writeup here.](https://www.noveltech.dev/checking-strings-similar-python/)

## Motivation  
I am working on a story generator, and I wanted a quick way to ensure that the names generated for characters are not too close, to avoid potential confusion.  



Usage:  
Use the CheckDistance function in main to compare words
```python
CheckDistance(word1: str, word2: str, parameters: Parameters = DEFAULT_PARAMETERS)    


# Parameters object have the following fields  
class Parameters(object):
    WindowSize: int = 3
    Scores: List[float] = None

# Use the Parameters.FromScores method to generate a Parameters object from a list of score values (floats)
# The list provided must have odd length  
DEFAULT_PARAMETERS = Parameters.FromScores([0.66, 1.0, 0.66]) 


``` 

You can also call it directly from cmd
```bash
> python main.py --help
usage: main.py [-h] word1 word2

> python main.py Alice Elise  
0.6
```  

