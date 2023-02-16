# Crea un programa en Python que simule una lista de compras. 
# El programa debe permitir al usuario agregar productos al final 
# de la lista, eliminar productos del inicio de la lista y 
# mostrar todos los productos en la lista en orden de compra.

import listaSimple

class Producto():
    def __init__(self):
        self.nombre = None

def listaCompras():
    listaCompras = listaSimple.ListaEnlazada()
    def menu():
        print('''
        ++++++++++++++++ Lista de compras +++++++++++++++++++
        [1]: Agregar producto 
        [2]: Eliminar primer producto
        [3]: Mostrar productos
        [4]: Salir
        ''')
        val = input('Opcion: -> ')
        return val

    def agregarProducto(producto):
        listaCompras.agregar(producto)

    def eliminarPrimerProducto():
        listaCompras.eliminarInicio()
    
    def mostrarListaProducto():
        cont = 0
        cadena = ''
        lista = listaCompras
        actual = lista.primero

        while actual != None:
            cadena += f'Producto {cont + 1}: {actual.dato.nombre}'
            cadena += '\n'
            actual = actual.siguiente
            cont += 1
        if cont == 0:
            cadena += 'No hay productos para mostrar'

        return cadena

    # +++++++++++++++++++ Programa principal +++++++++++++++++++

    while True:
        val = menu()
        if val == '1':
            producto = Producto()
            nombre = input("Ingrese nombre de producto: ")
            producto.nombre = nombre
            agregarProducto(producto)

        elif val == '2':
            eliminarPrimerProducto()

        elif val == '3':
            cadena = mostrarListaProducto()
            print(cadena)

        elif val == '4':
            break

        else:
            print('Ingrese una opción válida')
            pass

if __name__ == "__main__":
    listaCompras()