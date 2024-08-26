'''Microatividade 6: Descrever a utilização argumentos
de funções no Python'''

def loginUsuario(perfil):
  if perfil.lower() == "admin":
    print("Bem-vindo, Administrador")
  else:
    print("Bem-vindo, Usuário")

perfil = ["Admin", "admin", "User", "usuário", "etc."]

for i in perfil:
  print("Tentando com: ", i)
  loginUsuario(i)
