diccionario = {}
print(diccionario)
# añadir con el método setdefault
diccionario.setdefault(3, True)
print(diccionario)
diccionario.setdefault(4,[5,7,8,])
print(diccionario)

# añadir utilizando el operador de asignación "="
diccionario[5] = 'Pedro'
print(diccionario)

for i in diccionario:
    print(i)