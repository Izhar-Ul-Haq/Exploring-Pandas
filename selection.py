# While standard Python / NumPy expressions for selecting 
# and setting are intuitive and come in handy for interactive 
# work, for production code, we recommend the optimized pandas 
# data access methods, DataFrame.at(), DataFrame.iat(), 
# DataFrame.loc() and DataFrame.iloc().
import pandas as pd
import numpy as np
df = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df)
print(df["A"])
print(df[0:1])
print(df[:])