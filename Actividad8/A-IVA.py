
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        print("Vamos a realizar un cálculo del precio final producto con IVA: ")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el cálculo.")

    return funcion_interior

@funcion_decoradora
def calcular_iva(precio_produto, tipo_iva):

    print(precio_produto * tipo_iva + precio_produto)


calcular_iva(200, 21/100)
