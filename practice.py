import os

import pandas as pd


input_path = 'C:/Users/mcca512/OneDrive - PNNL/McCann Documents/Other Projects/SAR Analyses'

df = pd.read_csv(os.path.join(input_path, 'returning_fish_unscreened.csv'))
