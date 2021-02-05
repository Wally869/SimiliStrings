# SimiliStrings
Naïve Distance Computation of word distances using n-gram 

WIP: I hardcoded a tri-gram, and I might get rid of my Parameters class altogether 


Usage:  
Use the CheckDistance function in main to compare words
```python
CheckDistance(word1: str, word2: str, parameters: Parameters = DEFAULT_PARAMETERS)    

``` 

You can also call it directly from cmd
```bash
usage: main.py [-h] word1 word2

> python main.py Alice Elise  
0.5
```  

