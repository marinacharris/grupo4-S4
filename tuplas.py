# Las tuplas son una colección de datos que se utilizan para almacenar varios
# elementos
# son colecciones indexadas, son inmutables

# crear tupla
ciudades  = ('Cali', 'Medellín', 'Barranquilla')
print(ciudades, type(ciudades))
datos = tuple((True, [4,5,6], (6,7,89),'Carlos',20))
# ciudades[1] = 'Montería', esto No se puede porque las tuplas son inmutables
# los siguientes método no aplican para las tuplas
''' reverse()
append()
extend()
remove()
clear()
sort() '''

for i in datos:
    print(i, type(i))
    
lista = list(datos)
print(lista, type(lista))

def operaciones(a,b):
    suma = a+b 
    resta = a-b 
    mult = a*b 
    div = a/b 
    return suma, resta, mult, div 

resultados = operaciones(25,5)
print(resultados, type(resultados))   
print(f'El resultado de la suma es: {resultados[0]}')
