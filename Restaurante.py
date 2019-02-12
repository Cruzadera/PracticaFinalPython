# 1.	Crear un plato. Antes de crearlo, deben listarse todos los platos existentes (si los hubiera). No puede haber
# platos repetidos. 
# 2.	Eliminar un plato. Antes de eliminarlo, deben listarse todos los platos existentes (si los
# hubiera). 
# 3.	Dar de alta o baja a un usuario. 4.	Leer la lista de repartidores. 5.	Crear un pedido.

ruta_platos = "./platos.txt"
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


def configuracion_usuarios():
    pass


def listar_repartidores():
    pass


def crear_pedido():
    pass


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
        configuracion_usuarios()
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
