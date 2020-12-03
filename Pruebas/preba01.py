class Punto:
	def __init__(self,x,y):
		self.X=x
		self.Y=y

	def MostrarPunto(self):
		print("El punto es (",self.X,".",self.Y,")")


#p1 = Punto(4,6)
#p1.MostrarPunto()


class Pokemon:
	def __init__(self,nombre,vida,ataque):
		self.Nombre = nombre
		self.Vida = vida
		self.Ataque = ataque

	def MostrarPokemon(self):
		print("Datos del pokemon (",self.Nombre,".",self.Vida,".",self.Ataque,")")


p1 = Pokemon("Picachu",100,55)
p1.MostrarPokemon()