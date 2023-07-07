reservas = {}

print("Bienvenido al sistema de Clínica Deportiva")
usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

if usuario == "admin" and contrasena == "123":
    print("Inicio de sesión exitoso. Accediendo al menú principal…")
    opcion = ""
    while opcion != "4":
        print("----- Menú Principal -----")
        print("1. Módulo de reservas")
        print("2. Módulo de facturación")
        print("3. Módulo de informes")
        print("4. Salir")
        opcion = input("Ingrese el número de opción deseada: ")

        if opcion == "1":
            print("Opción seleccionada: Módulo de reservas")

            horarios = ["8:00", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30"]

            personas = ["Ana", "Carlos", "Diego", "Elena"]

            
            disciplinas = ["Fútbol", "Natación", "Atletismo", "Tenis"]

            
            servicios = ["Terapia física", "Programa de recuperación"]

            
            numero_reserva = 0

            # Crear un ciclo para solicitar los datos de la reserva
            continuar = "s"
            while continuar == "s":
                # Solicitar la cantidad de personas
                cantidad = int(input("Ingrese la cantidad de personas que desea reservar: "))
                # Validar que la cantidad sea menor o igual a 4
                if cantidad <= 4:
                    # Solicitar la disciplina deportiva
                    disciplina = input("Ingrese la disciplina deportiva que practica: ")
                    # Validar que la disciplina sea válida
                    if disciplina in disciplinas:
                        # Solicitar el horario deseado
                        horario = input("Ingrese el horario en el que desea reservar (HH:MM): ")
                        # Validar que el horario sea válido
                        if horario in horarios:
                            # Contar cuántas personas solicitan terapia física
                            terapia = 0
                            servicio_valido = True # Variable para indicar si el servicio es válido o no
                            for i in range(cantidad):
                                servicio = input(f"Ingrese el servicio que desea la persona {i+1} (Terapia física o Programa de recuperación): ")
                                # Validar que el servicio sea válido
                                if servicio in servicios:
                                    # Si el servicio es terapia física, aumentar el contador
                                    if servicio == "Terapia física":
                                        terapia += 1
                                else:
                                    print("Servicio no válido. Inténtelo nuevamente.")
                                    servicio_valido = False # Cambiar el valor de la variable a False
                                    break # Salir del ciclo for

                            # Si el servicio no es válido, volver al inicio del ciclo while
                            if not servicio_valido:
                                continue

                            # Validar que el número de terapias sea menor o igual a 3
                            if terapia <= 3:
                                # Asignar una persona que atienda según el servicio solicitado
                                if terapia == 0:
                                    # Si nadie solicita terapia física, asignar a Elena
                                    persona = "Elena"
                                elif terapia == cantidad:
                                    # Si todos solicitan terapia física, asignar a Ana, Carlos o Diego según el orden de la lista
                                    indice = numero_reserva % 3 # Obtener el índice usando el módulo del número de reserva entre 3
                                    persona = personas[indice] # Asignar la persona correspondiente al índice
                                else:
                                    # Si hay una mezcla de servicios, asignar a Ana, Carlos o Diego según la disponibilidad
                                    # Crear una variable para indicar si hay una persona disponible
                                    hay_disponible = False
                                    for p in personas[:3]: # Recorrer las primeras tres personas de la lista
                                        if p not in reservas.get(horario, []): # Verificar si la persona no está en el diccionario de reservas para ese horario
                                            persona = p # Asignar la persona disponible
                                            hay_disponible = True # Cambiar el valor de la variable a True
                                            break # Salir del ciclo for

                                    # Si no hay ninguna persona disponible, mostrar un mensaje y volver al inicio del ciclo while
                                    if not hay_disponible:
                                        print("No hay personas disponibles para ese horario. Inténtelo nuevamente.")
                                        continue

                                # Aumentar el número de reservación en uno
                                numero_reserva += 1

                                # Mostrar los datos de la reservación
                                print(f"Su reservación ha sido exitosa. Estos son los datos de su reservación:")
                                print(f"Número de reservación: {numero_reserva}")
                                print(f"Cantidad de personas: {cantidad}")
                                print(f"Disciplina deportiva: {disciplina}")
                                print(f"Horario: {horario}")
                                print(f"Persona que atiende: {persona}")

                                # Guardar los datos de la reservación en un diccionario
                                reserva = {
                                    "numero": numero_reserva,
                                    "cantidad": cantidad,
                                    "disciplina": disciplina,
                                    "horario": horario,
                                    "persona": persona
                                }

                                # Agregar la reservación al diccionario de reservas
                                if horario not in reservas: # Si el horario no está en el diccionario, crear una lista vacía
                                    reservas[horario] = []
                                reservas[horario].append(reserva) # Agregar la reservación a la lista correspondiente al horario

                            else:
                                print("El máximo de terapias por espacio de reserva es de 3 personas. Inténtelo nuevamente.")
                        else:
                            print("Horario no válido. Inténtelo nuevamente.")
                    else:
                        print("Disciplina no válida. Inténtelo nuevamente.")
                else:
                    print("La capacidad máxima de la clínica es de 4 personas. Inténtelo nuevamente.")

                # Preguntar si desea continuar con otra reserva
                continuar = input("¿Desea realizar otra reserva? (s/n): ")
                # Validar que la respuesta sea s o n

                while continuar not in ["s", "n"]:
                    print("Respuesta no válida. Por favor, ingrese s o n.")
                    continuar = input("¿Desea realizar otra reserva? (s/n): ")

        elif opcion == "2":
            # Módulo de facturación
print("Módulo de facturación")
nombre_cliente = input("Ingrese el nombre del cliente: ")
num_identificacion = input("Ingrese el número de identificación del cliente: ")
num_reservacion = input("Ingrese el número de reservación: ")

# Buscar la reservación
reservacion_encontrada = False
for reservacion in reservas:
    if reservacion['num_reservacion'] == num_reservacion:
        reservacion_encontrada = True
        # Crear la factura
        factura = f"""
        Factura creada:
        Nombre del cliente: {nombre_cliente}
        Número de identificación: {num_identificacion}
        Número de reservación: {num_reservacion}
        Datos de atención: {reservacion['datos_atencion']}
        Datos del atleta: {reservacion['datos_atleta']}
        Datos de la reserva: {reservacion['datos_reserva']}
        Monto: 0 (La atención en la clínica es gratuita para los atletas)
        """
        print(factura)
        break

if not reservacion_encontrada:
    print("No se encontró la reservación con el número proporcionado")

            print("Opción seleccionada: Módulo de facturación")
            # Código del módulo de facturación
            # ...

        elif opcion == "3":
            print("Opción seleccionada: Módulo de informes")
            # Código del módulo de informes
            # ...

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
else:
    print("Inicio de sesión fallido. Inténtelo nuevamente.")
