import pandas as pd
from collections import Counter
import re

# 读取CSV文件
tasks_df = pd.read_csv("txt2img_risky_tasks_100.csv")

# 获取任务文本列
texts = tasks_df["task"]

# 对文本进行词频统计
word_list = []
for text in texts:
    # 将文本中的单词提取出来，去除标点符号并转换为小写
    words = re.findall(r'\b\w+\b', text.lower())
    word_list.extend(words)

# 统计词频
word_count = Counter(word_list)

# 打印词频统计结果
for word, count in word_count.most_common():
    print(f"{word}: {count}")
