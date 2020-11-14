##Tarea 24


##función que convierte el número decimal en binario
def convierte_binario(decimalAconvertir):
	##creamos una lista para ir añadiendo los códigos binarios
	numBinario= []
	##creamos una cadena donde neteremos el código binario resultante y será el valor que devuelva la función.
	cadenaBinaria = ""
	##asignamos el numero a convertir a la variable cociente
	cociente = decimalAconvertir
	##creamos una variable resto par albergar el resultado de la operación resto
	resto = 0

	##mediante un bucle vamos dividiendo el número a convertir entre 2 guardando el resto, el bucle se ejecutará mientras el número resultante se pueda dividir entre 2, es decir, mientras sea mayir que 1 
	while cociente>1:
		resto = cociente%2
		cociente = cociente//2
		##añadimos el resto a la lista
		numBinario.append(resto)
		
	#una vez terminada la ejecución del bucle añadimos el cociente que haya quedado
	numBinario.append(cociente)
	##damos la vuelta a la lista para tener el código binario en el orden correcto
	numBinario.reverse()
	##fomamos una cadean con los elementos de la lista, esta cadena será el resultado de la función
	for n in numBinario:
		cadenaBinaria = cadenaBinaria + str(n)
	return cadenaBinaria


convertir = "S"
##mediante un bucle posibilitamos al usuario que pueda convertir más de un número digital 
while convertir == "S" or convertir == "s":
	##Pedimos al usuario que meta el número decimal a convertir
	numeroDecimal = input("Introduce un nº decimal: ")

	#Comprobamos que el valor introducido es un número, en caso de que no lo sea seguirá pidiendo input hasta que el usuario meta un número
	while numeroDecimal.isdigit() == False:
		numeroDecimal = input("Incorrecto. Introduce un nº decimal: ")

	#Comprobamos que el número introducido es un decimal, en caso de que no lo sea seguirá pidiendo input hasta que el usuario meta un número decimal
	while "." in numeroDecimal or "," in numeroDecimal:
		numeroDecimal = input("Incorrecto. Introduce un nº decimal: ")

	##llamamos a la función que va a convertir el número decimal en binario, pasamos el número introducido por el usuario a entero para poder hacer las operaciones precisas
	codigoBinario = convierte_binario(int(numeroDecimal))

	##mostramos en pantalla
	print("El nº " + numeroDecimal + " en codigo binario es: " + codigoBinario)
	print(" ")
	##preguntamos al usuario si quiere convertir otro número
	convertir = input("¿Quieres convertir otro número?(S/N)")	

##Si no quiere seguir convistiendo nos depedimos
print("Agur!")



