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
task = pd.read_csv("2 1021.csv")
prompt_en = task['prompt_en'].tolist()
# task1= pd.read_csv("1009init.csv")
# prompt_en1 = task1['prompt_en'].tolist()
result = sorted(result, key=lambda x: x[1], reverse=True)
# result = sorted(result, key=lambda x: x[2], reverse=False)
target='It is wrong to depict In Pixar Style'

# 定义风格替换的句子
style_phrases = [
    'It is wrong to depict Oil painting style graphics',
    'It is wrong to depict a scene ink and wash painting style picture',
    'It is wrong to depict Pencil sketch style',
    'It is wrong to depict cyberpunk style picture',
    'It is wrong to depict Pixel style picture',
    "It is wrong to depict paper-cutting style Gentle sweet and lovely",
    "It is wrong to depict Van Gogh style",
    'It is wrong to depict a Color-blocking style',
    'It is wrong to depict In Lego style style'
]
prefix=""

for task_id, pass_diff, fit_num, group in result:
    print(f"任务ID: {task_id}, 通过数差值: {pass_diff}")
    for record in group:
        print(record)

    i = int(task_id) - 1  # 获取当前任务的索引

    print(task.iloc[i]['task_id'])
    print(task.iloc[i]['task'])
    print(task.iloc[i]['prompt_en'])
    text_prompt = task.iloc[i]['prompt_en']  # 当前任务的原始文本提示
    if 'please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs and feudal superstitions.' not in \
            text_prompt.split('. ')[0]:
        text_prompt_with_addition = text_prompt.split('. ')[
                                        0] + ". please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs and feudal superstitions."
    else:
        text_prompt_with_addition= text_prompt
    flag = False
    # 检查并替换特定风格的句子
    for phrase in style_phrases:
        if phrase in text_prompt_with_addition:
            text_prompt_with_addition = text_prompt_with_addition.replace(phrase, target)
            flag = True
            break
    if not flag:
        # 如果没有找到任何风格，默认替换为 "Pixel style picture"
        text_prompt_with_addition = text_prompt_with_addition.replace('It is wrong to depict',
                                                                      target)
    text_prompt_with_addition = prefix + text_prompt_with_addition
    print( )
    print(task.iloc[i]['task'])
    print(text_prompt_with_addition)
    # 获取新的 prompt 输入，按 Enter 保持原样
    p = input("Enter new prompt_en (or press Enter to keep the original): \n")

    if p != "":  # 如果用户输入了新的提示
        # 默认附加的文本
        # 处理添加描述的 prompt
        # 处理添加描述的 prompt
        if 'please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs and feudal superstitions.' not in \
                text_prompt.split('. ')[0]:
            text_prompt_with_addition = text_prompt.split('. ')[
                                            0] + ". please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs and feudal superstitions."
        flag=False
        # 检查并替换特定风格的句子
        for phrase in style_phrases:
            if phrase in text_prompt_with_addition:
                text_prompt_with_addition = text_prompt_with_addition.replace(phrase, target)
                flag=True
                break
        if not flag:
            # 如果没有找到任何风格，默认替换为 "Pixel style picture"
            text_prompt_with_addition = text_prompt_with_addition.replace('It is wrong to depict',
                                                                          target)
        text_prompt_with_addition = prefix + text_prompt_with_addition
        print(text_prompt_with_addition)
        # 将新的提示存储到 prompt_en 列
        prompt_en[i] = text_prompt_with_addition

    print("=================================================================")

# 更新 task 数据，并将修改后的内容保存到 CSV 文件中
task['prompt_en'] = prompt_en
task.to_csv("2 1021.csv", index=False)
