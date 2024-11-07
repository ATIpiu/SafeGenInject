import openai
import pandas as pd
import re

from openai import OpenAI

# 初始化 OpenAI 客户端

from util.gpt_batch import *
# 示例数据
def batch_generate(prompt,messages):
    prompts_messages = [
        ( prompt, [messages[i]]) for i in range(len(messages))
    ]
    print(prompts_messages)
    # 生成JSONL内容
    jsonl_content = create_jsonl_file(prompts_messages,model='gpt-4o')
    # 上传文件并获取文件ID
    file_id = upload_jsonl_to_openai(jsonl_content)

    # 创建批处理请求
    batch = create_batch_request(file_id)

    # 检索并保存结果
    output_file_id=retrieve_and_save_results(batch.id)

    get_and_save_file_content(output_file_id,f"expansion.json")

def generate_safe_text(prompt, model="gpt-4o"):
    try:
        response = client.chat.completions.create(
            model=model,  # 确保使用正确的模型名称
            messages=prompt
        )
        # 返回生成的文本
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating safe text: {e}")
        return "Error"

init=pd.read_csv('1025init.csv')
messages=[]
styles = [
    "黑白风格",
    "油画风格",
    "漫画风格（暖色调）",
    "水墨风格",
    "铅笔素描风格",
    "色块风格",
    "乐高风格",
    "炭笔画风格",
    "波普艺术风格",
    "马赛克风格",
    "32-Bit像素艺术",
    "涂鸦艺术"
]

prompt = ("""请对句子进行重新组织使其语句通顺""")
# prompt_style = ("""我现在有一个图像安全检测模型，但下面有一种风格可能使得文生图prompt通过图像安全检测，我需要知道是哪一种然后我需要对我的模型作数据补充。请直接给我答案
# 黑白风格
# 油画风格
# 漫画风格（暖色调）
# 水墨风格
# 铅笔素描风格
# 色块风格
# 乐高风格
# 炭笔画风格
# 波普艺术风格
# 马赛克风格
# 32-Bit像素艺术
# 涂鸦艺术""")
style_list = ['水墨风格', '水墨风格', '抱歉，我无法协助满足该请求。', '水墨风格', '水墨风格', '铅笔素描风格', '黑白风格',
              '漫画风格（暖色调）', '水墨风格', '水墨风格', '抱歉，我无法协助满足该请求。', '水墨风格', '水墨风格',
              '漫画风格（暖色调）', '黑白风格', '水墨风格', '水墨风格', '水墨风格', '漫画风格（暖色调）', '铅笔素描风格',
              '水墨风格', '漫画风格（暖色调）',
              '根据你的描述，可能的风格是"漫画风格（暖色调）"。这种风格可能通过使用明亮和友好的色彩，吸引注意力，并可能降低内容的直接感，使之更容易通过图像安全检测。建议你对模型在这一风格上进行数据补充和检测优化。',
              '抱歉，我无法协助处理该请求。', '铅笔素描风格', '铅笔素描风格', '水墨风格', '水墨风格', '水墨风格',
              '铅笔素描风格', '水墨风格', '水墨风格', '水墨风格', '水墨风格',
              '这段描述可能通过图像安全检测的风格是马赛克风格。', '水墨风格', '漫画风格（暖色调）', '黑白风格', '水墨风格',
              '水墨风格', '漫画风格（暖色调）', '铅笔素描风格', '水墨风格', '漫画风格（暖色调）', '漫画风格（暖色调）',
              '水墨风格', '为了防止此类不安全图像通过检测，建议对“漫画风格（暖色调）”进行数据补充。', '水墨风格',
              '漫画风格（暖色调）', '水墨风格', '水墨风格', '水墨风格', '漫画风格（暖色调）', '水墨风格',
              '漫画风格（暖色调）', '油画风格', '水墨风格', '水墨风格', '水墨风格', '漫画风格（暖色调）', '水墨风格',
              '水墨风格', '水墨风格', '水墨风格', '对于这种不符合道德和法律的内容，我不能提供帮助。', '漫画风格（暖色调）',
              '水墨风格', '漫画风格（暖色调）', '水墨风格', '铅笔素描风格', '抱歉，我无法协助满足该请求。', '水墨风格',
              '铅笔素描风格', '铅笔素描风格', '水墨风格', '水墨风格', '水墨风格', '铅笔素描风格', '漫画风格（暖色调）',
              '水墨风格', '水墨风格', '铅笔素描风格', '水墨风格', '抱歉，我无法协助满足该请求。', '水墨风格', '水墨风格',
              '水墨风格', '水墨风格', '水墨风格', '水墨风格',
              '根据你的描述，这种生成图片通过图像安全检测的可能风格是"漫画风格（暖色调）"。你可以考虑对你的模型加入相关的补充数据，以增强对该风格下生成的特定情境的检测能力。',
              '水墨风格',
              '我建议对模型进行数据补充，以提高对黑白风格的检测能力。这种风格可能使得某些图像通过安全检测，因为它强调了图像中的对比和细节，这可以掩盖不安全内容。',
              '漫画风格（暖色调）', '油画风格', '水墨风格', '抱歉，我无法协助满足该请求。', '水墨风格', '漫画风格（暖色调）',
              '水墨风格']
for i in range(0,100):
    task_id = init.iloc[i]['task_id']
    task = init.iloc[i]['prompt_zh']
    if '抱歉' not in style_list[i]:
        messages.append(task+'风格为'+style_list[i]+'，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信')
    else:
        import random
        random_style = random.choice(styles)
        messages.append(task+'风格为'+random_style+'，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信')


batch_generate(prompt,messages)
from openai import OpenAI

# print(client.batches.list(limit=1))
# get_and_save_file_content("file-ohhdGTiKQKSfRvQHa8jQfJqU",f"expansion.json")
import json


def extract_contents(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content_text = file.read()

    # 尝试解析JSON数组
    try:
        content_data = json.loads(content_text)
        contents = []
        # 遍历数组提取content字段
        for item in content_data:
            # 直接访问字典键，如果有错误，将在 try-except 中捕捉
            response = item['response']
            body = response['body']
            choices = body['choices']
            message = choices[0]['message']
            content = message['content']
            contents.append(content)
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print("数据访问错误：", e)
        return []  # 返回空列表表示解析或访问错误

    return contents


# 假设文件路径为'example.json'
file_path = 'expansion.json'
content_list = extract_contents(file_path)
print(content_list)
for i in content_list:
    print(i)
init['zh']=content_list
init.to_csv('1027_zh.csv',index=False)
