# =============================================================
# Tema 02 · Condicionales y menú con while · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo a tu repositorio practicas-python como:
#        tema-02.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Ejecuta el archivo y prueba cada caso (los que se cumplen
#      y los que no).
#   4. Súbelo a GitHub con el commit:
#        feat: ejercicios del tema 02
#
# Nombre completo: JHAN CARLOS MUÑOZ VARGAS
# Mi app se llama: PRESTAYA
# =============================================================

# -------------------------------------------------------------
# EJERCICIO 1 · ¿Alcanza el dinero?
# -------------------------------------------------------------
# Pregunta con input() cuánto dinero tiene el usuario y cuánto
# cuesta lo que quiere comprar.
#   - Si le alcanza: muestra cuánto le sobra.
#   - Si no: muestra cuánto le falta.
#
# Así debe verse (si escribe 20000 y 26500):
#   Te faltan $6,500

# Tu código aquí:

print("----------------- EJERCICIO 1 -----------------")
tiene = int(input("Cuanto dinero tienes:"))
cuesta = int(input("Cuanto cuesta lo que vas a comprar:"))
falta = cuesta-tiene
quedan = tiene-cuesta

if tiene>cuesta:
    print(f"*****Perfecto si te alcanza, y te quedan ${quedan:,.0f}*****")
else:
    print(f"*****Que mal no te alcanza, te faltan ${falta:,.0f}*****")
print("----------------------------------------------------")
print()

# -------------------------------------------------------------
# EJERCICIO 2 · El nivel del usuario
# -------------------------------------------------------------
# Una app de ejercicio clasifica al usuario según los minutos que
# entrenó en la semana. Pregunta los minutos y muestra el nivel:
#   - 0 minutos:            "Sin actividad: ¡empieza hoy!"
#   - de 1 a 149 minutos:   "Nivel principiante"
#   - de 150 a 299 minutos: "Nivel activo"
#   - 300 o más:            "Nivel atleta"
#
# Usa if, elif y else. Prueba los cuatro casos.

# Tu código aquí:

print("----------------- EJERCICIO 2 -----------------")
tiempo = int(input("Cuanto tiempo entrenaste esta semana en minutos:"))

if tiempo == 0:
    print("Sin actividad: ¡empieza hoy!")
elif tiempo > 0 and tiempo < 150:
    print("Nivel principiante")
elif tiempo > 149 and tiempo < 300:
    print("Nivel activo")
else:
    print("Nivel atleta")
print("----------------------------------------------------")
print()

# -------------------------------------------------------------
# EJERCICIO 3 · ¿Se puede agendar la cita?
# -------------------------------------------------------------
# Una barbería atiende de 8 a 19 horas, de lunes a sábado.
# Pregunta el día (en minúsculas) y la hora (número entero).
#   - Si es domingo:                 "Los domingos no atendemos"
#   - Si la hora está fuera de 8–19: "Fuera del horario de atención"
#   - Si todo está bien:             "Cita disponible"
#
# Usa and / or en al menos una condición.
#
# Pista: si el usuario escribe "Domingo" con mayúscula, tu if no lo
# reconoce. Prueba:  dia = input("Día: ").lower()
# .lower() convierte el texto a minúsculas (.upper() a mayúsculas).

# Tu código aquí:

print("----------------- EJERCICIO 3 -----------------")
dia = input("Que dia quieres agendar la cita:").lower()
hora = int(input("A que hora quieres agendar la cita:"))

if dia == "domingo":
    print("Los domingos no atendemos")
elif hora < 8 or hora > 19:
    print("Fuera del horario de atención")
else:
    print("Cita disponible")

print("----------------------------------------------------")
print()

# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error
# -------------------------------------------------------------
# Este código tiene 3 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   clave = input("Clave: ")
#   if clave = "1234"
#   print("Bienvenido")
#   else:
#       print("Clave incorrecta")

# Tu código corregido aquí:

print("----------------- EJERCICIO 4 -----------------")
clave = input("Clave: ")
if clave == "1234":
    print("Bienvenido")
else:
    print("Clave incorrecta")


# Error 1: Se usa = en lugar de == para comparación
# Error 2: Falta dos puntos después del if
# Error 3: Falta indentación en los bloques de código


# -------------------------------------------------------------
# EJERCICIO 5 · Caja registradora con menú
# -------------------------------------------------------------
# Haz un menú con while que se repita hasta que el usuario elija
# salir:
#   1. Agregar un producto (pregunta el precio y súmalo al total)
#   2. Ver el total
#   3. Salir
#
# Si escribe una opción que no existe, muestra "Opción no válida".
# Pista: crea total = 0 antes del while y en la opción 1 haz
#        total = total + precio
#
# Así debe verse:
#   1. Agregar producto  2. Ver total  3. Salir
#   Opción: 1
#   Precio: 4500
#   Opción: 1
#   Precio: 2000
#   Opción: 2
#   Total: $6,500

# Tu código aquí:
print("----------------- EJERCICIO 5 -----------------")
total = 0
while True:
    print("1. Agregar producto  2. Ver total  3. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        precio = float(input("Precio: "))
        total += precio
    elif opcion == "2":
        print(f"Total: ${total:,.0f}")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Escribe 1, 2 o 3.")
print("----------------------------------------------------")
print()


# =============================================================
# EJERCICIO 6 · LLÉVALO A TU APP  (va en src/app.py de tu app, no aquí)
# =============================================================
# Tu app ya saluda (tema 01). Hoy le das un MENÚ. En el archivo
# src/app.py de tu app:
#   1. Deja la bienvenida al inicio.
#   2. Agrega un menú con while con al menos 3 opciones
#      que tengan sentido para tu app, más "Salir".
#   3. Cada opción hace algo (aunque sea sencillo): preguntar un
#      dato, calcular algo o mostrar un mensaje.
#   4. Al menos una opción valida un dato con if
#      (por ejemplo: que un número no sea negativo).
#   5. Si eligen una opción que no existe: "Opción no válida".
#
# Ejemplo para una app de citas de barbería:
#   ===== BARBERÍA EL CORTE =====
#   1. Ver precios
#   2. Agendar cita
#   3. Calcular total de cortes
#   4. Salir
#
# Con esto tu app ya se ve como una app de verdad. En el próximo
# tema guardamos varias citas, productos o registros en listas.
# =============================================================