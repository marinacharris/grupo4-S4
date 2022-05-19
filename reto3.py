'''Cadena de caracteres de la forma   
Producto  consultado  :  {idProducto}  Descripción  {dProducto} 
#Parte {pnProducto} Cantidad vendida {cvProducto} Stock 
{sProducto} Comprador {nComprador} Documento 
{cComprador} Fecha Venta {fVenta}
“No hay registro de venta de ese producto” 

Producto consultado : 2010  Descripción  bujía  #Parte  MS9512  Cantidad vendida  4  Stock  15  Comprador Carlos Rondon  Documento  1256  Fecha Venta  12/06/2020↩
Producto consultado : 2010  Descripción  bujía  #Parte  ER6523  Cantidad vendida  9  Stock  36  Comprador Pedro Montes  Documento  1243  Fecha Venta  12/06/2020
'''
def AutoPartes(ventas:list):
    diccionario = dict(zip(range(len(ventas)),ventas))
    return diccionario

def consultaRegistro(ventas: dict, idProducto):
    for i in ventas:
        if ventas[i][0] == idProducto:
            dProducto = ventas[i][1]
            pnProducto = ventas [i][2]
            cvProducto = ventas[i][3]
            sProducto = ventas[i][4]
            nComprador = ventas[i][5]
            cComprador = ventas[i][6]
            fVenta = ventas[i][7]
            print(f'Producto  consultado  :  {idProducto}  Descripción  {dProducto} #Parte {pnProducto} cantidad vendida {cvProducto} Stock {sProducto} Comprador {nComprador} Documento {cComprador} Fecha Venta {fVenta}')
    return f''

ventas =[ 
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'), 
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'), 
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),     
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'), 
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')
]

print(consultaRegistro(AutoPartes(ventas),2010))