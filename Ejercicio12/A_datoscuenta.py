
def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        print("Presentamos los datos del cliente: ")

        funcion_parametro(*args, **kwargs)

    return funcion_interior

@funcion_decoradora
def datos(nombre_usuario, apellido_usuario, dinero_cuenta):
    print("Nombre y apellido:", nombre_usuario, apellido_usuario, "// Dinero en la cuenta: ", dinero_cuenta,"$")

datos(nombre_usuario = "Alejandro", apellido_usuario = "Martínez", dinero_cuenta = 1000)