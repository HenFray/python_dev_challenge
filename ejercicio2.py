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

  if quantity > 0:
    return "HAY STOCK"
  else:
    return "NO HAY STOCK"
'''buscar una funcion en pandas que busque '''

# <<<<<<<<<<<<<<<<<<<MAIN>>>>>>>>>>>>>>>>>>>>>>

if __name__ == "__main__":
  print("Buenos dias tenemos lo siguentes helados para pedir:")
  print("#############################")

  _PRODUCT_DF = _PRODUCT_DF.rename(columns={'product_name':'Nombre','quantity': 'Cantidad'})
  print(_PRODUCT_DF.to_string(index=False))

  print("#############################")

  eleccion_cliente=input("Cualqueres? ")

  busqueda=_PRODUCT_DF.loc[_PRODUCT_DF['Nombre'] == eleccion_cliente]
  print(busqueda['Cantidad']) # test


  vartest=busqueda['Cantidad']

  StockExistente = is_product_available(eleccion_cliente, vartest)
  print(StockExistente)

