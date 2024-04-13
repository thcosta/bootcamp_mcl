def segundo_maior(lista):
  maior = max(lista)
  lista.remove(maior)
  return max(lista)

lista = [0,1,2,3,4,5,6,7,8,9,10];
print(f'Lista: {lista}')
print(f'Resultado: {segundo_maior(lista)}')