import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    a=[]
    for i in employees['salary']:
        a.append(i*2)
    employees['salary']=a
    return employees