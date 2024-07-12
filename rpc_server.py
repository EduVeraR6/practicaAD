from xmlrpc.server import SimpleXMLRPCServer

def suma(x, y):
    return x + y

server = SimpleXMLRPCServer(('0.0.0.0', 8000))
server.register_function(suma, 'suma')
print("Esperando solicitudes RPC...")
server.serve_forever()