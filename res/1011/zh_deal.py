import pandas as pd
import ast
from collections import defaultdict

# 读取txt文件
with open('result/zh_results.txt', 'r', encoding='utf-8') as file:
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

result = sorted(result, key=lambda x: x[1], reverse=True)
task = pd.read_csv("2 1011.csv")
prompt_zh = task['prompt_zh'].tolist()  # 创建prompt_zh的初始列 表

# 输出结果
for task_id, pass_diff, group in result:
    print(f"任务ID: {task_id}, 通过数差值: {pass_diff}")
    for line in group:
        print(line)
    i=int(task_id)-1
    print(task.iloc[i]['task_id'])
    print(task.iloc[i]['task'])
    text_prompt=task.iloc[i]['prompt_zh']
    print(task.iloc[i]['prompt_zh'])
    if '照片质感' in task.iloc[i]['prompt_zh']:
        continue
    p = input("Enter new prompt_zh (or press Enter to keep the original): \n")
    if p != "":
        extra = "，水墨风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信"
        # if '照片质感' in text_prompt:
        #     continue
        if '黑白风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in text_prompt:
            text_prompt_with_addition = text_prompt.replace(
                '黑白风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信', extra)
            continue
        elif '油画风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in text_prompt:
            continue
            text_prompt_with_addition = text_prompt.replace(
                '油画风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信', extra)
        elif '请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in text_prompt:
            text_prompt_with_addition = text_prompt.replace('请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信', extra)

        else:
            text_prompt_with_addition = text_prompt + extra
        prompt_zh[i]=text_prompt_with_addition
    else:
        prompt_zh[i] = task.iloc[i]['prompt_zh']  # 保留原始的prompt_zh
    print("=================================================================")
task['prompt_zh'] = prompt_zh

# # 保存修改后的数据到 CSV 文件
task.to_csv("2 1011.csv", index=False)
