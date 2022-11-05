import jellyfish


_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1",
"heladoFrozen"]


def validate_discount_code(discount_code):
    """
    Ejemplo:
    "primavera2021" deberia devolver True, ya que al compararlo:
    vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
    vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o', 'm', 'V','p', 'v')
    vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0', 'x', 'e','d', 'p', 'r')
    vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i', 'v', 'n','o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
    """
    if jellyfish.levenshtein_distance(discount_code ,_AVAILABLE_DISCOUNT_CODES[0])<=3:
        return True #, "es compatible con Primavera2021" 
    elif jellyfish.levenshtein_distance(discount_code ,_AVAILABLE_DISCOUNT_CODES[1])<=3:
        return True #, "es compatible con Verano2021"
    elif jellyfish.levenshtein_distance(discount_code ,_AVAILABLE_DISCOUNT_CODES[2])<=3:
        return True #, "es compatible con Navidad2x1"
    elif jellyfish.levenshtein_distance(discount_code ,_AVAILABLE_DISCOUNT_CODES[3])<=3:
        return True #, "es compatible con heladoFrozen"
    else:
        return False #, "no es compatible con ninguno"


if __name__ == "__main__":
    
    code = input("Codigo de descuento: ")
    validate_func= validate_discount_code(code)

    print(validate_func)
