import os 
os.system ("cls") 

# cadenas a lista
cadena = 'Colombia'
lista = list(cadena)
print(lista)

#lista a cadena

cad = ''.join(lista)
print(cad)

nombre = 'Pedro'
diccionario = dict(zip(range(1,len(nombre)+1),nombre))
print(diccionario)

lista1 = ['Enero','Febrero','Marzo','Abril']
lista2 = [150000000, 200000000, 180000000, 220000000]
diccionario2 = dict(zip(lista1,lista2))
print(diccionario2)
print(diccionario.values())
print(diccionario.keys())
print(diccionario.items())
cadena2 = ''.join(diccionario.values())
print(cadena2)