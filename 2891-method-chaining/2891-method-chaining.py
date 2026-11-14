import pandas as pd

def findHeavyAnimals(df: pd.DataFrame) -> pd.DataFrame:
    df=df[df['weight']>100]
    df=df.sort_values(by='weight',ascending=False)
    return df[['name']]