# Baseado no algoritmo em Linguagem C: https://github.com/EscovandoBits/cpf/blob/main/cpf.c

# verifica se um número de CPF é válido
def cpf_valido(n):
  #print('cpf_valido(%011d)' % n)

  # extrair dígitos verificadores
  dv = n % 100
  d10 = dv // 10
  d11 = dv % 10

  # calcular penúltimo dígito
  v1 = 0
  r = n // 100
  i = 9
  while True:
    d = r % 10
    r = r // 10
    v1 += i * d
    i = i - 1
    if not (r > 0 and i > 0):
      break
  v1 = (v1 % 11) % 10
  if (v1 != d10):
    return 0

  # calcular último dígito
  v2 = 0
  r = n // 100
  i = 8
  while True:
    d = r % 10
    r = r // 10
    v2 += i * d
    i = i - 1
    if not (r > 0 and i > 0):
      break
  v2 += 9 * v1
  v2 = (v2 % 11) % 10
  if (v2 != d11):
    return 0

  return 1

if __name__ == "__main__":
  for num in [11111111111, 11111111112, 22222222222, 22222222221, 123]:
    print('cpf_valido(%011d)? %d' % (num, cpf_valido(num)))

