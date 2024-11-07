import pandas as pd

task = pd.read_csv("2 1006.csv")
task1 = pd.read_csv("1004init.csv")
task2 = pd.read_csv("1 1001.csv")
prompt_en = task1['prompt_en'].tolist()  # 创建prompt_en的初始列 表
prompt_en1 = task2['prompt_en'].tolist()  # 创建prompt_en的初始列 表
for i in range(len(prompt_en)):
    if not (str(prompt_en[i])==str(prompt_en1[i])):
        print(prompt_en[i])
        print(prompt_en1[i])
# 将 prompt_en 列更新回 task 数据框
task['prompt_en'] = prompt_en1

# # 保存修改后的数据到 CSV 文件
task.to_csv("1007init.csv", index=False)