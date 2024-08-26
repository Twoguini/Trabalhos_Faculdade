'''Trabalho Prático'''

saida = ""

def adicao(num1, num2):
  return num1 + num2

def subtracao(num1, num2):
  return num1 - num2

def multiplicacao(num1, num2):
  return num1 * num2

def divisao(num1, num2):
  if num2 == 0:
    print("Impossível realizar uma divisão por 0")
    return
  else:
    return num1 / num2

def calculadora(num1, operador, num2):
  resultado = ""
  match operador:
    case "+":
      resultado = adicao(int(num1), int(num2))
    case "-":
      resultado = subtracao(int(num1), int(num2))
    case "*":
      resultado = multiplicacao(int(num1), int(num2))
    case "/":
      resultado = divisao(int(num1), int(num2))
    case _:
      print("Operador Não Encontrado")
  
  return resultado

while saida.lower() != "n":
  num1 = input("Digite o primeiro número: ")
  operador = input("Digite o operador (+ - * /): ")
  num2 = input("Digite o Segundo número: ")

  print("O resultado da operação é: ", calculadora(num1, operador, num2))

  saida = input("Deseja continar a execução do programa? (s ou n): ")