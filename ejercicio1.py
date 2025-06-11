""" 
Ejercicio 1: Conversor de Temperatura 
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit
"""
celsius = float(input("Por favor, ingrese una temperatura de grados Celsius"))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")


"""
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
"""
monto = 35.95
monto_total = monto + (monto * 0.15) 
print(f"El total a pagar es: {monto_total}")

"""
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no
"""
edad = int(input("Por favor, ingrese su edad"))
if edad >= 18: 
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

"""
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario
"""
palabra = input("Por favor, escriba una palabra: ")
vocales = "aeiouAEIOU"
contador = 0 

for letra in palabra:
  if letra in vocales:
    contador += 1

print(f"La palabra {palabra} tiene {contador} vocales")

"""
Ejercicio 5: Suma de números pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100
"""
suma = 0
for num in range(1, 101):
  if num % 2 == 0:
    suma += num

print(f"La suma de los números pares del 1 al 100 es {suma}")

"""
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)
"""
palabra = input("Por favor, ingrese una palabra: ")

palabra_limpia = palabra.replace(" ", "").lower()

if palabra_limpia == palabra_limpia[::-1]:
  print(f"La palabra {palabra} es un palíndromo")
else:
  print(f"La palabra {palabra} no es un palíndromo")

"""
Ejercicio 7: Calculadora simple
Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario
"""
print("Operaciones disponibles: ")
print("1. Suma ")
print("2. Resta ")
print("3. Multiplicación ")
print("4. División")

opcion = input("Por favor, elija una operación (1, 2, 3 o 4)").strip()

num1 = float(input("Por favor, introduce el primer número: "))
num2 = float(input("Por favor, introduce el segundo número: "))

if opcion == "1":
  resultado = num1 + num2
  print(f"Resultado: {num1} + {num2} = {resultado}")
elif opcion == "2":
  resultado = num1 - num2
  print(f"Resultado: {num1} - {num2} = {resultado}")
elif opcion == "3":
  resultado = num1 * num2
  print(f"Resultado: {num1} * {num2} = {resultado}")
elif opcion == "4":
  if num2 != 0:
    resultado = num1 / num2
    print(f"Resultado: {num1} / {num2} = {resultado}")
  else:
    print(f"Error. No se puede dividir entre cero")
else:
  print("Operación inválida. Por favor, elige 1, 2, 3 o 4")

"""
Ejercicio 8: Cálculo del índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona
"""
peso = float(input("por favor, introduce tu peso en kilogramos: "))
altura = float(input("por favor, introduce tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Su Índice de Masa Corporal es de: {imc}")

"""
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 
1 dólar es igual a 0.85 euros
"""
dolares = 1

euros = dolares * 0.85

print(f"{dolares} dolares son {euros} euros")

"""
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un 
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
"""
numero = int(input("Por favor, ingrese un número del 1 al 7: "))
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

if 1 <= numero <= 7:
  dia = dias[numero - 1]
  print(f"El día número {numero} es {dia}")
else:
  print("Número no válido. Por favor, ingrese un número del 1 al 7.")


"""
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
"""
año_nacimiento = int(input("Por favor, ingrese su año de nacimiento"))
edad_actual = 2025 - año_nacimiento
print(f"Tu edad actual es de {edad_actual} años")

"""
Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.
"""
longitud = float(input("Por favor, ingrese la longitud del rectángulo en centímetros: "))
ancho = float(input("Por favor, ingrese el ancho del rectángulo en centímetros"))

area = longitud * ancho

print(f"El área del rectángulo con la longitud {longitud} y el ancho {ancho} es de {area} centímetros cuadrados")

"""
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo 
o no.
"""
numero = int(input("Por favor, introduzca un número entero: "))
if numero <= 1:
  print(f"El número {numero} no es primo")
else:
  es_primo = True
  for i in range(2, numero):
    if numero % i == 0:
      es_primo = False
      break
  if es_primo:
    print(f"El número {numero} es primo")
  else:
    print(f"El número {numero} no es primo")
"""
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un 
descuento del 20%.
"""
precio = float(input("Por favor, ingrese el precio del producto: "))
 
descuento = 0.20
precio_final = precio - (precio * 0.20) 

print(f"El precio final es {precio_final} €")

"""
Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por 
ejemplo, 145 minutos serían 2 horas y 25 minutos.
"""
minutos_totales = 145
horas = minutos_totales // 60
minutos_restantes = minutos_totales % 60

print(f"{minutos_totales} minutos son {horas} horas y {minutos_restantes} minutos")

"""
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en 
una lista ingresada por el usuario.
"""
lista_numeros = input("Por favor, ingrese una lista de números separados por comas: ")

numeros = [int(num.strip()) for num in lista_numeros.split(",")]
pares = 0
impares= 0

for numero in numeros:
  if numero % 2 == 0:
    pares += 1
  else:
    impares +=1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")

"""
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo 
que 1 milla equivale a 1.60934 kilómetros.
"""
millas = 2
kilometros = millas * 1.60934 

print(f"{millas} millas equivalen a {kilometros} km")

"""
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por 
el usuario.
"""
oracion = input("Por favor, ingrese una frase: ")

palabras = oracion.split()
cantidad = len(palabras)
print(f"La oración ingresada tiene {cantidad} palabras")

"""
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.
"""
año = int(input("Por favor, introduce un año: "))
if(año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
  print(f"El año {año} es bisiesto")
else:
  print(f"El año {año} no es bisiesto")

"""
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el 
usuario
"""
lista_numeros = input("Por favor, ingrese una lista de números separados por comas: ")

numeros = [int(num.strip()) for num in lista_numeros.split(",")]
suma = 0

suma_total = sum(numeros)

print(f"La suma de la lista de números es {suma_total}")

