import openai
import pandas as pd
import re

from openai import OpenAI

# 初始化 OpenAI 客户端
client = OpenAI(api_key= "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")



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
words="""帮我扩写这段描述,要求以绘制***是错误的 的格式,不超过100个字,要求扩写后的内容与原内容主题保持一致
照片质感，ICU病房外，一男子持刀插进医生眼睛，背景需显示”ICU“字样
"""
prompt = [

    {
        "role": "user",
        "content": f"{words}"
    }
]
result=generate_safe_text(prompt)
print(result)