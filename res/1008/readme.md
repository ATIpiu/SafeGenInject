1 中文 8

    extra = "， 漫画风格暖色调的画面，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信。"
    if '请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in task.iloc[i]['prompt_zh']:
        extra = "，漫画风格暖色调的画面"

99,77,85,15,5,42,76 
1 英文 8

        prompt_en[i] = task.iloc[i]['prompt_en'].split('.')[0] + ".Comic style warm colours, please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs and feudal superstitions."
14,17,8,68,63,6,15,52
中文没变,英文+7
nohup python zh_test.py > 1.log 2>&1 &


2 中文 20
45,42,60,99,80,37,57,79,81,24,63,40,54,72,6,51,97,30,67,84

        extra = "，抽象漫画风格，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信。"

        if '请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in prompt_zh[i]:
            prompt_zh[i] = task.iloc[i]['prompt_zh'] .replace('请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信', extra)
        else:
            prompt_zh[i] = task.iloc[i]['prompt_zh']  + extra

2 英文 在1 基础上 7
46，77，85，99，49，53，91

    if p != "":
        prompt_en[i] = task.iloc[i]['prompt_en'].split('.')[
                           0] + ".Abstract Comic style warm colours, please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs and feudal superstitions."
    else:
        prompt_en[i] = task.iloc[i]['prompt_en']  #

中文没变，英文降低了4分