# Es una coleccion de datos que se utiliza para almacenar 
# varios elementos.
# Los conjuntos no son ordenados, son mutables,
# es decir se le pueden agregar o quitar elementos  y no 
# permite elementos duplicados

nombres = {'Juan', 'Camilo', 'Sergio', 'Verónica', 'Sergio'}
ciudades = set((
    'Caracas', 
    'Panamá', 
    'Quito'))
print(nombres, type(nombres))
print(ciudades, type(ciudades)),
numeros = {8,8,9,6,5,6,6,8,5,2,2,3,7,8,5,8,4,5,4, True, 'Casa'}
print(numeros)

#añadir elemento a un conjunto, método add
ciudades.add('Nueva York')
#eliminar un elemento
ciudades.remove('Quito')
print(ciudades)
print('Panamá' in ciudades)
for i in ciudades:
    print(i)
