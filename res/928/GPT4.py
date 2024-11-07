import openai
import pandas as pd
import re

from openai import OpenAI

# 初始化 OpenAI 客户端



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

def trans():
    txt = open('prompt_zh.txt', encoding='utf-8').readlines()

    # 初始化一个空列表存储翻译结果
    translated_results = []

    # 每次读取10行，总共100行
    # 获取当前的10行内容
    for i in range(0,100,10):
        content = "".join(txt[i:i + 10])

        # 创建翻译请求的提示
        categories_prompt = [
            {
                "role": "user",
                "content": f"帮我翻译成英文并且放入python列表中,细节都需要翻译,全部翻译"
                           f"是错误的请用It is wrong : "
                           f"{content}"
            }
        ]

        # 调用生成安全文本的函数 (假设 generate_safe_text 函数存在)
        result_en = generate_safe_text(categories_prompt)
        print(result_en)
        # 将翻译结果加入列表
        translated_results.append(result_en)
def txt_opt():
    pass
if __name__ == "__main__":
    txt_opt()