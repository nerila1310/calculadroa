import numpy as np
import math

def simpleOperations(num1, num2, operation):
    if (operation == 1):
        print("\t\tEl resultado de la suma es: ", num1 + num2)
        return
    if (operation == 2):
        print("\t\tEl resultado de la resta es: ", num1 - num2)
        return
    if (operation == 3):
        print("\t\tEl resultado de la multiplicación es: ", num1 * num2)
        return
    if (operation == 4):
        print("\t\tEl resultado de la división es: ", num1 / num2)
        return

def trigonometryOperations(num, operation):
	if (operation == 6):
		print("\t\tEl resultado de la potencia es: ", (num**2))
		return
	if (operation == 7):
		print("\t\tEl resultado de la operacion seno es: ", math.sin(num))
		return
	if (operation == 8):
		print("\t\tEl resultado de la operacion coseno es: ", math.cos(num))
		return
	if (operation == 9):
		print("\t\tEl resultado de la operacion tangente es: ", math.tan(num))
		return

def printMenu():
    print("\n\t\t -------Ingresa una opcion de la calculadora a ocupar------- \n"
		  "\n\t 1) Sumar"
          "\n\t 2) Restar"
          "\n\t 3) Multiplicar"
          "\n\t 4) Dividir"
          "\n\t 5) Raiz n"
          "\n\t 6) Exponente n"
          "\n\t 7) Seno"
          "\n\t 8) Coseno"
          "\n\t 9) Tangente"
          "\n\t 10 Exit\n")
    return int(input('\t\t Que opcion deseas realizar: '))

