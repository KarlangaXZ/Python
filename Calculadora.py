def Suma(x, y):
    return x + y

def Resta(x, y):
    return x - y

def Multiplicacion(x, y):
    return x * y

def Division(x, y):
    return x / y

print("Calculador simple \n")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

operador = input(" Registre tipo de operacion aqui: ")

num1 = float( input("Ingrese el primer numero : "))
num2 = float(input("Ingrese el segundo numero : "))

if operador == '1':
    print(num1, "+", num2, "=", Suma(num1,num2))

elif operador == '2':
    print(num1, "-", num2, "=", Resta(num1,num2))

elif operador == '3':
    print(num1, "*", num2, "=", Multiplicacion(num1,num2))

elif operador == '4':
    print(num1, "/", num2, "=", Division(num1,num2))

else:
    print("Algo salio mal, Asegurate solo usar numero.")