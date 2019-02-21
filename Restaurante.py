from datetime import datetime, timedelta, time

ruta_platos = "./platos.txt"
ruta_usuarios = "./usuarios.txt"
ruta_repartidores = "./repartidores.txt"
ruta_pedidos = "./pedidos.txt"
separador = '|'
espacio = ' '
separador_hora = ':'
intervalo = 15


def agregar_plato():
    correcto = False
    while not correcto:
        if num_platos() > 0:
            listar_platos()
        try:
            nombre_plato = input("Introduce el nombre del plato que desea añadir: \n")
            lista_ingredientes = input("Introduce los ingredientes que lleva este plato:\n")
            lista_alergenos = input("Introduce los alergenos que puede llevar este plato:\n")
            num_raciones = int(input("Introduce el número de raciones que se han preparado para este plato:\n"))
            precio = float(input("Introduce el precio del plato: \n"))
            # Pasamos los parametros numéricos a cadena
            num_raciones = str(num_raciones)
            precio = str(precio)
            fichero_escritura_platos = open(ruta_platos, 'a', encoding='utf8')
            # Creamos la linea que queremos añadir al fichero con el método join
            datos_plato = [nombre_plato, lista_ingredientes, lista_alergenos, num_raciones, precio]
            nuevo_plato = separador.join(datos_plato)
            fichero_escritura_platos.writelines(nuevo_plato + "\n")

            fichero_escritura_platos.close()
            print("El plato " + nombre_plato + " se ha añadido correctamente")
            correcto = True
        except (ValueError, TypeError):
            print("Error. El tipo tiene que ser numérico o no dependiendo de lo que se pide. Intételo de nuevo")
            correcto = False


def comprobar_plato(plato):
    comprobado = False
    fichero_lectura_usuarios = open(ruta_usuarios, 'r', encoding='utf8')
    lista_usuarios = fichero_lectura_usuarios.readlines()
    numlinea = 0

    for linea in lista_usuarios:
        numlinea += 1
        if plato == numlinea:
            comprobado = True

    fichero_lectura_usuarios.close()
    return comprobado


def eliminar_plato():
    correcto = False
    listar_platos()
    while not correcto:
        try:
            plato_borrar = int(input("Introduce el número del plato que deseas borrar: \n"))
            if comprobar_plato(plato_borrar):
                lineas_fichero_plato = open(ruta_platos, 'r', encoding='utf8').readlines()
                fichero_borrado_plato = open(ruta_platos, 'w', encoding='utf8')
                numlines = 0

                for linea in lineas_fichero_plato:
                    numlines += 1
                    if numlines != plato_borrar:
                        fichero_borrado_plato.write(linea)
                print("El plato número " + str(plato_borrar) + " se ha borrado correctamente.")
                fichero_borrado_plato.close()
                correcto = True
            else:
                print("Error. Por favor, introduce un número de plato existente.")
                correcto = False
        except ValueError:
            print("Error. Tiene que ser un valor numérico. Intételo de nuevo")
            correcto = False


def agregar_usuario():
    nombre_usuario = input("Introduce el nombre del usuario: \n")
    apellidos_usuario = input("Introduce los apellidos del usuario: \n")
    direccion_usuario = input("Introduce la direccion del usuario: \n")
    # Considero el número de teléfono como cadena porque se puede meter el prefijo de dicho número
    numero_usuario = input("Introduce un número de teléfono de contacto: \n")
    # Le ponemos el id autoincremental al usuario
    fichero_lectura_usuario = open(ruta_usuarios, 'r', encoding='utf8')
    lista_usuarios = fichero_lectura_usuario.readlines()
    if len(lista_usuarios) > 0:
        ultima_linea = lista_usuarios[len(lista_usuarios) - 1]
        posicion = ultima_linea.find(separador, 0)
        ultimo_id = ultima_linea[0:posicion]
        ultimo_id_num = int(ultimo_id)
        id_usuario = ultimo_id_num + 1
    else:
        id_usuario = 1
    # Convertimos el id a string
    id_usuario = str(id_usuario)
    fichero_escritura_usuario = open(ruta_usuarios, 'a', encoding='utf8')
    # Creamos la linea que queremos añadir al fichero con el método join
    datos_usuario = [id_usuario, nombre_usuario, apellidos_usuario, direccion_usuario, numero_usuario]
    nuevo_usuario = separador.join(datos_usuario)
    fichero_escritura_usuario.writelines(nuevo_usuario + "\n")

    fichero_lectura_usuario.close()
    fichero_escritura_usuario.close()
    print("El usuario " + nombre_usuario + " se ha añadido correctamente")


def listar_usuarios():
    fichero_lectura_usuarios = open(ruta_usuarios, 'r', encoding='utf8')
    lista_usuarios = fichero_lectura_usuarios.readlines()

    print("--------LISTA DE USUARIOS---------")
    for linea in lista_usuarios:
        id_user = linea.find(separador, 0)
        nombre = linea.find(separador, id_user + 1)
        apellido = linea.find(separador, nombre + 1)
        print(linea[0:id_user] + "\t" + linea[id_user + 1:nombre] + "\t" + linea[nombre + 1:apellido])

    fichero_lectura_usuarios.close()


def comprobar_usuario(id_usuario):
    comprobado = False
    fichero_lectura_usuarios = open(ruta_usuarios, 'r', encoding='utf8')
    lista_usuarios = fichero_lectura_usuarios.readlines()

    for linea in lista_usuarios:
        id_user = linea.find(separador, 0)
        if id_usuario == linea[0:id_user]:
            comprobado = True

    fichero_lectura_usuarios.close()
    return comprobado


def eliminar_usuario():
    correcto = False
    while not correcto:
        listar_usuarios()
        try:
            id_usuario_borrar = int(input("Introduce el número del usuario que deseas borrar: \n"))
            id_usuario_borrar = str(id_usuario_borrar)  # Lo pasamos a cadena para leer el fichero
            if comprobar_usuario(id_usuario_borrar):
                fichero_r_usuarios = open(ruta_usuarios, 'r', encoding='utf8').readlines()
                fichero_w_usuarios = open(ruta_usuarios, 'w', encoding='utf8')
                for linea in fichero_r_usuarios:
                    id_user = linea.find(separador, 0)
                    if id_usuario_borrar != linea[0:id_user]:
                        fichero_w_usuarios.write(linea)

                fichero_w_usuarios.close()
                print("El usuario " + id_usuario_borrar + " se ha borrado correctamente")
                correcto = True
            else:
                print("Error. Por favor, introduce un número de usuario existente.")
                correcto = False
        except ValueError:
            print("Error. Tiene que ser un valor numérico. Intételo de nuevo")
            correcto = False


def menu_usuarios():
    salir2 = False
    while not salir2:
        print("-------CONGIGURACIÓN DE USUARIOS--------")
        print("\n1. DAR DE ALTA A UN USUARIO.")
        print("2. DAR DE BAJA A UN USUARIO.")
        print("3. SALIR")

        try:
            opcion2 = int(input("Seleccione opción: "))

            if opcion2 == 1:
                agregar_usuario()
            elif opcion2 == 2:
                eliminar_usuario()
            elif opcion2 == 3:
                salir2 = True
            else:
                print("Elija una opción válida\n")
        except ValueError:
            print("Error. Tiene que ser un valor numérico. Intételo de nuevo")


def listar_repartidores():
    fichero_lectura_repartidores = open(ruta_repartidores, 'r', encoding='utf8')
    lista_repartidores = fichero_lectura_repartidores.readlines()

    print("--------LISTA DE REPARTIDORES---------")
    for linea in lista_repartidores:
        id_repartidor = linea.find(separador, 0)
        nombre = linea.find(separador, id_repartidor + 1)
        apellido = linea.find(separador, nombre + 1)
        print("{0:<3} {1:<10} {2:<20}".format(linea[0:id_repartidor], linea[id_repartidor + 1:nombre],
                                              linea[nombre + 1:apellido]))

    fichero_lectura_repartidores.close()


def comprobar_hora(repartos, hours, minutos):
    incremento_min = timedelta(minutes=intervalo)
    hora_pedido = timedelta(hours=hours, minutes=minutos)
    for reparto in repartos:
        if not reparto == '':
            formato_reparto = reparto.split(separador_hora)
            hours = int(formato_reparto[0])
            minus = int(formato_reparto[1])
            reparto_format = timedelta(hours=hours, minutes=minus)
            if hora_pedido == reparto_format:
                return False
            if ((hora_pedido + incremento_min) > reparto_format) and ((hora_pedido - incremento_min) < reparto_format):
                return False
    return True


def asignar_repartidor(hora_introducida):
    fichero_lectura_repartidores = open(ruta_repartidores, 'r', encoding='utf8')
    lista_repartidores = fichero_lectura_repartidores.readlines()
    fichero_escritura_repartidores = open(ruta_repartidores, 'w', encoding='utf8')
    asignado = False
    id_repartidor = 0

    for linea in lista_repartidores:
        pos_id = linea.find(separador, 0)
        pos_nombre = linea.find(separador, pos_id + 1)
        pos_apellido = linea.find(separador, pos_nombre + 1)
        pos_repartos = linea.find(separador, pos_apellido + 1)
        if not asignado:
            repartos = linea[pos_apellido + 1:pos_repartos].split(espacio)
            tiene_hora = True
            if len(repartos) > 1:  # Si tiene algún reparto asignado
                formato_hora = hora_introducida.split(separador_hora)
                hours = int(formato_hora[0])
                minutos = int(formato_hora[1])
                tiene_hora = comprobar_hora(repartos, hours, minutos)
            if tiene_hora:
                # Formateamos la hora introducida por el usuario en formato datetime
                hora_introducida2 = datetime.strptime(hora_introducida, '%H:%S')
                hora_formateada = datetime.strftime(hora_introducida2, '%H:%S')
                # Volvemos a convertir la cadena en string para pasarla a la lista de horas
                cadena_hora = str(hora_formateada)
                repartos.append(cadena_hora)
                repartos_cadena = espacio.join(repartos)
                repartidor = [linea[0:pos_id], linea[pos_id + 1: pos_nombre],
                              linea[pos_nombre + 1:pos_apellido], repartos_cadena]
                repartidor_ocupado = separador.join(repartidor)
                linea = repartidor_ocupado + "\n"
                asignado = True
                id_repartidor = repartidor[0]

        fichero_escritura_repartidores.write(linea)

    fichero_lectura_repartidores.close()
    fichero_escritura_repartidores.close()
    return id_repartidor


def calcular_total(platos):
    lineas_fichero_plato = open(ruta_platos, 'r', encoding='utf8').readlines()
    fichero_w_plato = open(ruta_platos, 'w', encoding='utf8')
    numlines = 0
    numplato = 0
    total = 0
    for linea in lineas_fichero_plato:
        numlines += 1
        pos_nombre = linea.find(separador, 0)
        pos_ingredientes = linea.find(separador, pos_nombre + 1)
        pos_alergenos = linea.find(separador, pos_ingredientes + 1)
        pos_raciones = linea.find(separador, pos_alergenos + 1)
        pos_precio = linea.find(separador, pos_raciones + 1)
        if numlines == int(platos[numplato]):
            total += float(linea[pos_raciones + 1:pos_precio])
            if numplato < len(platos) - 1:
                numplato += 1

        fichero_w_plato.write(linea)
    fichero_w_plato.close()
    return str(total)  # Convierto el total en cadena para que se escriba después en el fichero


def guardar_pedido(id_user, platos, id_repartidor, hora_introducida):
    total = calcular_total(platos)
    fichero_wr_pedido = open(ruta_pedidos, 'a', encoding='utf8')
    platos = espacio.join(platos)
    # Creamos la linea que queremos añadir al fichero con el método join
    datos_pedido = [id_user, platos, id_repartidor, total, hora_introducida]
    nuevo_pedido = separador.join(datos_pedido)
    fichero_wr_pedido.writelines(nuevo_pedido + "\n")
    fichero_wr_pedido.close()
    return datos_pedido


def crear_pedido():
    while True:
        try:
            print("---------CREACIÓN DEL PEDIDO----------")
            listar_usuarios()
            id_user = int(input("Indica tu id de usuario: "))
            id_user = str(id_user)
            listar_platos()
            platos_cadena = input("Introduce los números de platos (separados por espacios) que deseas añadir al "
                                  "pedido: ")
            platos = platos_cadena.split(espacio)
            # Ordenamos los números de los platos de menor a mayor
            platos = sorted(platos)
            # Comprobamos las raciones de los platos
            if comprobar_numraciones(platos):
                hora_introducida = input("¿A qué hora desea recibir la entrega? - ")
                id_repartidor = asignar_repartidor(hora_introducida)
                if id_repartidor != 0:
                    datos_pedido = guardar_pedido(id_user, platos, id_repartidor, hora_introducida)
                    print("Pedido realizado, su importe total es de: " + datos_pedido[3] + "€")
                else:
                    print("No hay repartidores disponibles en este momento. Intételo de nuevo más tarde.")
                break
        except TypeError:
            print("Error")


def comprobar_numraciones(platos):
    lineas_fichero_plato = open(ruta_platos, 'r', encoding='utf8').readlines()
    fichero_w_plato = open(ruta_platos, 'w', encoding='utf8')
    numlines = 0
    numplato = 0
    comprobado = False
    for linea in lineas_fichero_plato:
        numlines += 1
        pos_nombre = linea.find(separador, 0)
        pos_ingredientes = linea.find(separador, pos_nombre + 1)
        pos_alergenos = linea.find(separador, pos_ingredientes + 1)
        pos_raciones = linea.find(separador, pos_alergenos + 1)
        pos_precio = linea.find(separador, pos_raciones + 1)
        if numlines == int(platos[numplato]):
            if not int(linea[pos_alergenos + 1: pos_raciones]) == 0:
                racion = str(int(linea[pos_alergenos + 1:pos_raciones]) - 1)
                dish = [linea[0:pos_nombre], linea[pos_nombre + 1: pos_ingredientes],
                        linea[pos_ingredientes + 1:pos_alergenos], racion, linea[pos_raciones + 1: pos_precio]]
                decremento_racion_plato = separador.join(dish)
                linea = decremento_racion_plato + "\n"
                if numplato < len(platos) - 1:
                    numplato += 1
                comprobado = True
            else:
                print("Para el plato " + linea[0:pos_nombre] + " no hay más raciones disponibles. Inténtelo de nuevo.")
                comprobado = False
        fichero_w_plato.write(linea)
    fichero_w_plato.close()
    return comprobado


def listar_platos():
    fichero_lectura_platos = open(ruta_platos, 'r', encoding='utf8')
    lista_platos = fichero_lectura_platos.readlines()
    numlineas = 0

    print("--------PLATOS DE TAPAS CAMILO---------")
    for linea in lista_platos:
        numlineas += 1
        if linea.strip():  # Si la linea no está en blanco
            posicion = linea.find(separador, 0)  # Buscamos hasta que posicion llega el nombre del plato
            print(numlineas, linea[0:posicion])  # Mostramos el nombre del plato a través de la anotación slice

    fichero_lectura_platos.close()


def num_platos():
    fichero_lectura_platos = open(ruta_platos, 'r', encoding='utf8')
    lista_platos = fichero_lectura_platos.readlines()
    numlineas = 0

    for linea in lista_platos:
        numlineas += 1

    fichero_lectura_platos.close()
    return numlineas


def menu_opciones():
    salir = False
    while not salir:
        print("----------------------------------------")
        print("       RESTAURANTE TAPAS CAMILO")
        print("________________________________________")
        print("\n1. CREAR UN PLATO.")
        print("2. ELIMINAR UN PLATO.")
        print("3. CONFIGURACIÓN DE USUARIOS.")
        print("4. LISTA DE REPARTIDORES.")
        print("5. CREAR UN PEDIDO")
        print("6. SALIR")

        try:
            opcion = int(input("Seleccione opción: "))
            if opcion == 1:
                agregar_plato()
            elif opcion == 2:
                eliminar_plato()
            elif opcion == 3:
                menu_usuarios()
            elif opcion == 4:
                listar_repartidores()
            elif opcion == 5:
                crear_pedido()
            elif opcion == 6:
                salir = True
            else:
                print("Elija una opción válida\n")
        except TypeError:
            print("Error. Tiene que ser un valor numérico. Intételo de nuevo")


# MAIN
menu_opciones()
