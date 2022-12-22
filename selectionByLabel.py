# Selection by label
# See more in Selection by Label using DataFrame.loc()
# or DataFrame.at().
import numpy as np 
import pandas as pd
df = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo"
    }
)
print(df)
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[3:5, 0:2])
print(df.iloc[1, 1])
print(df.iat[1, 1])
s1 = pd.Series([1, 2, 3, 4, 5, 6], index  = pd.date_range("20130102", periods=6))
print(s1)
