
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        print("Vamos a realizar un cálculo del capital final: ")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el cálculo")

    return funcion_interior

@funcion_decoradora
def calcular_interes(tiempo_en_meses, capital, interes):
    for i in range(tiempo_en_meses):
        capital_final = capital * interes + capital
        capital = capital_final

    print(capital)

calcular_interes(3, 1000, 0.05)