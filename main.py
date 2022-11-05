from ejercicio1 import GeoAPI
#from ejercicio2 
from ejercicio3 import validate_discount_code


if  GeoAPI == True:
    print("Bienvenida 1")
else:
    print("Bienvenida 2")

# ACA VA EL EJERCICIO 2

while True:
    code = input("Codigo de descuento: ")
    if validate_discount_code(code) == True:
        break
    else:
        print("CODIGO INVALIDO")
        print("CTRL+C para salir")
        pass

print("SU PEDIDO A SIDO CONFIRMADO!")






