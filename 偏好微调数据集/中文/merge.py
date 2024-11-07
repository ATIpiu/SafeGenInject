import json

# 从文件读取数据
with open('merged_output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 初始化最终数据格式
final_data = []

# 遍历每个记录并转换格式
for item in data:
    conversation = {
        "conversations": [
            {
                "from": "human",
                "value": item["input"]
            }
        ],
        "chosen": {
            "from": "gpt",
            "value": item["chosen"]
        },
        "rejected": {
            "from": "gpt",
            "value": item["rejected"]
        }
    }
    final_data.append(conversation)

# 将最终格式保存为新的JSON文件
with open('formatted_conversations.json', 'w', encoding='utf-8') as output_file:
    json.dump(final_data, output_file, ensure_ascii=False, indent=2)

print("数据已成功转换并保存到 formatted_conversations.json 文件中。")
