# 读取txt文件
with open('zh.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 初始化变量
data_groups = []
temp_group = []

# 分组数据，以"===="作为分隔
for line in lines:
    line = line.strip()
    if line.startswith('任务ID'):
        temp_group.append(line)
    elif line == '==========================================================================================================================================================================':
        if temp_group:
            data_groups.append(temp_group)
            temp_group = []

# 处理分组后的数据
result = []
for group in data_groups:
    if len(group) < 2:
        continue  # 跳过不完整的组

    # 提取第一行和第二行的"通过数"
    first_pass_count = int(group[0].split('通过数: ')[1].split(',')[0])
    second_pass_count = int(group[1].split('通过数: ')[1].split(',')[0])

    # 计算通过数差值
    pass_diff = second_pass_count - first_pass_count

    # 检查是否满足差值大于0的条件
    if pass_diff > 0:
        task_id = group[0].split('任务ID: ')[1].split(',')[0]
        result.append((task_id, pass_diff, group))
import pandas as pd
# 按照通过数差值逆序排列
result = sorted(result, key=lambda x: x[1], reverse=True)
task = pd.read_csv("1007init.csv")
prompt_zh = task['prompt_zh'].tolist()  # 创建prompt_zh的初始列 表
# 输出结果
for task_id, pass_diff, group in result:
    print(f"任务ID: {task_id}, 通过数差值: {pass_diff}")
    for line in group:
        print(line)
    i=int(task_id)-1
    print(task.iloc[i]['task_id'])
    print(task.iloc[i]['task'])
    print(task.iloc[i]['prompt_zh'])
    extra = "， 漫画风格暖色调的画面，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信。"
    if '请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in task.iloc[i]['prompt_zh']:
        extra = "，漫画风格暖色调的画面"

    if '照片质感' in task.iloc[i]['prompt_zh']:
        continue
    p = input("Enter new prompt_zh (or press Enter to keep the original): \n")
    if p != "":
        prompt_zh[i] = task.iloc[i]['prompt_zh']+extra
    else:
        prompt_zh[i] = task.iloc[i]['prompt_zh']  # 保留原始的prompt_zh
    print("=================================================================")
task['prompt_zh'] = prompt_zh

# # 保存修改后的数据到 CSV 文件
task.to_csv("2 1007.csv", index=False)
