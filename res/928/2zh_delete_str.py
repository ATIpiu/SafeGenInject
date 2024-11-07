import numpy as np
import pandas as pd

# 将原输入为：+原输入 以及后缀去掉试试看得分
task = pd.read_csv('928init.csv')
changed_zh = []
for i in range(100):
    task_id = task.iloc[i]['task_id']
    prompt_zh = task.iloc[i]['prompt_zh']
    tasks = task.iloc[i]['task']
    # prompt_zh=prompt_zh.replace("原输入为："+tasks,"")
    prompt_zh=prompt_zh.replace(",请绘制原输入 请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信","。")
    changed_zh.append(prompt_zh)
task['prompt_zh']=changed_zh
task.to_csv('928 2.csv',index=False)
