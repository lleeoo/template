"Minimal access methods for Athena"
#%%
import pandas as pd

#%%
def a_function(df: pd.DataFrame, col:str) -> float:
    "return mean of a column from df"
    return df[col].mean()
