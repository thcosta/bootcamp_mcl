import pandas as pd

df = pd.DataFrame({
    'a': range(5),
    'b': [-100, -50, 0, 200, 1000]
})

# Selecionando uma coluna
print(f'Selecionando coluna b: {df['b']}')

# Filtrando linhas
filtro = df['b'] > 0
print(f'Filtrando valores positivos da coluna b: {df[filtro]}')