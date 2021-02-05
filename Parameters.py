from typing import List


class Parameters(object):
    WindowSize: int = 3
    Scores: List[float] = None
    @classmethod
    def FromScores(cls, scores: List[float]):
        if len(scores) % 2 != 1:
            raise ValueError("Parameters.FromScore - Length of Scores must be odd.")
        params = Parameters() 
        params.Scores = scores
        params.WindowSize = len(scores)
        return params


DEFAULT_PARAMETERS = Parameters.FromScores([0.5, 1.0, 0.5]) 
