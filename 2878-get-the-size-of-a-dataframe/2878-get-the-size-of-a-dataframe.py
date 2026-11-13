import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    t=players.shape
    return [t[0],t[1]]