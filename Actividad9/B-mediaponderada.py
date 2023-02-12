
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        print("Vamos a calcular la media ponderada: ")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el cálculo.")

    return funcion_interior

@funcion_decoradora
def calcular_media(num1, num2, num3, pond1, pond2, pond3):
    print(num1*pond1 + num2*pond2 + num3*pond3)

calcular_media(11, 32, 9, 0.2, 0.3, 0.5)