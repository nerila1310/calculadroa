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

def afterOperation():
    print("\n\t\t -------Elige una opcion del menu------- \n"
		  "\n\t 1) Regresar al menú"
          "\n\t 2) Volver a realizar la operación"
          "\n\t 3) Salir de calculadora\n")
    return int(input('\t\t Que opcion deseas: '))

def calculate(operation):
	if (operation == 10):
			return 3
	elif (operation > 0 and operation <= 4):
		num1 = int(input("\n\t Ingrese el primer valor: "))
		num2 = int(input("\t Ingrese el segundo valor: "))
		simpleOperations(num1, num2, operation)
	elif (operation == 5):
		while 1:
			num1 = int(input("\n\t Ingrese el un valor: "))
			if (num1 >= 0):
				break
		print("\t\tEl resultado de la raiz es: ", np.sqrt(num1))
	elif (operation > 5 and operation <= 9):
		num = int(input("\n\t Ingrese un numero: "))
		trigonometryOperations(num, operation)
	
	after = afterOperation()	
	return after
	
def getOperation():
	operation = printMenu()
	while (operation <= 0 or operation > 10):
		print("\n\t\t -------Ingrese una opción válida para la calculadora-------")
		operation = printMenu()
	return operation

def main():
	operation = getOperation()
	if (operation == 10):
			print("Saliendo de la calcualdora")
			print("\n\t\t\t******  Gracias por usar la calculadora  ******")
			print("--------------------------------------------------------------------------------------------")
	else:
		after = calculate(operation)
		while 1:
			print("--------------------------------------------------------------------------------------------")
			if(after == 3):
				print("\n\t\t\t******  Gracias por usar la calculadora  ******")
				print("--------------------------------------------------------------------------------------------")
				break
			elif(after == 2):
				after = calculate(operation)
			else:
				operation = getOperation()
				after = calculate(operation)
main()