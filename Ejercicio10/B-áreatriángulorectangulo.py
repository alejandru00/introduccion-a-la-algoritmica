
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        print("Vamos a calcular el área de un triángulo rectangulo: ")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el cálculo.")

    return funcion_interior

@funcion_decoradora
def calcular_area(medida_lado):
    print(medida_lado * medida_lado / 2)

calcular_area(5)