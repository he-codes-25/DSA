import pandas as pd

def pivotTable(df: pd.DataFrame) -> pd.DataFrame:
    df=df.pivot(index='month',columns='city',values='temperature')
    return df