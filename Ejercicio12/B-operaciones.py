
from A_datoscuenta import *

def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs):

        print("Vamos a realizar unas operaciones en tu cuenta: ")

        funcion_parametro(*args, **kwargs)

    return funcion_interior

operacion = input("Que operación desea realizar? (1) Extraer dinero, (2) Ingresar dinero, (3) Mostrar dinero en la cuenta: ")

if operacion == 1:
    @funcion_decoradora
    def extraer_dinero(dinero_extraido):
        if dinero_extraido < dinero_cuenta or nombre_usuario == "Alejandro":
            dinero_cuenta = dinero_cuenta - dinero_extraido
            print("Te quedan ", dinero_cuenta, "$ en la cuenta.")       
        else:
            print("No se puede extraer esa cantidad de dinero ya que no hay suficiente dinero en la cuenta.")
    extraer_dinero(dinero_extraido)

if operacion == 2:
    def ingresar_dinero(dinero_ingresado):
        dinero_cuenta = dinero_cuenta + dinero_ingresado
        print("Ahora tienes", dinero_cuenta," en la cuenta.")
    ingresar_dinero(dinero_ingresado)

if operacion == 3:
    def mostrar_dinero():
        print("Tu dinero en la cuenta: ", dinero_cuenta,"$")
    mostrar_dinero()

