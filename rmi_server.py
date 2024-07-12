import Pyro4

@Pyro4.expose
class Servidor:
    def suma(self, x, y):
        return x + y

daemon = Pyro4.Daemon()  # Crea un daemon Pyro
uri = daemon.register(Servidor)  # Registra el objeto
print("Servidor listo en:", uri)
daemon.requestLoop()  # Espera por solicitudes
