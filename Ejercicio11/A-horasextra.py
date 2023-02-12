def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        print("Vamos a calcular lo que deberia cobrar un trabajado por sus horas extra: ")

        funcion_parametro(*args, **kwargs)

        print("Hemos terminado el cálculo.")

    return funcion_interior

@funcion_decoradora
def calcular_horas_extra(horas_trabajadas, salario_mensual_bruto):
    if horas_trabajadas >= 44:
        print((horas_trabajadas-35) * salario_mensual_bruto/35 * 1,5)

    if horas_trabajadas >= 36 and horas_trabajadas <= 43:
        print((horas_trabajadas-35) * salario_mensual_bruto/35 * 1,25)

calcular_horas_extra(45, 1000)