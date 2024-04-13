def ordena_nomes(tupla) -> tuple:
  return sorted(tupla, key=lambda pessoa: pessoa['nome'])

tupla = [
  {
    'nome': 'Carlos',
    'idade': 40
  },
  {
    'nome': 'Bruno',
    'idade': 25
  },
  {
    'nome': 'Ana',
    'idade': 32
  }
];
print(f'Tupla: {tupla}')
print(f'Resultado: {ordena_nomes(tupla)}')