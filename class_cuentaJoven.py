from class_cuenta import Cuenta
class CuentaJoven(Cuenta):
    
    def __init__(self, titular=None, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    def es_titular_valido(self):
        edad = self.get_titular().get_edad()
        return edad >= 18 and edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
    
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.__bonificacion)