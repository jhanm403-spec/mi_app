#============================================================
#===== JHAN CARLOS MUÑOZ VARGAS - TECNICO EN SITEMAS ========
#=====              ADSO - 3505803                   ========
#============================================================

# =============================================================
# Tema 01 · Variables, tipos, entrada y salida · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo al repositorio de TU app como:
#        ejercicios/tema-01.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Ejecuta el archivo y prueba que todo funcione.
#   4. Súbelo a GitHub con el commit:
#        feat: tema 01 y bienvenida de la app
#
# Nombre completo: JHAN CARLOS MUÑOZ VARGAS
# Mi app se llama: PRESTAYA
# =============================================================


# -------------------------------------------------------------
# EJERCICIO 1 · Tarjeta de presentación
# -------------------------------------------------------------
# Crea tres variables: tu nombre (texto), tu edad (entero) y tu
# estatura en metros (decimal). Muestra las tres con UN solo print
# usando f-string.
#
# Así debe verse:
#   Soy Ana, tengo 19 años y mido 1.62 m.

# Tu código aquí:

print ("===================EJERCICIO 1=========================")
print ()
nombre = input("Nombre: ")
edad = int(input("Edad: "))
estatura = float(input("Estatura: "))

print(f"Soy {nombre}, tengo {edad} años y mido {estatura}")
print ("=======================================================")
print ()

# -------------------------------------------------------------
# EJERCICIO 2 · ¿De qué tipo es?
# -------------------------------------------------------------
# Crea estas cuatro variables y muestra el tipo de cada una con type():
#   a = "100"
#   b = 100
#   c = 100.0
#   d = "cien"
#
# Después, en un comentario, responde: ¿por qué "100" y 100 no son
# lo mismo para Python?

# Tu código aquí:
print ("=====================================EJERCICIO 2================================================")
print()
a = "100"
b = 100
c = 100.0
d = "cien"
print ('- Si le asigno un valor a una variable de esta forma ("100") el tipo de dato es:'), print(type(a))
print ('- Si le asigno un valor a una variable de esta forma (100) el tipo de dato es:'), print(type(b))
print ('- Si le asigno un valor a una variable de esta forma (100.0) el tipo de dato es:'), print(type(c))
print ('- Si le asigno un valor a una variable de esta forma ("cien") el tipo de dato es:'), print(type(d))
print ("==================================================================================================")
print ()


# Respuesta: toda asiganacion hecha con comillas las va a detectar como string asi tenga numeros, y las que estan sin comillas las detecta como entero y y float las que tengan su debido puntuacion de decimal.


# -------------------------------------------------------------
# EJERCICIO 3 · La cuenta del almuerzo
# -------------------------------------------------------------
# Pregunta con input():
#   - el valor de la cuenta
#   - cuántas personas van a pagar
#   - el porcentaje de propina (por ejemplo 10)
#
# Muestra: el valor de la propina, el total con propina y cuánto
# paga cada persona. Los valores en pesos, con separador de miles.
#
# Así debe verse (si escriben 85000, 3 y 10):
#   Propina:          $8,500
#   Total:            $93,500
#   Cada uno paga:    $31,167

# Tu código aquí:
print ("=====================================EJERCICIO 3================================================")
print()
cuenta = int(input("Valor de la cuenta: "))
personas = int(input("Número de personas: "))
propina = int(input("Porcentaje de propina: "))

porcentajePropina = propina / 100
valorPropina = cuenta * porcentajePropina
totalCuenta = cuenta + valorPropina
cadaPersona = totalCuenta / personas
print ()
print (f"Propina:            ${valorPropina:,.0f}")
print (f"Total:              ${totalCuenta:,.0f}")
print (f"Cada uno paga:      ${cadaPersona:,.0f}")
print ("==================================================================================================")
print ()

# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error
# -------------------------------------------------------------
# Este código tiene 2 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   precio = input("Precio del producto: ")
#   unidades = input("Unidades: ")
#   print("Total a pagar: " + precio * unidades)

# Tu código corregido aquí:
print ("=====================================EJERCICIO 4================================================")
print()
precio = int(input("Precio del producto: "))
unidades = int(input("Unidades: "))
totalPrecio = precio * unidades
print(f"Total a pagar:  ${totalPrecio:,.0f}")
print ("==================================================================================================")
print ()

# Error 1: no se utiliza + en el print no se puede concatenar
# Error 2: la multiplicacion se puede hacer con string se debe asignar el tipo de variable entero en el input


# -------------------------------------------------------------
# EJERCICIO 5 · Inventario rápido
# -------------------------------------------------------------
# Pregunta el nombre de un producto, cuántas unidades hay y el
# precio de cada unidad. Muestra un resumen como este:
#
#   ===== INVENTARIO =====
#   Producto:   Tabla de pino
#   Unidades:   40
#   Precio:     $18,000
#   Valor total: $720,000
#   ======================

# Tu código aquí:
producto = input("Ingresa Producto: ")
unidades = int(input("Cantidad: "))
precio = int(input("Precio: "))
valorTotal = precio * unidades
print ()
print ("========== INVENTARIO ==========")
print (f"Producto:      {producto}")
print (f"Unidades:      {unidades}")
print (f"Precio:       ${precio:,.0f}")
print (f"Valor total:  ${valorTotal:,.0f}")
print ("=================================")
print ("==================================================================================================")
print ()

# =============================================================
# EJERCICIO 6 · LLÉVALO A TU APP  (va en tu app.py, no aquí)
# =============================================================
# En el archivo app.py de tu proyecto, crea la pantalla de bienvenida
# de tu app. Debe:
#   1. Mostrar el nombre de tu app con un encabezado visible.
#   2. Preguntarle al usuario al menos 2 datos con input()
#      (por ejemplo: su nombre y algo que tenga sentido en tu app).
#   3. Responder con un mensaje que use esos datos (f-string).
#   4. Al menos un dato debe ser un número con el que hagas una cuenta.
#
# Ejemplo para una app de citas de barbería:
#   ==============================
#        BARBERÍA EL CORTE
#   ==============================
#   ¿Cómo te llamas? Carlos
#   ¿Cuántos cortes quieres agendar? 2
#   Hola Carlos, tus 2 cortes cuestan $50,000.
#
# Este es el primer paso de tu app: en los próximos temas le
# agregamos el menú, las listas y todo lo demás.
# =============================================================
