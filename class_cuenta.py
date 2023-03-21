class Cuenta:
    
    def __init__(self, titular=None, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad
    
    def set_titular(self, titular):
        self.titular = titular
    
    def get_titular(self):
        return self.titular
    
    @property
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print("Titular:", self.titular.get_nombre())
        print("Cantidad:", self.__cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad


