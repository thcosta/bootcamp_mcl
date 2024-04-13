def retorna_impares(lista) -> list:
  return list(filter(lambda numero: numero % 2 != 0 , lista))

lista = [0,1,2,3,4,5,6,7,8,9,10]
print(f'Lista: {lista}')
print(f'Resultado: {retorna_impares(lista)}')