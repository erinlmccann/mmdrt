import os
import pandas as pd

inputPath = 'C:/Users/mcca512/OneDrive - PNNL/McCann Documents/Other Projects/SAR Analyses/'
D = pd.read_csv(os.path.join(inputPath, 'returning_fish_unscreened.csv'))