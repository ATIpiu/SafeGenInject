import numpy as np
import pandas as pd

# 读取CSV文件
tasks_df = pd.read_csv("09241445 247 217.csv")
tasks_df2 = pd.read_csv("test_en.csv")

# 存储修改后的英文提示
translated_prompts = []
no=np.array([6, 12, 14, 16, 40, 48, 49,53, 64, 68, 96])+1
# 遍历前100条数据
for i in range(100):
    task_id = tasks_df2.iloc[i]['task_id']

    # 如果task_id不在指定列表中，使用tasks_df2的英文提示
    if task_id not in no:
        translated_prompts.append(tasks_df2.iloc[i]['prompt_en'])
    else:
        # 否则使用tasks_df中的英文提示
        translated_prompts.append(tasks_df.iloc[i]['prompt_en'])

# 更新tasks_df的列
tasks_df['prompt_zh'] = "测试"
tasks_df['prompt_en'] = translated_prompts

# 保存到新的CSV文件
tasks_df.to_csv("test_en1.csv", index=False)
