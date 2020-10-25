##Tarea 23
import random


##funciones
##función que pcifra y descifra el texto
def cifra_descifra(cifraTextoDescifra,listaCartasB):

	#creamos un diccionario con las letras y su correpondiente valor
	valoresLetras = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

	##función que devuelve el valor numérico del texto a cifrar/descifrar
	def valor_numerico_texto(textoCD):
		listaTxtNum=[]
 		##creamos un diccionario con las letras y su valor numérico
		numLetras = len(textoCD)
 		##vamos buscando el valor de cada letra
		for i in range(numLetras):
			valorLetra = valoresLetras.get(textoCD[i:i+1])
			listaTxtNum.append(valorLetra)

		return listaTxtNum


	##función que devuelve el texto cifrado correspondientes a una lista de valores numéricos
	def valor_texto_numerico(listaNumeros):
		##pasamos a una lista las claves del diccionario y utilizamos el valor numérico como índice de la lista
		claves = list(valoresLetras.keys())
		txtCifrado =''
		for j in listaNumeros:
			txtCifrado = txtCifrado + claves[j-1]
		return txtCifrado


	##################################
	##función que ejecuta el algoritmo del solitario para sacar el valor numérico a sumar al valor numérico del texto
	def solitario(listaCartasBarajeada):

		print("listaPaso0")
		print(listaCartasBarajeada)
		##Paso1 del agoritmo: Intercambiar Joker A con la carta que está debajo
		posicionJokerA = listaCartasBarajeada.index("Joker A")
		listaCartasBarajeada.remove("Joker A")
		listaCartasBarajeada.insert(posicionJokerA + 1,"Joker A")

		print("listaPaso1")
		print(listaCartasBarajeada)
		##Paso 2 del agoritmo: intercambiar Joker B con la carta que está debajo de la que tiene debajo
		posicionJokerB = listaCartasBarajeada.index("Joker B")
		listaCartasBarajeada.remove("Joker B")
		listaCartasBarajeada.insert(posicionJokerB + 2,"Joker B")

		print("listaPaso2")
		print(listaCartasBarajeada)
		##Paso 3 del algoritmo: cortamos la baraja en 3, intercambiando las cartas antes del primer comodín con las cartas que están detrás del segundo comodin.
		posicionJokerA = listaCartasBarajeada.index("Joker A")
		posicionJokerB = listaCartasBarajeada.index("Joker B")

		if posicionJokerA < posicionJokerB:
			primerComodin = posicionJokerA
			segundoComodin = posicionJokerB
		else:
			primerComodin = posicionJokerB 
			segundoComodin = posicionJokerA


		listaCorte1 = listaCartasBarajeada[0:primerComodin]
		listaCorte2 = listaCartasBarajeada[segundoComodin + 1:54]

		##pasamos el corte 2 a la parte de arriba
		indiceAinsertar = 0
		for k in listaCorte2:
			listaCartasBarajeada.remove(k)
			listaCartasBarajeada.insert(indiceAinsertar,k)
			indiceAinsertar = indiceAinsertar + 1

		##pasamos el corte 1
		for j in listaCorte1:
			listaCartasBarajeada.remove(j)
			listaCartasBarajeada.append(j)

		print("listaPaso3")
		print(listaCartasBarajeada)
		##Paso 4 del agoritmo: buscamos la última carta de la baraja, buscamos su valor numérico, contamos desde la primera carta hasta ese valor numerico
		ultimaCarta = listaCartasBarajeada[53]
		valorUltimaCarta = barajaCartas[listaCartasBarajeada[53]]
		listaCorte3 = listaCartasBarajeada[0:valorUltimaCarta]
		listaCartasBarajeada.remove(listaCartasBarajeada[53])
		#print("listaCorte3")
		#print(listaCorte3)

		##pasamos el corte 1
		for m in listaCorte3:
			listaCartasBarajeada.remove(m)
			listaCartasBarajeada.append(m)

		listaCartasBarajeada.append(ultimaCarta)

		print("listaPaso4")
		print(listaCartasBarajeada)
		##Paso 5 del algoritmo; mira la primera carta y conviertela en numero, cuenta las cartas hasta ese número (la primera es el uno)
		primeraCarta = listaCartasBarajeada[0]
		valorPrimeraCarta = barajaCartas[listaCartasBarajeada[0]]
		CartaPaso5 = listaCartasBarajeada[valorPrimeraCarta]
		valorCartaPaso5 = barajaCartas[CartaPaso5]

		print("listaPaso5")
		print(listaCartasBarajeada)
		return valorCartaPaso5

	##cuerpo de la función cifra_descifra	
	##llamamos a la función que nos devuelve el valor numérico del texto a cifrar
	valorTexto = valor_numerico_texto(cifraTextoDescifra)
	print("valorTexto")
	print(valorTexto)
	##utilizamos el algoritmo del solitario para generar la ristra a sumar para conseguir el texto cifrado
	# ristra = []
	# for n in cifraTextoDescifra:
	valorRistra = solitario(listaCartasB)
	# 	ristra.append(valorRistra)
	# print("ristra")
	# print(ristra)

	##ahora sumamos los valores de las letras a cifrar con los valores que nos ha devuelto el algoritmo del solitario	
	valorTextomasRistra = []

	for i, w in enumerate(valorTexto):
 	  	valorTextomasRistra.append(valorTexto[i] + ristra[i])

	print("Final1")
	print(valorTextomasRistra)

	valorTextomasRistra2 = []

	for v in valorTextomasRistra:
		valorCorregido = v
		if v > 26 and v <= 52:
			valorCorregido = v -26
		elif v > 52:
			valorCorregido = v-52

		valorTextomasRistra2.append(valorCorregido)


	print("Final2")
	print(valorTextomasRistra2)



	return valor_texto_numerico(valorTextomasRistra2)
	#return valorTexto





#######################
##construimos la baraja

##Palos de la baraja
palosBaraja = ("Treboles","Diamantes","Corazones","Picas")

##creamos una lista con las cartas para barajearlas
listaCartas = []

##Valores de las cartas
## Treboles -- Su valor
## Diamantes -- su valor + 13
## Corazones - su valor + 26
## Picas -- su valor + 39

barajaCartas = {"Joker A":53,"Joker B":53}
listaCartas = ["Joker A","Joker B"]

for element in palosBaraja:
	for i in range(13):
		if element == "Treboles":
			valorASumar = 0
		elif element == "Diamantes":
			valorASumar = 13
		elif element == "Corazoness":
			valorASumar = 26
		elif element == "Picas":
			valorASumar = 39

		cartaBaraja = str(i+1) + element
		valor = barajaCartas.setdefault(cartaBaraja,i+1 + valorASumar)
 		##creamos una lista con las cartas de la baraja para despues "barajearla"
		listaCartas.append(cartaBaraja)


##barajeamos la baraja de cartas
random.shuffle(listaCartas)
print("listaCartas_01")
print(listaCartas)
##Pedimos al usuario que escriba el texto a cifrar
textoAcifrar = input("Introduce el texto a cifrar: ")
##ponemos el texto en mayúsculas
textoAcifrar = textoAcifrar.upper()
numeroDeLetras = len(textoAcifrar)

txtCifrado = cifra_descifra(textoAcifrar,listaCartas)
# print(textoAcifrar + ' cifrado es: ' + txtCifrado)

# respuesta = ''

# #while respuesta != 'S' or respuesta != 'N'
# while respuesta not in ('S','N'):
#  	respuesta1 = input("¿Quieres descifrar " + txtCifrado + "? (S/N): ")	
#  	respuesta = respuesta1.upper()

# if respuesta == 'N':
#  	## No desciframos
#  	print("OK. Agur")
# else:
# 	print("listaCartas")
# 	print(listaCartasBuena)
# 	txtDescifrado = cifra_descifra(txtCifrado,listaCartasBuena)
# 	print(txtDescifrado)

