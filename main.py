from class_persona import Persona
from class_cuentaJoven import CuentaJoven
from class_cuenta import Cuenta

titular = Persona("Leandro", 38, "123456789")
titular.mostrar()
print(titular.es_mayor_de_edad())
cuentaTitular = Cuenta(titular, 1000)
cuentaTitular.mostrar()

titular2 = Persona("Soledad", 20, "987654321")
cuenta_joven1 = CuentaJoven(titular2, 500, 10)
cuenta_joven1.mostrar()
print(cuenta_joven1.es_titular_valido())
cuenta_joven1.retirar(100)
cuenta_joven1.mostrar()