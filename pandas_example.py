import pandas as pd

df = pd.read_csv('./pokemon_small.csv')

print(df.to_latex(index=False, na_rep=''))