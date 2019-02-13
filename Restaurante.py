# 1.	Crear un plato. Antes de crearlo, deben listarse todos los platos existentes (si los hubiera). No puede haber
# platos repetidos. 
# 2.	Eliminar un plato. Antes de eliminarlo, deben listarse todos los platos existentes (si los
# hubiera). 
# 3.	Dar de alta o baja a un usuario. 4.	Leer la lista de repartidores. 5.	Crear un pedido.

ruta_platos = "./platos.txt"
ruta_usuarios = "./usuarios.txt"
ruta_repartidores = "./repartidores.txt"
ruta_pedidos = "./pedidos.txt"
separador = '|'


def agregar_plato():
    # TODO: Hay que controlarlo mendiante excepciones
    nombre_plato = input("Introduce el nombre del plato que desea añadir: \n")
    lista_ingredientes = input("Introduce los ingredientes que lleva este plato:\n")
    lista_alergenos = input("Introduce los alergenos que puede llevar este plato:\n")
    num_raciones = input("Introduce el número de raciones que se han preparado para este plato:\n")

    fichero_escritura_platos = open(ruta_platos, 'a', encoding='utf8')
    # Creamos la linea que queremos añadir al fichero con el método join
    datos_plato = [nombre_plato, lista_ingredientes, lista_alergenos, num_raciones]
    nuevo_plato = separador.join(datos_plato)
    fichero_escritura_platos.writelines(nuevo_plato + "\n")

    fichero_escritura_platos.close()
    print("El plato " + nombre_plato + " se ha añadido correctamente")


def eliminar_plato():
    listar_platos()
    # TODO: Controlar que sea un número
    linea_borrar = int(input("Introduce el número del plato que deseas borrar: \n"))
    lineas_fichero_plato = open(ruta_platos, 'r', encoding='utf8').readlines()
    fichero_borrado_plato = open(ruta_platos, 'w', encoding='utf8')
    numlines = 0

    for linea in lineas_fichero_plato:
        numlines += 1
        if numlines != linea_borrar:
            fichero_borrado_plato.write(linea)
    print("El plato número " + str(linea_borrar) + " se ha borrado correctamente.")
    fichero_borrado_plato.close()


def agregar_usuario():
    nombre_usuario = input("Introduce el nombre del usuario: \n")
    apellidos_usuario = input("Introduce los apellidos del usuario: \n")
    direccion_usuario = input("Introduce la direccion del usuario: \n")
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


def eliminar_usuario():
    listar_usuarios()
    # TODO: CONTROLAR LAS EXCEPCIONES DE ENTRADA DE PARÁMETROS
    id_usuario_borrar = input("Introduce el número del usuario que deseas borrar: \n")
    fichero_r_usuarios = open(ruta_usuarios, 'r', encoding='utf8').readlines()
    fichero_w_usuarios = open(ruta_usuarios, 'w', encoding='utf8')
    for linea in fichero_r_usuarios:
        id_user = linea.find(separador, 0)
        if id_usuario_borrar != linea[0:id_user]:
            fichero_w_usuarios.write(linea)

    fichero_w_usuarios.close()
    print("El usuario " + id_usuario_borrar + " se ha borrado correctamente")



def menu_usuarios():
    salir2 = False
    print("-------CONGIGURACIÓN DE USUARIOS--------")
    print("\n1. DAR DE ALTA A UN USUARIO.")
    print("2. DAR DE BAJA A UN USUARIO.")
    print("3. SALIR")

    opcion2 = int(input("Seleccione opción:\n"))

    if opcion2 == 1:
        agregar_usuario()
    elif opcion2 == 2:
        eliminar_usuario()
    elif opcion2 == 3:
        salir2 = True
    else:
        print("Elija una opción válida\n")

    return salir2


def listar_repartidores():
    fichero_lectura_repartidores = open(ruta_repartidores, 'r', encoding='utf8')
    lista_repartidores = fichero_lectura_repartidores.readlines()

    print("--------LISTA DE REPARTIDORES---------")
    for linea in lista_repartidores:
        id_repartidor = linea.find(separador, 0)
        nombre = linea.find(separador, id_repartidor + 1)
        apellido = linea.find(separador, nombre + 1)
        print("{0:<3} {1:<10} {2:<20}" .format(linea[0:id_repartidor], linea[id_repartidor + 1:nombre], linea[nombre + 1:apellido]))

    fichero_lectura_repartidores.close()

def crear_pedido():



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


def menu_opciones():
    salir = False
    print("----------------------------------------")
    print("       RESTAURANTE TAPAS CAMILO")
    print("________________________________________")
    print("\n1. CREAR UN PLATO.")
    print("2. ELIMINAR UN PLATO.")
    print("3. CONFIGURACIÓN DE USUARIOS.")
    print("4. LISTA DE REPARTIDORES.")
    print("5. CREAR UN PEDIDO")
    print("6. SALIR")

    opcion = int(input("Seleccione opción:\n"))

    if opcion == 1:
        listar_platos()
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

    return salir


while True:
    salir = menu_opciones()
    if salir:
        break
