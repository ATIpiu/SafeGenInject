import pandas as pd
import ast
from collections import defaultdict

# 读取txt文件
with open('result/en_results.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 按task_id分组数据
data_groups = defaultdict(list)

# 将每行字典格式的数据解析并按task_id分组
for line in lines:
    line = line.strip()
    if line.startswith("{'task_id'"):
        record = ast.literal_eval(line)  # 将字典格式字符串转换为实际字典
        task_id = record['task_id']
        data_groups[task_id].append(record)

# 处理分组后的数据
result = []
for task_id, group in data_groups.items():
    if len(group) < 2:
        continue  # 跳过不完整的组

    # 提取每组中的通过数
    first_pass_count = group[0]['通过数']
    second_pass_count = group[1]['通过数']

    # 计算通过数差值
    pass_diff = second_pass_count - first_pass_count
    fit_num=group[0]['符合数']
    # 检查是否满足差值大于0的条件
    if pass_diff > 0:
        result.append((task_id, pass_diff,fit_num, group))

# 读取CSV文件并创建初始列
task = pd.read_csv("2 1012.csv")
prompt_en = task['prompt_en'].tolist()
task1= pd.read_csv("1009init.csv")
prompt_en1 = task1['prompt_en'].tolist()
result = sorted(result, key=lambda x: x[1], reverse=True)
# result = sorted(result, key=lambda x: x[2], reverse=False)
for task_id, pass_diff,fit_num, group in result:
    print(f"任务ID: {task_id}, 通过数差值: {pass_diff}")
    for record in group:
        print(record)
    i = int(task_id) - 1

    print(task.iloc[i]['task_id'])
    print(task.iloc[i]['task'])
    print(task.iloc[i]['prompt_en'])
    text_prompt=task.iloc[i]['prompt_en']
    p = input("Enter new prompt_en (or press Enter to keep the original): \n")

    if p != "":
        text_prompt_with_addition = text_prompt.split('. ')[
                                        0] + ". please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs and feudal superstitions."
        text_prompt_with_addition = text_prompt_with_addition.replace('It is wrong to depict',
                                                                      "It is wrong to depict Pencil sketch style")
        prompt_en[i] =text_prompt_with_addition
        # prompt_en[i] =prompt_en1[i]
    print("=================================================================")
task['prompt_en'] = prompt_en
task.to_csv("2 1012.csv", index=False)