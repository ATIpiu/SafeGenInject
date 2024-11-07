import numpy as np
import pandas as pd

tasks_df = pd.read_csv("233 168.csv")



tasks_df['prompt_zh']="测试"
tasks_df['prompt_en']="测试"
tasks_df.to_csv("test_en.csv",index=False)