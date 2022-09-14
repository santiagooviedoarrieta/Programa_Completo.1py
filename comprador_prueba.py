from vendedor_1 import lista_cel
from vendedor_1 import caract_memory_intA
from vendedor_1 import caract_memory_ramA
from vendedor_1 import reconocimiento_facial
from vendedor_1 import memoria_expanss
from vendedor_1 import capacidad_de_bateriaA
from vendedor_1 import tipo_de_sist_operativoA
from vendedor_1 import modelo_de_sist_operativoA
from vendedor_1 import precioA
from vendedor_1 import lector_de_huellasA
from vendedor_1 import menu_vendedor
def menu_comprador_prueba():
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                     Bienvenido al programa para comprar tu nuevo celular")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    preg=input("Desea ver los modelos de celulares que poseemos\n>>>")
    if preg== "si":
        print("A continuacion le vamos a mostrar los celulares que temenos disponibles con sus respectivas caracteristicas, se le mostraran varias listas con los celulares")
        print("La lista se lee de arriba a bajo, los celulares con misma marca de fabricante van a aparecer acompañados de un numero para especificar la diferecia")
        print("El orden de las caracteristicas de arriba a abajo es: marca, memoria interna, memoria ram, capacidad de la bateria, si posee lector de huellas, cuanta memoria expansible posee, si posee reconocimiento facial , tipo de sistema operativo, modelo de sistema operativp, precio del producto")
        pregunta=input("¿Continuar?\n>>>")
        if pregunta== "si":
            print(lista_cel)
            print(caract_memory_intA, "GB")
            print(caract_memory_ramA, "GB")
            print(capacidad_de_bateriaA, "Mah")
            print(lector_de_huellasA)
            print(memoria_expanss)
            print(reconocimiento_facial)
            print(tipo_de_sist_operativoA)
            print(modelo_de_sist_operativoA)
            print(precioA, "$")
            resp = input("¿Desea comprar alguno de estos dispositivos?\n>>>")
            if resp == "si":
                respuesta = (input("Ingrese el celular que ha elegido comprar\n>>>"))

                if respuesta in (lista_cel):
                        print(f"El celular que ha elegido comprar fue {respuesta}, solicitelo con ese nombre en la caja")
                        print("-----------------------------------------------------------------------------------------------------------------")
                        print("          FELICIDADES POR COMPRAR SU CELULAR NUEVO, ACERQUESE A LA CAJA PARA SOLICITARLO Y ABONARLO              ")
                        print("         GRACIAS POR USAR EL PROGRAMA DE COMPRA DE TELEFONOS CELULARES, ESPERAMOS TE HAYA RESULTADO UTIL         ")
                        print("-----------------------------------------------------------------------------------------------------------------")
                else:
                    print("Lo sentimos, ese dispositivo no se encuentra en la lista, intentelo de nuevo")
            else:
                print("Lamentamos no haber podido conseguir un celular que se ajuste a sus necesidades")
        else:
            if pregunta== "no":
                print("Desidio no ver los modelos que tenemos disponibles")
            else:
                print("Respuesta no valida, vuelva a ingresar")
    else:
        if preg =="acceder_como_vendedor":
            menu_vendedor()
        else:
            if preg == "no":
                print("Desidio no ver los modelos que tenemos disponibles, el programa se reiniciara")
            else:
                print("Respuesta no valida, vuelva a intentarlo")