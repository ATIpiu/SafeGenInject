
from openai import OpenAI
import json
import time
# 初始化客户端
client = OpenAI(api_key= "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")

def create_jsonl_file(prompts_messages, model="gpt-3.5-turbo-0125", max_tokens=1000):
    """创建一个JSONL文件的内容。"""
    entries = []
    for i, (prompt, messages) in enumerate(prompts_messages, 1):
        entry = {
            "custom_id": f"request-{i}",
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": model,
                "messages": [{"role": "system", "content": prompt}] + [{"role": "user", "content": msg} for msg in messages],
                "max_tokens": max_tokens
            }
        }
        entries.append(json.dumps(entry))
    return "\n".join(entries)

def upload_jsonl_to_openai(jsonl_content):
    """上传JSONL内容到OpenAI并返回文件ID。"""
    with open("temp_batch_input.jsonl", "w") as file:
        file.write(jsonl_content)
    with open("temp_batch_input.jsonl", "rb") as file:
        response = client.files.create(file=file, purpose="batch")
    return response.id

def create_batch_request(input_file_id):
    """创建一个批处理请求。"""
    response = client.batches.create(
        input_file_id=input_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h"
    )
    return response

def retrieve_and_save_results(batch_id, output_filename="batch_results.json"):
    """检索批处理结果并在批处理完成后保存到文件。"""
    while True:
        batch = client.batches.retrieve(batch_id)
        # 确保处理对象，获取其状态
        batch_status = batch.status  # 假设 `Batch` 对象有一个 `status` 属性

        if batch_status in ['completed', 'failed', 'expired']:  # 根据具体情况调整完成的状态
            # 创建一个可以序列化的字典
            batch_dict = {
                'id': batch.id,
                'status': batch.status,
                'created_at': batch.created_at,
                'completed_at': batch.completed_at,
                # 你可以继续添加你需要的其他字段
            }
            return batch.output_file_id
        else:
            print("批处理尚未完成，正在等待...")
            time.sleep(5)  # 每隔5秒检查一次


def get_and_save_file_content(file_id, save_path="saved_file_content.json"):
    """从OpenAI获取文件内容并保存到JSON文件。"""
    file_content = client.files.content(file_id)  # 获取文件内容
    content_text = file_content.text  # 假设文件内容为文本
    print("原始文本内容：")
    print(content_text)  # 打印文件原始内容

    # 处理可能存在的多个JSON对象
    try:
        # 将多个JSON对象拼接成一个数组
        json_objects = "[" + content_text.replace("}\n{", "},\n{") + "]"
        content_data = json.loads(json_objects)
        # 将解析后的JSON数据保存到文件
        with open(save_path, "w", encoding='utf-8') as f:
            json.dump(content_data, f, ensure_ascii=False, indent=4)
        print(f"文件内容已保存到 {save_path}")
    except json.JSONDecodeError as e:
        # 打印错误详情和位置
        print("JSON解析错误：", e)
        # 也许需要额外的逻辑来处理或修复数据
