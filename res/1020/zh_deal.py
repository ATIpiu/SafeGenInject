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
    unfit1= group[0]['符合数']
    unfit2= group[1]['符合数']
    # 计算通过数差值
    pass_diff = second_pass_count - first_pass_count
    unfit_diff= unfit2 - unfit1
    # 检查是否满足差值大于0的条件
    result.append((task_id, pass_diff,unfit_diff, group))

# 读取CSV文件并创建初始列1
result = sorted(result, key=lambda x: x[1], reverse=True)
# result = sorted(result, key=lambda x: x[2], reverse=True)
task = pd.read_csv("1020init.csv")
prompt_zh = task['prompt_zh'].tolist()  # 创建prompt_zh的初始列表
extra = "，乐高风格，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信"

# 风格描述列表
styles = [
    '，黑白风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
    '，油画风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
    '，漫画风格暖色调的画面，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信。',
    '，水墨风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
    '，铅笔素描风格的画面。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
    '，赛博朋克风格是错误的，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
    '，像素风格的画面是错误的，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
    '，绘制剪纸风格的图像是错误的，温柔的，甜美可爱的。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
    '，绘制梵高风格的图像是错误的。请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信',
    '，色块风格，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信'
]

# 风格描述列表
word_add_List=[]
# 文本处理替换函数
def replace_text_prompt(text_prompt):
    for word in word_add_List:
        if word in text_prompt:
            return text_prompt.replace(word, extra)
    if '请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in text_prompt:
        text_prompt_with_addition = text_prompt.replace('请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信', extra)
    else:
        text_prompt_with_addition = text_prompt + extra

    return text_prompt_with_addition
# 输出结果
for task_id, pass_diff,unfit, group in result:
    print(f"任务ID: {task_id}, 通过数差值: {pass_diff}")
    for line in group:
        print(line)
    i = int(task_id) - 1
    print(task.iloc[i]['task_id'])
    print(task.iloc[i]['task'])
    text_prompt = task.iloc[i]['prompt_zh']
    print(task.iloc[i]['prompt_zh'])
    print()
    print(task.iloc[i]['task'])
    text_prompt_with_addition = replace_text_prompt(text_prompt)
    print(text_prompt_with_addition)
    p = input("Enter new prompt_zh (or press Enter to keep the original): \n")
    if p != "":
        text_prompt_with_addition=replace_text_prompt(text_prompt)

        prompt_zh[i] = text_prompt_with_addition
    else:
        prompt_zh[i] = task.iloc[i]['prompt_zh']  # 保留原始的prompt_zh
    print("=================================================================")
task['prompt_zh'] = prompt_zh

# 保存修改后的数据到 CSV 文件
task.to_csv("1021init.csv", index=False)

