def dividir(a, b):
    if a == 0 or b == 0:
        raise ZeroDivisionError("No se puede dividir por 0")
    else:
        return a / b

if __name__ == "__main__":
    print(dividir(6, 3))