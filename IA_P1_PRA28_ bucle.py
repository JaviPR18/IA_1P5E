# Valor inicial de x
x = 18

# while se ejecuta hasta menor o igual que 30
while x <= 30:
	x += 2  # incrementos de 1

	# if para saltar ejecuciones del bucle
	if x == 2 or x == 4 or x == 6:
		print('Se saltó el valor ', x, ' de x')
		continue

	# if para romper la ejecución del bucle
	if x == 30:
		print('Se rompió la ejecución del bucle cuando x valía: ', x)
		break

	# imprime los resultados que no se corresponden a ninguno de los if
	print(x)