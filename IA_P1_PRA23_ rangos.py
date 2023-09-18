edad = int(input('¿Cuantos años tienes?\n'))
if edad <= 0:
	print('Parece que tienes meses de nacido')
elif edad >= 1 and edad <= 18:
	print('Aun no eres mayor de edad.')
elif edad > 18 and edad <= 50:
	print('Eres mayor de edad.')
elif edad > 50 and edad <= 100:
	print('Eres persona de la 3ra edad')
elif edad > 100 and edad <= 120:
	print('Como lo hiciste?.')
else:
	print('Edad no válida.12')
