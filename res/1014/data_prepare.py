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

# 读取CSV文件
task = pd.read_csv("1014init.csv")
prompt_zh = task['prompt_zh'].tolist()

# 初始化保存结果的列表
final_result = []

# 处理分组后的数据
for task_id, group in data_groups.items():
    if len(group) < 2:
        continue  # 跳过不完整的组

    # 提取每组中的通过数
    first_pass_count = group[0]['通过数']
    second_pass_count = group[1]['通过数']

    # 计算通过数差值
    pass_diff = second_pass_count - first_pass_count

    # 检查是否满足差值大于0的条件
    i = int(task_id) - 1
    text_prompt=task.iloc[i]['prompt_zh']

    extra = "，像素风格的画面是错误的，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信"
    # 风格描述列表
    styles = [
        '，黑白风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
        '，油画风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
        '，漫画风格暖色调的画面，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信。',
        '，水墨风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
        '，铅笔素描风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
        '，赛博朋克风格是错误的，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信'
    ]

    prefix = ''

    # 替换风格描述
    text_prompt_with_addition = text_prompt
    for style in styles:
        if style in text_prompt:
            text_prompt_with_addition = text_prompt.replace(style, extra)
            break

    if '请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in text_prompt and '原输入为：' in text_prompt:
        text_prompt_with_addition = text_prompt.replace('请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信', extra)
        text_prompt_with_addition = text_prompt_with_addition.replace('原输入为：', '原输入为：' + prefix)
    else:
        text_prompt_with_addition = text_prompt + extra
        text_prompt_with_addition = prefix + text_prompt_with_addition
    modified= text_prompt_with_addition
    if group[0]['符合数'] > group[1]['符合数'] and group[0]['通过数'] > group[1]['通过数']:
        chosen = task.iloc[i]['prompt_zh']
        rejected = modified
    elif group[0]['符合数'] < group[1]['符合数'] and group[0]['通过数'] < group[1]['通过数']:
        rejected = task.iloc[i]['prompt_zh']
        chosen = modified
    else:
        continue

    human_input = task.iloc[i]['task']
    final_result.append({
        "instruction": "请针对我的输入帮我修改我的输出，",
        "input": human_input,
        "chosen": chosen,
        "rejected": rejected
    })

# 将结果保存到新的JSON文件
import json
with open('1014.json', 'w', encoding='utf-8') as f:
    json.dump(final_result, f, ensure_ascii=False, indent=2)

print("数据已成功保存到formatted_output.json文件中。")
