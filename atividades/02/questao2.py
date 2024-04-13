def retorna_primos(lista) -> list:
  def verifica_divisibilidade(numero) -> int:
    for i in range(2, numero - 1):
      return False if numero % i == 0 else True
    
  return list(filter(lambda numero: verifica_divisibilidade(numero), lista))

lista = [0,1,2,3,4,5,6,7,8,9,10]
print(f'Lista: {lista}')
print(f'Resultado: {retorna_primos(lista)}')