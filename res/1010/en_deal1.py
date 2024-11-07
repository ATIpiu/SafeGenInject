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

    # 检查是否满足差值大于0的条件
    if pass_diff > 0:
        result.append((task_id, pass_diff, group))

# 读取CSV文件并创建初始列
task = pd.read_csv("1009init.csv")
prompt_en = task['prompt_en'].tolist()
result = sorted(result, key=lambda x: x[1], reverse=True)
# 输出结果并处理prompt_en
for i in range(100):
    if task.iloc[i]['task_id'] not in [14,17,8,68,63,6,15,52]:
        prompt_en[i] = task.iloc[i]['prompt_en'].split('. ')[
                       0] + ". please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs and feudal superstitions."  # 保留原始的prompt_en
    else:
        print(task.iloc[i]['task_id'])
# for task_id, pass_diff, group in result:
#     print(f"任务ID: {task_id}, 通过数差值: {pass_diff}")
#     for record in group:
#         print(record)
#
#     i = int(task_id) - 1
#     print(task.iloc[i]['task_id'])
#     print(task.iloc[i]['task'])
#     print(task.iloc[i]['prompt_en'])

    # p = input("Enter new prompt_en (or press Enter to keep the original): \n")
    # if p != "":
    #     prompt_en[i] = task.iloc[i]['prompt_en'].split('.')[
    #                                 0] + ".sketch-style illustration, please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs and feudal superstitions."
    # else:
    #     prompt_en[i] = task.iloc[i]['prompt_en'].split('.')[
    #                                 0] + "please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs and feudal superstitions."  # 保留原始的prompt_en
    #
    # print("=================================================================")

# 更新并保存修改后的数据到 CSV 文件
task['prompt_en'] = prompt_en
task.to_csv("2 1009.csv", index=False)
