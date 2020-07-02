
print("Tarea 21\n")
#Pedimos que introduzca el nº
numero = input("Introduce un nº entre 0.0001 y 0.9999: ")


#Comprobamos que el nº está en el rango indicado. NO HE CONSEGUIDO METER LAS TRES CONDICIONES EN UN WHILE
while numero[0]!= "0":
	numero = input("Incorrecto. Introduce un nº entre 0.0001 y 0.9999: ")

while len(numero)>6:
	numero = input("Incorrecto. Introduce un nº entre 0.0001 y 0.9999: ")

while len(numero)<3:
	numero = input("Incorrecto. Introduce un nº entre 0.0001 y 0.9999: ")

#sustituimos la coma decimal por punto para que no de error al convertir en tipo float
numero = numero.replace(",",".")

#calculamos la fracción irreducible
numerador = int(float(numero) * 10000)
div = numerador
denominador = 10000

while div > 1 :
    if numerador % div == 0 and denominador % div == 0:
        numerador = numerador / div
        denominador = denominador / div
    div =  div - 1
 
print ("La fracción irreducible es: " + str(int(numerador)) + "/" + str(int(denominador)))








