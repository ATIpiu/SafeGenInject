import pandas as pd

init=pd.read_csv('1 1005_en_info_expansion.csv')
messages=[]
prompt_zh=[]
t=0
for i in range(100):
    task_id = init.iloc[i]['task_id']
    task_zh = init.iloc[i]['prompt_zh']
    if '请绘制原输入 请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in task_zh:
        prompt_zh.append(task_zh)
        t+=1
    else:
        prompt_zh.append("白色图片")
print(t)
print(prompt_zh)
init['prompt_zh']=prompt_zh
init.to_csv('1 1005.csv',index=False)
