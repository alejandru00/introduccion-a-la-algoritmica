
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        print("Vamos a calcular el área de un triángulo: ")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el cálculo.")

    return funcion_interior

@funcion_decoradora
def calcular_area(medida_lado, altura):
    print(medida_lado * altura / 2)

calcular_area(5, 7)