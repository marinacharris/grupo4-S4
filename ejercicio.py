# Realice un programa que lea el código numérico de un producto como llave de un 
# diccionario y dicha llave va a almacenar nombre, precio y cantidad 
# del producto en una lista.
# El programa debe permitir cargar datos al diccionario, debe mostrar 
# un listado completo del diccionario, debe permitir consultar un producto 
# por su llave, actualizar precio y/o cantidad de un producto
# y eliminar productos

# Aplicación CRUD, create, read, update, delete

def mostrar():
    print('LISTADO DE PRODUCTOS')
    print('Código','Nombre','Precio','Cantidad', sep='\t\t')
    for i in productos:
        print(i, productos[i][0], productos[i][1], productos[i][2],sep='\t\t')

def consultar():
    codigo = int(input('Digite el código del producto que desea consultar\n'))
    if codigo in productos:
        print('Código','Nombre','Precio','Cantidad', sep='\t\t')
        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2],sep='\t\t')
    else:
        print('El código del producto no existe')

def actualizar():
    # actualizar precio y cantidad
    codigo = int(input('Digite el código del producto que desea actualizar\n'))
    if codigo in productos:
        precio = int(input('Digite el nuevo precio del producto\n'))
        cantidad = int(input('Digite la cantidad actualizada del producto\n'))
        productos[codigo][1] = precio
        productos[codigo][2] = cantidad
        print('Prodcto actualizado:', productos[codigo])
    else:
        print('El código del producto no existe')
        
def borrar():
    codigo = int(input('Digite el código del producto que desea eliminar:\n'))
    if codigo in productos:
        print('Producto eliminado:', productos.pop(codigo))
    else:
        print('El código del producto no existe')

def crear():
    codigo = int(input('Digite el código del producto\n'))
    nombre = input('Digite el nombre del producto\n')
    precio = int(input('Digite el precio unitario del producto\n'))
    cantidad = int(input('Digite la cantidad existente\n'))
    #productos.setdefault(codigo,[nombre,precio,cantidad]) #añadir una llave
    productos[codigo] = [nombre, precio, cantidad] #añadir una llave
    print('Producto creado:', productos[codigo])



productos ={ #inicializar el diccionario
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
    print('4. Actualizar\n5. Eliminar\n')
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



    