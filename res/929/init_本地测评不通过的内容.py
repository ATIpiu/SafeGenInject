import re
from collections import Counter

import pandas as pd


def isFit():
    nos = [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
           1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1,
           1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    ids1 = []
    for i in range(0, len(nos)):
        if nos[i] == 0:
            ids1.append(i + 1)
    # print((ids1))
    ids2 = []
    with open("929 本地测试不通过的.txt", encoding="utf-8") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            if i % 5 == 0:
                numbers = re.findall(r'\b\d+\b', lines[i - 1])
                numbers = list(map(int, numbers))
                if numbers[1] == 0:
                    ids2.append(numbers[0])
    # print((ids2))
    nos2 = [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    nos2=[1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1]
    ids3 = []
    for i in range(0, len(nos2)):
        if nos[i] == 0:
            ids3.append(i + 1)
    print((ids3))
    nos3=[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0]
    ids4=[]
    for i in range(0, len(nos3)):
        if nos[i] == 0:
            ids4.append(i + 1)
    print((ids4))
    combined_list = ids1  + ids2

    # 计数每个元素的出现次数
    counter = Counter(combined_list)

    # 筛选出现次数超过两次的元素
    result = [num for num, count in counter.items() if count >= 2]

    print(result)  # [4, 5, 16, 44, 45, 51, 58, 66, 78]
isFit()
task = pd.read_csv('1 929.csv')
prompt_zh=[]
for i in range(100):
    task_id = task.iloc[i]['task_id']
    if task_id in [2, 4, 5, 14, 16, 18, 21, 24, 28, 38, 41, 42, 44, 45, 47, 51, 52, 56, 58, 63, 66, 67, 70, 71, 78, 91, 92, 95, 97]:
        print( task.iloc[i]['prompt_zh'])
        print( task.iloc[i]['task'])
        tem=input()

        prompt_zh.append(tem)
        print("================================"*5)
    else:
        prompt_zh.append(task.iloc[i]['prompt_zh'])

# task['prompt_zh'] = prompt_zh
# task.to_csv('1 929.csv',index=False)