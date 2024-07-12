import Pyro4

uri = "PYRONAME:http://23.22.144.230:8000/"  # Asumiendo que el nombre de objeto es "Servidor"
servidor = Pyro4.Proxy(uri)  # Conéctate al objeto remoto
resultado = servidor.suma(10, 5)
print("Resultado de la suma:", resultado)
