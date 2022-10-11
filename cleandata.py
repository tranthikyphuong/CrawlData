import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from collections import Counter
# Opening JSON file
jsonObj = pd.read_json(path_or_buf='C:/Users/ttkph/Documents/cslt/data_NCKH/springer-v1-train.jsonl', lines=True)
journal = jsonObj['journal']
count = Counter(journal)
df = pd.DataFrame({'journal':count.keys(),'amount':count.values()})
#df.to_csv('C:/Users/ttkph/Desktop/amount_crawl(1).csv', index=False, encoding='utf-8')
# print(df.sort_values(by=['amount'], ascending=False).head()) #sap xep giam dan
amount_min = df[df['amount'] < 5000]
dt = pd.DataFrame({'journal':amount_min['journal'],'journal < 5000':amount_min['amount']})
# dt.to_csv('C:/Users/ttkph/Desktop/amount_crawl.csv', index=False, encoding='utf-8')
df.plot(color = 'lightpink')
plt.title('Springer-v1-train')
plt.ylabel('Sum')
plt.xlabel('journal')
plt.show()
