import os

import pandas as pd


input_path = 'C:/Users/mcca512/OneDrive - PNNL/McCann Documents/MMD Adult Study/mmd_sum_2022/data/parquet_raw_data'

df = pd.read_parquet(os.path.join(input_path, '1_MITAS_20220626_20220627.parquet'), engine = 'pyarrow')
