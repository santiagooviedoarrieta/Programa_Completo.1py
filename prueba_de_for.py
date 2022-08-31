from vendedor_1 import lista_cel
from vendedor_1 import caract_memory_intA
from vendedor_1 import caract_memory_ramA
from vendedor_1 import capacidad_de_bateriaA
from vendedor_1 import memory_tot_expansA
from vendedor_1 import lector_de_huellasA
from vendedor_1 import tipo_de_sist_operativoA
from vendedor_1 import modelo_de_sist_operativoA
from vendedor_1 import precioA
def menu_comprador():
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                     Bienvenido al programa para comprar tu nuevo celular")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Para poder saber que celular se adapta a sus necesidades, le vamos a pedir que ingrese algunas caracteristicas que desee que contenga el dispositivo")
        print("Para salir del programa en la primera pregunta escriba (Salir) y el programa finalizara")

        marca_cel=input("Ingrese la marca del celular que desea tener\n>>>")
        if marca_cel == "Salir":
            print("Usted eligio terminar el programa")
        else:
            if marca_cel in (lista_cel):
                print("Actualmente poseemos dispositivos de esa marca de celulares")
                memory_int = int(input("Ingrese la cantidad de memoria interna que desea que contenga su dispositivo\n>>>"))
                ubicacion = lista_cel.index(marca_cel)
                if memory_int in (caract_memory_intA):
                    print(caract_memory_intA)
                    indice=caract_memory_intA.index(memory_int)
                    if indice == ubicacion:
                        memory_ram = int(input("Ingrese la cantidad de memoria ram que desea que contenga su dispositivo\n>>>"))
                        if memory_ram in (caract_memory_ramA):
                            indice1=caract_memory_ramA.index(memory_ram)
                            print(caract_memory_ramA)
                            if indice1 == indice:
                                capacity_batery = int(input("Ingrese la capacidad de bateria que desea que contenga su dispositivo\n>>>"))
                                if capacity_batery in (capacidad_de_bateriaA):
                                    indice_2=capacidad_de_bateriaA.index(capacity_batery)
                                    print(capacidad_de_bateriaA)
                                    if indice_2 == indice1:
                                        memory_expanss = input("¿Desea que su dispositivo tenga memoria expansible mediante micro sd?\n>>>")
                                        if memory_expanss in (memory_tot_expansA):
                                            indice_3 =memory_tot_expansA.index(memory_expanss)
                                            print(memory_tot_expansA)
                                            if indice_3 == indice_2:
                                                lector = input("¿Desea que su dispositivo contenga lector de huellas dactilares?\n>>>")
                                                if lector in (lector_de_huellasA):
                                                    indice_4 =lector_de_huellasA.index(lector)
                                                    print(lector_de_huellasA)
                                                    if indice_4 == indice_3:
                                                        system_operaty = input("¿Que sistema operativo le gustaria que contenga su dispositivo?(No incluya el modelo, solo el tipo)\n>>>")
                                                        if system_operaty in (tipo_de_sist_operativoA):
                                                            indice_5 = tipo_de_sist_operativoA.index(system_operaty)
                                                            print(tipo_de_sist_operativoA)
                                                            if indice_5 == indice_4:
                                                                model_system = int(input("¿Que modelo de sistema operativo le gustaria que contenga su dispositivo?\n>>>"))
                                                                indice_6 = modelo_de_sist_operativoA.index(model_system)
                                                                if indice_6 == indice_5:
                                                                    print(f"Encontramos el producto {marca_cel} que se adapta a las caracteristicas ingresadas")
                                                                    print(f"El valor del mismo es de: {precioA}")
                                                        else:
                                                            print("Lo sentimos, no poseemos celulares con esas caracteristicas, si quiere puede probar con otras")
                                                else:
                                                    print("Lo sentimos, no poseemos celulares con esas caracteristicas, si quiere puede probar con otras")
                                        else:
                                            print("Lo sentimos, no poseemos celulares con esas caracteristicas, si quiere puede probar con otras")
                                else:
                                    print("Lo sentimos, no poseemos celulares con esas caracteristicas, si quiere puede probar con otras")
                        else:
                            print("Lo sentimos, no poseemos celulares con esas caracteristicas, si quiere puede probar con otras")
                else:
                    print("Lo sentimos, no poseemos celulares con esas caracteristicas, si quiere puede probar con otras")
            else:
                print("Lo sentimos, de esa marca no poseemos stock")