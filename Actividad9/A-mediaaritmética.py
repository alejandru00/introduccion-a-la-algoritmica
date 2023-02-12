
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        print("Vamos a calcular la media aritmética: ")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el cálculo.")

    return funcion_interior

@funcion_decoradora
def calcular_media(num1, num2, num3):
    print((num1 + num2 + num3) / 3)

calcular_media(11, 32, 9)