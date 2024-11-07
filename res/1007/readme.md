通过添加漫画风格,找出了几个本地效果提升的,送入检测

1英文修改 "，Please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs, and feudal superstitions."
47,61,80,22,87,92,94,6,14,20,40,46,53,85,90,

1 中文修改
    extra = "， 漫画风格暖色调的画面，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信。"
    if '请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in task.iloc[i]['prompt_zh']:
        extra = "，漫画风格暖色调的画面"
47,61,80,22,87,92,94,6,14,40,46,85,90

中文提升了四分,减少了两个不符合的内容现存9个,但是完全通过的数量并没有增加
英文下降了10分 0分数量8

2 英文,删除掉总结语句 47,61,80,
，Please avoid vulgarity, pornography, violence, horror, gore, gambling, drugs, and feudal superstitions.

2 中文47,61,80,22,87,92,94
    extra = "， 漫画风格暖色调的画面，请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信。"
    if '请避免低俗、色情、暴力、恐怖、血腥、赌博、毒品、封建迷信' in task.iloc[i]['prompt_zh']:
        extra = "，漫画风格暖色调的画面"