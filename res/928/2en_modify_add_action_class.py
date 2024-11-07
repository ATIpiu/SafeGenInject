import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# 加载数据
task = pd.read_csv('2 928.csv')

# 定义行为
actions = [
    ("拒绝吸毒。", "Reject drug use."),
    ("拒绝伤害成年人。", "Reject harm to adults."),
    ("拒绝伤害未成年人。", "Reject harm to minors."),
    ("拒绝暴力行为。", "Reject violent behavior."),
    ("拒绝血腥行为。", "Reject bloody behavior."),
    ("拒绝低俗行为。", "Reject vulgar behavior."),
    ("拒绝伤害他人。", "Reject harm to others."),
    ("拒绝违法行为。", "Reject illegal behavior."),
    ("拒绝色情内容。", "Reject sexual content."),
    ("拒绝伤害自己。", "Reject harm to oneself."),
    ("拒绝赌博。", "Gambling is wrong."),
]


# 标注数据的函数
def annotate_data(i):
    if i >= len(task):
        messagebox.showinfo("完成", "数据标注完成。")
        task.to_csv("2 928.csv", index=False)
        root.quit()
        return

    task_content = task.iloc[i]['task']
    msg = f"{task_content}\n请选择行为："

    def on_click(action_index):
        if action_index < len(actions) - 1:  # 有拒绝的行为
            task.at[i, 'prompt_en'] = task.iloc[i]['prompt_en'] + actions[action_index][1]
        annotate_data(i + 1)  # 继续下一个任务

    # 清除先前的按钮
    for widget in button_frame.winfo_children():
        widget.destroy()

    tk.Label(button_frame, text=msg, font=("Arial", 14)).pack()

    for idx, (chinese_text, english_text) in enumerate(actions):
        tk.Button(button_frame, text=chinese_text, command=lambda index=idx: on_click(index), font=("Arial", 12),
                  width=25).pack(pady=5)


# 创建主窗口
root = tk.Tk()
root.title("数据标注")
root.geometry("600x400")  # 设置窗口大小
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
annotate_data(0)
root.mainloop()