import pandas as pd
import json

# Opening JSON file
jsonObj = pd.read_json(path_or_buf='C:/Users/ttkph/Documents/cslt/data_NCKH/cs-train.jsonl', lines=True)
journal = jsonObj['journal']
print(journal.head(1)) #in ra 5 hang dau tien
#jsonObj.columns  # in ten cac cot
# # displaying data
# df.to_csv('C:/Users/ttkph/Desktop/dataclean.csv', index=False, encoding='utf-8')