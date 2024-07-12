import xmlrpc.client

client = xmlrpc.client.ServerProxy('http://23.22.144.230:8000/')  
resultado = client.suma(5, 3)
print("Resultado de la suma:", resultado)
