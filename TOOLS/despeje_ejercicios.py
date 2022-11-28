# Descripcion


# Ax + B = Cx + D
# Ax - Cx = D - B
# x = (D - B)/(A - C)

import random
from TOOLS.fraccion import *
import numpy as np

class Despeje:
	def __init__(self):
#		self.ejercicio = []
		self.loop = False

		while not self.loop:
			self.ejercicio = []
			while len(self.ejercicio) != 4:
				numero = random.randint(-100, 100)

				if numero not in self.ejercicio:
					self.ejercicio.append(numero)

			self.ejercicio = np.array(self.ejercicio)
			self. loop = self.Loop()


	def __repr__(self):
		a, b, c, d = Despeje.Nume2strs(self.ejercicio)
		A, B, C, D = "", "", "", ""

		if int(a) != 0:
			A = f'{a}x'
			if abs(int(a)) == 1:
				A = A.replace("1", "")

		if int(c) != 0:
			C = f'{c}x'
			if abs(int(c)) == 1:
				C = C.replace("1", "")

		if int(b) != 0:
			B = b
		if int(d) != 0:
			D = d

		izquierda = f'{A}{B}'
		derecha = f'{C}{D}'

		if izquierda[0] == "+":
			izquierda = izquierda[1:]
		if derecha[0] == "+":
			derecha = derecha[1:]

		return f'{izquierda} = {derecha}'


	def Loop(self):

		a, b, c, d = self.ejercicio
		self.solucion = (d-b)/(a-c)

		fraccion = Fraccion(self.solucion)

		if fraccion.vector[1] != 1:
			return False
		aux = []

		for i in self.ejercicio:
			if i != 0:
				aux.append(i)

		algunos, todos = Fraccion.Factorizacion_prima(*aux)
		MCD = 1

		for i in todos:
			MCD *= i

		self.solucion = self.solucion/MCD

		return True


	def __eq__(self, other):
		n1 = self.ejercicio == other.ejercicio
		n2 = self.solucion == other.solucion

		return all(n1) or n2

	@staticmethod
	def Nume2strs(Array):
		salida = []
		for i in Array:
			delta = abs(i - int(i))

			if i >= 0:
				signo = "+"
			else:
				signo = ""

			if delta == 0.0:
				salida.append(signo + str(int(i)))
			else:
				salida.append(signo + str(i))
		return salida
