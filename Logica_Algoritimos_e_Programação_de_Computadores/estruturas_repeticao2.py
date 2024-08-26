'''Microatividade 4: Descrever a utilização da estrutura
de repetição for em Python'''

texto = "Olá, laço for."

for i in texto:
  item = i
  print("Caractere: ", item)

for i in range(1,11):
  print("Número do intervalo: ", str(i)) # we don't need this str(), python does it already 