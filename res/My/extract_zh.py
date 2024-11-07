import numpy as np
import pandas as pd

tasks_df = pd.read_csv("249 213 My.csv")



tasks_df['prompt_en']="white picture"
tasks_df.to_csv("test_zh.csv",index=False)