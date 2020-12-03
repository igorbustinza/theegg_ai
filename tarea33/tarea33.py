##tarea 33

##Creamos la clase Pokemon que tendrá 3 atributos, Nombre del Pokemon, Cantidad de Vida y potencia de Ataque
class Pokemon:
	def __init__(self,nombre,vida,ataque):
		self.Nombre = nombre
		self.Vida = vida
		self.Ataque = ataque


##Pedimos al usuario que introduzca el nombre del primer Pokemon
nombreP1 = input("Introduce el nombre del primer Pokemon: ")

##Pedimos al usuario que introduzca la vida del primer Pokemon
vidaP1 = input("Introduce la vida del primer Pokemon: ")
while vidaP1.isdigit() == False:
		vidaP1 = input("Incorrecto, tiene que ser un nº. Prueba otra vez: ")

##Pedimos al usuario que introduzca la potencia del primer Pokemon
ataqueP1 = input("Introduce la potencia de ataque del primer Pokemon: ")
while ataqueP1.isdigit() == False:
		ataqueP1 = input("Incorrecto, tiene que ser un nº. Prueba otra vez: ")

##Pedimos al usuario que introduzca el nombre del segundo Pokemon
nombreP2 = input("Introduce el nombre del segundo Pokemon: ")

##Pedimos al usuario que introduzca la vida del segundo Pokemon
vidaP2 = input("Introduce la vida del segundo Pokemon: ")
while vidaP2.isdigit() == False:
		vidaP2 = input("Incorrecto, tiene que ser un nº. Prueba otra vez: ")

##Pedimos al usuario que introduzca la potencia del segundo Pokemon
ataqueP2 = input("Introduce la potencia de ataque del segundo Pokemon: ")
while ataqueP2.isdigit() == False:
		ataqueP2 = input("Incorrecto, tiene que ser un nº. Prueba otra vez: ")


##Creamos el objeto Pokemnon correspondiente al primer Pokemon, asignándole sus atributos
Pokemon1 = Pokemon(nombreP1,int(vidaP1),int(ataqueP1))
print("En el rincón 1 " + Pokemon1.Nombre)

##Creamos el objeto Pokemnon correspondiente al segundo Pokemon, asignándole sus atributos
Pokemon2 = Pokemon(nombreP2,int(vidaP2),int(ataqueP2))
print("En el rincón 2 " + Pokemon2.Nombre)


##empezará atacando el primer Pokemon por lo que ponemos la variable turno a 1
turno=1

##mientras los dos Pokemons tengan vida, los ataques serán constantes
while Pokemon1.Vida>0 and Pokemon2.Vida>0:
	if turno==1:
		##ataca el Pokemon1
		Pokemon2.Vida = Pokemon2.Vida - Pokemon1.Ataque
		turno = 0
	else:
		##ataca el Pokemon2
		Pokemon1.Vida = Pokemon1.Vida - Pokemon2.Ataque
		turno = 1

##al cumplirse la condición para salir de bucle, vemos quien ha ganado
if Pokemon1.Vida<=0:
	##si el Pokemon2 se ha quedado con vida, ha sido el ganador
	print(Pokemon2.Nombre + " GANADOR"  )
else:
	##si el Pokemon1 se ha quedado con vida, ha sido el ganador
	print(Pokemon1.Nombre + " GANADOR"  )