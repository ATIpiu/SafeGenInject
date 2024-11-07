
# generate one image
# It is wrong for
import matplotlib.pyplot as plt
import pandas as pd
import time
task =pd.read_csv("1929.csv")
prompt_en = task['prompt_en'].copy()  # 使用 copy()，以防止潜在的视图问题
for i in range(33,100):
    text_prompt=task.iloc[i]['prompt_en']
    print(i)
    print(text_prompt)
    print(task.iloc[i]['task'])
    prompt_en_i=input(':')
    prompt_en.iloc[i] = prompt_en_i

    # 将修改后的 prompt_en 列赋值给新的列 prompt_zh
    task['prompt_en'] = prompt_en
    print(text_prompt)
    print("================================"*10)
    # 保存修改后的数据框为新的 CSV 文件
    task.to_csv("1929.csv", index=False)