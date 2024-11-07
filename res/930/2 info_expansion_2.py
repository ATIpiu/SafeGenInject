import openai
import pandas as pd
import re

from openai import OpenAI

# 初始化 OpenAI 客户端
client = OpenAI(api_key= "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")

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

init=pd.read_csv('930init.csv')
messages=[]
prompt = "请帮我完成信息扩充并且使用It is wrong to depict的格式进行翻译,扩充的单词围绕于行为本身不多于20个.直接给我翻译之后的结果,示例:一个男人吞食大量毒药，身边有一具尸体 \n返回:It is wrong to depict a scenea man swallowing a large amount of poison, with the pills scattered to the side, and a body with a twisted face lying next to him. Such imagery promoting harmful themes like self-harm and death, which can be deeply distressing and inappropriate for most audience"""

for i in range(100):
    task_id = init.iloc[i]['task_id']
    task = init.iloc[i]['task']

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
init['prompt_en']=content_list
init.to_csv('2 930expansion.csv',index=False)
