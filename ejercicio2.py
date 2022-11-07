import pandas as pd


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


def is_product_available(product_name, quantity):
  stock = _PRODUCT_DF[(_PRODUCT_DF['product_name'] == product_name) & (_PRODUCT_DF['quantity'] >= quantity)]
  return len(stock) > 0


# <<<<<<<<<<<<<<<<<<<MAIN>>>>>>>>>>>>>>>>>>>>>>

if __name__ == "__main__":
  print(is_product_available("Chocolate", 4))
  print(is_product_available("Chocolate", 2))
'''  print("Buenos dias tenemos lo siguentes helados para pedir:")
  print("#############################")

  _PRODUCT_DF = _PRODUCT_DF.rename(columns={'product_name':'Nombre','quantity': 'Cantidad'})
  print(_PRODUCT_DF.to_string(index=False))

  print("#############################")

  eleccion_cliente=input("Cualqueres? ")

  busqueda=_PRODUCT_DF.loc[_PRODUCT_DF['Nombre'] == eleccion_cliente]
  print(busqueda['Cantidad']) # test


  vartest=busqueda['Cantidad']

  StockExistente = is_product_available(eleccion_cliente, vartest)
  print(StockExistente)'''

