import os
import pandas as pd


# Lendo CSV
dir = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(os.path.join(dir, 'teste.csv'))
print(df.to_string())