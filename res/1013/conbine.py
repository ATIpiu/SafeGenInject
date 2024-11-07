import pandas as pd

task1 = pd.read_csv("1 1013.csv")
prompt_en = task1['prompt_en'].tolist()
task2 = pd.read_csv("1013init.csv")
prompt_zh = task2['prompt_zh'].tolist()
task1['prompt_zh']=prompt_zh
task1.to_csv('1014init.csv',index=False)
