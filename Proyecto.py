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

            continuar = "s"
            while continuar == "s":
                cantidad = int(input("Ingrese la cantidad de personas que desea reservar: "))

                if cantidad > 4:
                    print("La capacidad máxima de la clínica es de 4 personas. Inténtelo nuevamente.")
                    continue

                disciplina = input("Ingrese la disciplina deportiva que practica: ")

                if disciplina not in disciplinas:
                    print("Disciplina no válida. Inténtelo nuevamente.")
                    continue

                horario = input("Ingrese el horario en el que desea reservar (HH:MM): ")

                if horario not in horarios:
                    print("Horario no válido. Inténtelo nuevamente.")
                    continue

                terapia = 0
                for i in range(cantidad):
                    servicio = input(f"Ingrese el servicio que desea la persona {i+1} (Terapia física o Programa de recuperación): ")
                    if servicio not in servicios:
                        print("Servicio no válido. Inténtelo nuevamente.")
                        break
                    if servicio == "Terapia física":
                        terapia += 1

                if terapia > 3:
                    print("El máximo de terapias por espacio de reserva es de 3 personas. Inténtelo nuevamente.")
                    continue

                if terapia == 0:
                    persona = "Elena"
                elif terapia == cantidad:
                    indice = numero_reserva % 3
                    persona = personas[indice]
                else:
                    hay_disponible = False
                    for p in personas[:3]:
                        if p not in reservas.get(horario, []):
                            persona = p
                            hay_disponible = True
                            break
                    if not hay_disponible:
                        print("No hay personas disponibles para ese horario. Inténtelo nuevamente.")
                        continue

                numero_reserva += 1

                print("Su reservación ha sido exitosa. Estos son los datos de su reservación:")
                print(f"Número de reservación: {numero_reserva}")
                print(f"Cantidad de personas: {cantidad}")
                print(f"Disciplina deportiva: {disciplina}")
                print(f"Horario: {horario}")
                print(f"Persona que atiende: {persona}")

                reserva = {
                    "numero": numero_reserva,
                    "cantidad": cantidad,
                    "disciplina": disciplina,
                    "horario": horario,
                    "persona": persona
                }

                if horario not in reservas:
                    reservas[horario] = []
                reservas[horario].append(reserva)

                continuar = input("¿Desea realizar otra reserva? (s/n): ")

                while continuar not in ["s", "n"]:
                    print("Respuesta no válida. Por favor, ingrese s o n.")
                    continuar = input("¿Desea realizar otra reserva? (s/n): ")

        elif opcion == "2":
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
