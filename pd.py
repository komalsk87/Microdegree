# import pandas as pd

# data = [
#     {'name': 'Alice', 'age': 25, 'city': 'New York'},
#     {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
# ]

# df = pd.DataFrame(data)
# print(df)

import pandas as pd
import numpy as np

d = {
    'score1': [90, 80, np.nan, 60],
    'score2': [85, 95, 70, np.nan]
}

df = pd.DataFrame(d)
final = df.isnull()
print(final)