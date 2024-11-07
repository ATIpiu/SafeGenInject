import pandas as pd

task = pd.read_csv("1008init.csv")
task1 = pd.read_csv("287 257.csv")
prompt_en = task1['prompt_en'].tolist()  # 创建prompt_en的初始列 表

# 将 prompt_en 列更新回 task 数据框
task['prompt_en'] = prompt_en

# # 保存修改后的数据到 CSV 文件
task.to_csv("1009init.csv", index=False)