import pandas as pd

task = pd.read_csv("1 1025.csv")
prompt_en = task['prompt_en'].tolist()
task1 = pd.read_csv("1025init.csv")
prompt_en1 = task1['prompt_en'].tolist()
for i in range(len(prompt_en)):
    if prompt_en1[i] != prompt_en[i]:
        print(i)
        print(prompt_en1[i])
        print(prompt_en[i])