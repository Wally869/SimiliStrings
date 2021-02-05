from typing import List


class Parameters(object):
    WindowSize: int = 3
    Scores: List[float] = None
    def __str__(self):
        return f'Parameter(WindowSize={self.WindowSize}, Scores={self.Scores})'
    def __repr__(self):
        return str(self)
    @classmethod
    def FromScores(cls, scores: List[float]):
        if len(scores) % 2 != 1:
            raise ValueError("Parameters.FromScore - Length of Scores must be odd.")
        params = Parameters() 
        params.Scores = scores
        params.WindowSize = len(scores)
        return params
    @classmethod
    def FromWindowSize(windowSize: int, decayFactor: float):
        raise NotImplementedError("Parameters.FromWindowSize - Not Implemented.")  


DEFAULT_PARAMETERS = Parameters.FromScores([0.66, 1.0, 0.66]) 
