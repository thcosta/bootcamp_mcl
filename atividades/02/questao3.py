def remove_duplicados(lista_a, lista_b) -> list:
  lista_c = lista_a + lista_b
  return list( dict.fromkeys(lista_c) )

lista_a = [0,1,2,3,4,5,6,7,8,9,10];
lista_b = [0,2,4,6,8,10,11,12,13,14,15]
print(f'Lista 1: {lista_a}')
print(f'Lista 2: {lista_b}')
print(f'Resultado: {remove_duplicados(lista_a, lista_b)}')