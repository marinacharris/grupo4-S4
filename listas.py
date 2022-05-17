# Una lista es una colección de datos que se utiliza para guardar
# varios elementos
# Una lista es indexada de forma numérica
# Las listas son mutables

# crear lista:
ciudades = ["New York", "Londres", "Madrid"]
frutas = list(("manzana","pera","coco")) # no olvide el doble paréntesis
print(ciudades, type(ciudades))
print(frutas, type(frutas))
frutas[0] ='banana'
print(frutas)

pos = 0
for i in ciudades: # la variable i toma el valor de los elementos de la lista
    if i == 'Londres':
        print(f'Londres está en la posición {pos} de la lista')
    print(i)
    pos +=1
    
ciudades.append("Caracas") # añadir un elemento al final de la lista
ciudades.remove('New York') # eleiminar un elemento
print(ciudades)

print('Londres' in ciudades)
ciudades.extend(frutas)
print(ciudades)
lista1 = [ 40, [50,20,80], 'Carlos']
print(lista1[2][1])
print(lista1.index('Carlos'))
print(lista1)
