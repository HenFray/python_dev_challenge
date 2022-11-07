import pandas as pd

# LOCAL
from ejercicio1 import GeoAPI
from ejercicio2 import is_product_available
from ejercicio3 import validate_discount_code


if  GeoAPI == True:
    print("Bienvenida 1")
else:
    print("Bienvenida 2")

# ACA VA EL EJERCICIO 2
print('Que sabor queres tenemos: ')

_PRODUCT_DF = pd.DataFrame(
{
  "product_name": [
    "Chocolate",
    "Granizado",
    "Limon",
    "Dulce de Leche"
  ],
  "quantity": [
    3,
    10,
    0,
    5
  ]
}
)

print(_PRODUCT_DF.rename(columns={'product_name': 'Nombre', 'quantity': 'Cant'}).to_string(index=False))

condicional = True
while condicional:
    sabor = input("Que sabor queres? ")
    cantidad = int(input(f"Cuantos de {sabor} queres? "))
    is_product_available(sabor, cantidad)

    if is_product_available(sabor, cantidad) == True:
        break
    else:
        print("No tenemos stock suficiente para esa cantidad!")
        pass


while True:
    code = input("Codigo de descuento: ")
    if validate_discount_code(code) == True:
        break
    else:
        print("CODIGO INVALIDO")
        print("CTRL+C para salir")
        pass

print("SU PEDIDO A SIDO CONFIRMADO!")






