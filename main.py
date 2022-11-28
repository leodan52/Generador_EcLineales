# Descripcion


from TOOLS.despeje_ejercicios import *
import random

def main():
	ejercicios = []
	archivo = "ejercicios.tex"
	total = 50
	n = 0
	salida = open(archivo, "w")

	while len(ejercicios) != total:
		aux = Despeje()

		if aux not in ejercicios:
			print(f'\\item ${aux}$', file=salida)
			n += 1
			print(f'Ecuacion {n} generada de {total}')
			ejercicios.append(aux)


	salida.close()


def main2():
	ejercicios = []
	archivo_entrada = "ejercicios.tex"
	archivo_salida = "desigualdades.tex"

	inequ = {0: "<", 1: ">", 2: "\\leq", 3: "\\geq" }


	entrada = open(archivo_entrada, "r")
	Salida_text = ""
	for i in entrada:
		eleccion = random.randint(0,3)
		impresion = i.replace("=", inequ[eleccion])
		Salida_text = Salida_text + impresion
	entrada.close()

	salida = open(archivo_salida, "w")
	print(Salida_text, file=salida)
	salida.close()



main()
