import pandas as pd

df = pd.DataFrame({
    'col_1': range(5),
    'col_2': [-100, -50, None, 200, 1000],
    'col_3': ['a', 'b', 'c', 'd', 'e']
})

# Opção 1 - removendo linhas com valores ausentes
print(f'Removendo a linha com valores ausentes: {df.dropna()}')

# Opção 2 - removendo colunas com valores ausentes
print(f'Removendo a coluna com valores ausentes: {df.dropna(axis=1)}')

# Opção 2 - preenchendo os valores ausentes com a média da coluna
print(f'Preenchendo os valores ausentes com a média da coluna: {df.fillna(df["col_2"].mean())}')