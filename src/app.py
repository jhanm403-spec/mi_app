#aqui empieza mi app
print ("======================================================")
print ("======       BIENVENIDO A PRESTAYA        ============")
print ("======================================================")
print ("** Esta app te permite llevar un control de tus prestamos **")
print ("** Todos los prestamos son al (10%) de interes mensual, no importa la cantidad de cuotas  **")
print ("** Debes diligenciar todos los campos para poder continuar **")
print ()
# =============================================================
# EJERCICIO 7 · LLÉVALO A TU APP  (va en src/app.py de tu app, no aquí)
# =============================================================
# Tu app ya tiene un menú (tema 02). Hoy aprende a GUARDAR
# varios registros mientras está abierta:
#   1. Crea una lista vacía antes del menú. Ejemplos: citas = [],
#      productos = [], metas = [], tareas = [].
#   2. Agrega la opción "Agregar ...": pregunta el dato y haz append.
#   3. Agrega la opción "Ver ...": muéstralos con un for, numerados.
#      Si la lista está vacía, muestra "Todavía no hay registros".
#   4. Muestra cuántos registros hay con len().
#
# Ejemplo para una app de citas de barbería:
#   1. Agendar cita
#   2. Ver citas
#   3. Salir
#   Opción: 2
#   1. Carlos - 10:00
#   2. Valentina - 11:30
#   Total de citas: 2
#
# Pista para numerar: for i in range(len(citas)):
#                         print(f"{i + 1}. {citas[i]}")
#
# OJO: cuando cierras la app, la lista se borra. Guardar en un
# archivo es un tema más adelante.
# =============================================================
prestamos = []
while True:
    print("======================= MENU =========================")
    print("1. Agregar prestamo")
    print("2. Total interes a pagar")
    print("3. Valor total de cuotas")
    print("4. Valor total a pagar")
    print("5. Ver prestamos")
    print("6. Salir")
    opcion = input("Elige una Opción: ")
    print("======================================================")
    print()
    if opcion == "1":
            nombre = input("¿Cómo te llamas?: ")
            cedula = input("¿Cuál es tu número de cédula?: ")
            celular = input("¿Cuál es tu número de celular?: ")
            direccion = input("¿Cuál es tu dirección?: ")
            prestamo = int(input("¿Cuánto dinero quieres prestar?: "))
            meses = int(input("¿En cuántos meses quieres pagar?: "))
            cuotas = int(input("¿En cuántas cuotas quieres pagar?: "))
            print()
            interes = prestamo * 0.10 
            totalInteres = interes * meses
            totalAPagar = prestamo + totalInteres
            totalCuotas = totalAPagar / cuotas
            print()
            print("======================================================")
            print("==========      DATOS DEL PRESTAMO      ==============")
            print(f"======= Nombre:      {nombre}")
            print(f"======= Cédula:      {cedula}")
            print(f"======= Celular:     {celular}")
            print(f"======= Dirección:   {direccion}")
            print(f"======= Préstamo:    ${prestamo:,.0f}")
            print(f"======= Meses:       {meses}")
            print(f"======= Cuotas:      {cuotas}")
            print("======================================================")
            print()
            nuevo_prestamo = input("Ingrese el nombre del prestamo: ")
            prestamos.append(nuevo_prestamo)
            print(f"Prestamo '{nuevo_prestamo}' agregado correctamente.")
            print()
    elif opcion == "2":
        print(f"Hola {nombre}, el total de intereses a pagar es: ${totalInteres:,.0f}")
        print()
    elif opcion == "3":
        print(f"Hola {nombre}, el total de cuotas a pagar es: ${totalCuotas:,.0f}")
        print()
    elif opcion == "4":
        print(f"Hola {nombre}, el total a pagar es: ${totalAPagar:,.0f}")
        print()
    elif opcion == "5":
        if prestamos:
            print("Prestamos registrados:")
            for i, prestamo in enumerate(prestamos, start=1):
                print(f"{i}. {prestamo}")
                print(f"total de prestamos: {len(prestamos)}")
        else:
            print("Todavía no hay prestamos registrados.")
        print()
    elif opcion == "6":
        print("¡Hasta luego!")
        print()
        break
    else:
        print("Opción no válida. Escribe 1, 2, 3 o 4.")
        print()
print("----------------------------------------------------")
print()
# print(f"Hola {nombre}, tu préstamo de ${prestamo:,.0f} con un interés del 10% es de ${interes:,.0f}.")
# print(f"Por lo tanto, el total a pagar en {meses} meses es de ${totalInteres:,.0f}. solo interes")
# print(f"El total a pagar es: ${totalAPagar:,.0f} en {cuotas} cuotas.")
# print(f"Cada cuota será de: ${totalCuotas:,.0f}.")