import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from collections import Counter
    # Opening JSON file
jsonObj = pd.read_json(path_or_buf='C:/Users/ttkph/Documents/cslt/data_NCKH/cs-train.jsonl', lines=True)
journal = jsonObj['journal']
Count = Counter(journal)
df = pd.DataFrame({'amount':Count})
df.plot()
plt.show()
    # print(journal.head(1)) #in ra 5 hang dau tien
    # print(jsonObj.dtypes)

    #jsonObj.columns  # in ten cac cot
    # # displaying data
    # jsonObj.to_csv('C:/Users/ttkph/Desktop/dataclean.csv', index=False, encoding='utf-8')