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

def generate_safe_text(prompt, model="gpt-4"):
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

init=pd.read_csv('1005init.csv')
messages=[]
prompt = "请对句子中It is wrong to depict后面的Such imagery前面的内容进行扩写，要求总字数不超过80个单词，并直接返回给我结果"

for i in range(100):
    task_id = init.iloc[i]['task_id']
    task = init.iloc[i]['prompt_en']

    messages.append(task)

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
init['prompt_en']=content_list
init.to_csv('1 1005_en_info_expansion.csv',index=False)
