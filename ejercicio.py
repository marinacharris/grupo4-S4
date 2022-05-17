# Realice un programa que lea el código numérico de un producto como llave de un 
# diccionario y dicha llave va a almacenar nombre, precio y cantidad 
# del producto en una lista.
# El programa debe permitir cargar datos al diccionario, debe mostrar 
# un listado completo del diccionario, debe permitir consultar un producto 
# por su llave, actualizar precio y/o cantidad de un producto
# y eliminar productos

# Aplicación CRUD, create, read, update, delete
def crear():
    pass

def mostrar():
    pass

def consultar():
    pass

def actualizar():
    pass

def borrar():
    pass

productos ={
    1: ['manzana', 2500, 60],
    2: ['pera', 2800, 85],
    3: ['banana', 500, 680]   
}
continuar = 's'
while continuar == 's' or continuar == 'S':
    print('Menu')
    print('1. Crear')
    print('2. Mostrar')
    print('3. Consultar')
    print('4. Actualizar')
    print('5. Eliminar')
    opcion = int(input('Digite una opción [1/2/3/4/5]:\n' ))
    if opcion == 1:
        crear()
    elif opcion == 2:
        mostrar()
    elif opcion == 3:
        consultar()
    elif opcion == 4:
        actualizar()
    elif opcion == 5:
        borrar()
    else:
        print('Digite una opción valida')
    continuar = input('Digite "s" para continuar o culquier tecla para salir\n')
