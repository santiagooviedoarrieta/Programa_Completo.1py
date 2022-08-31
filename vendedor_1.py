lista_cel= []
caract_memory_intA=[]
caract_memory_ramA=[]
lector_de_huellasA=[]
memoria_expanss=[]
reconocimiento_facial=[]
tipo_de_sist_operativoA=[]
modelo_de_sist_operativoA=[]
capacidad_de_bateriaA=[]
precioA=[]
def menu_vendedor():
    for i in range(3):
        user_contra= "Celulares"
        contra_user = input("Por metodos de seguridad para poder ingresar necesitamos su contraseña,tiene 3 intentos \n >>>")
        print("Si llega a ingresar como un comprador, debe escribir (acceder_como_vendedor) para acceder a este apartado")
        if user_contra == contra_user:
            break
        else :
            if contra_user == "comprador":
                break
            else:
                print("La contraseña ingresada fue incorrecta")
    if contra_user == user_contra :
        while True:
            print("Bienvenido señor/a, en este apartado podra registrar y modificar su inventario de venta")
            print("Ingrese una de las entradas del menu ")
            print("1.Mostrar lista de productos")
            print("2.Ingresar un producto ")
            print("3 Borrar un producto")
            print("4.Salir")
            respuesta = (int(input(">>> ")))
            if respuesta == 1:
                lista_cel.sort()
                print(lista_cel)
            elif respuesta == 2:
                cuantos_cel = int(input("Ingrese la cantidad de celulares a insertar: "))
                for i in range(cuantos_cel):
                    cel_new= input("Ingrese el celular a añadir \n >>> ")
                    lista_cel.append(cel_new)
                    caract_memory_int =int(input("Ingrese la memoria interna que posee el dispositivo\n>>>"))
                    caract_memory_intA.append(caract_memory_int)
                    caract_memory_ram=int(input("Ingrese la memoria ram que posee el dispositivo\n>>>"))
                    caract_memory_ramA.append(caract_memory_ram)
                    lector_de_huellas=(input("¿Posee lector de huellas?\n>>>"))
                    if lector_de_huellas == "si":
                        lector_de_huellasA.append(lector_de_huellas)
                        reco= input("¿Tambien posee reconocimiento facial?\n>>>")
                        if reco == "si":
                            print("Perfecto,sera añadido como caracteristica")
                            reconocimiento_facial.append(reco)
                        else:
                            if reco == "no":
                                print("Indico que no posee detector de reconocimiento facial")
                                reconocimiento_facial.append("no")
                            else:
                                print("Respuesta no valida, se anotara como que no posee detector de reconocimiento")
                                reconocimiento_facial.append("no")
                    else:
                        print("Indico que no posee lector de huellas")
                    preg=(input("Posee memoria expansible?\n>>>"))
                    if preg == "si":
                        preg_1 = int(input("Cuanta memoria expansible posee?\n>>>"))
                        memoria_expanss.append(preg_1)
                    else:
                        if preg == "no" :
                            print("Usted indico que el dispositivo no posee memoria expansible")
                            memoria_expanss.append(0)
                        else:
                            print("Respuesta no valida, se indicara que no posee memoria expansible")
                            memoria_expanss.append(0)
                    tipo_de_sist_operativo=(input("Que tipo de sistema operativo posee (ej:android)\n>>>"))
                    tipo_de_sist_operativoA.append(tipo_de_sist_operativo)
                    modelo_de_sist_operativo=int(input("cual es el modelo de sistema operativo posee (ej:9)\n>>>"))
                    modelo_de_sist_operativoA.append(modelo_de_sist_operativo)
                    capacidad_de_bateria=int(input("cual es la capacidad de la bateria en miliamperios\n>>>"))
                    capacidad_de_bateriaA.append(capacidad_de_bateria)
                    precio=int(input("Ingrese el precio del producto sin el simbolo de pesos\n>>>"))
                    precioA.append(precio)
            elif respuesta == 3 :
                cual_cel=input("Ingrese el producto que desea eliminar\n>>>")
                if cual_cel in lista_cel:
                    indice_cel= lista_cel.index(cual_cel)
                    lista_cel.remove(cual_cel)
                    caract_memory_intA.pop(indice_cel)
                    caract_memory_ramA.pop(indice_cel)
                    lector_de_huellasA.pop(indice_cel)
                    tipo_de_sist_operativoA.pop(indice_cel)
                    modelo_de_sist_operativoA.pop(indice_cel)
                    capacidad_de_bateriaA.pop(indice_cel)
                    precioA.pop(indice_cel)
                    print("Su producto fue borrado con exito")
                else:
                    print("Ese producto no se encuentra en la lista")
            elif respuesta == 4 :
                print("Usted a elegido salir del programa")
                print("El programa va a cerrarse")
                break
