# main.py
# Este archivo controla la interacción con el usuario y utiliza las clases Producto e Inventario
# Aquí se maneja todo el menú y se llama a los métodos para agregar, eliminar, actualizar, buscar y mostrar productos

from producto import Producto  # Traemos la clase Producto desde producto.py
from inventario import Inventario  # Traemos la clase Inventario desde inventario.py


def mostrar_menu():
    """
    Función para mostrar el menú de opciones al usuario.
    Cada vez que se ejecuta, el usuario puede elegir qué acción realizar.
    """
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Agregar producto")  # Opción para agregar un nuevo producto
    print("2. Eliminar producto")  # Opción para eliminar un producto existente por ID
    print("3. Actualizar producto")  # Opción para actualizar la cantidad o precio de un producto
    print("4. Buscar producto")  # Opción para buscar productos por nombre
    print("5. Mostrar todos los productos")  # Opción para ver todos los productos del inventario
    print("6. Salir")  # Opción para salir del programa


def main():
    """
    Función principal que controla el flujo del programa.
    Aquí se crean las instancias de Inventario y se manejan las opciones del menú.
    """
    inventario = Inventario()  # Creamos una lista vacía para guardar todos los productos

    while True:  # Bucle infinito que se repite hasta que el usuario elija salir
        mostrar_menu()  # Mostramos el menú en cada vuelta del bucle
        opcion = input("Seleccione una opción: ")  # Leemos la opción que el usuario escribe

        if opcion == "1":  # Agregar producto
            # Pedimos al usuario todos los datos necesarios para crear un producto
            id_producto = input("Ingrese ID del producto: ")  # ID único
            nombre = input("Ingrese nombre del producto: ")  # Nombre del producto
            cantidad = int(input("Ingrese cantidad: "))  # Cantidad disponible (convertimos a entero)
            precio = float(input("Ingrese precio: "))  # Precio del producto (convertimos a decimal)

            # Creamos un objeto Producto con los datos ingresados
            producto = Producto(id_producto, nombre, cantidad, precio)

            # Llamamos al método para agregar el producto al inventario
            inventario.agregar_producto(producto)

        elif opcion == "2":  # Eliminar producto
            id_producto = input("Ingrese ID del producto a eliminar: ")  # Pedimos el ID del producto
            inventario.eliminar_producto(id_producto)  # Llamamos al método para eliminarlo

        elif opcion == "3":  # Actualizar producto
            id_producto = input("Ingrese ID del producto a actualizar: ")  # ID del producto a cambiar
            cantidad = input("Ingrese nueva cantidad (dejar vacío si no desea cambiar): ")  # Nueva cantidad opcional
            precio = input("Ingrese nuevo precio (dejar vacío si no desea cambiar): ")  # Nuevo precio opcional

            # Convertimos a número solo si el usuario ingresó un valor
            cantidad = int(cantidad) if cantidad else None  # Si dejó vacío, no cambiamos la cantidad
            precio = float(precio) if precio else None  # Si dejó vacío, no cambiamos el precio

            # Llamamos al método de Inventario para actualizar el producto
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":  # Buscar producto
            nombre = input("Ingrese nombre del producto a buscar: ")  # Pedimos nombre o parte del nombre
            resultados = inventario.buscar_producto(nombre)  # Buscamos coincidencias
            if resultados:
                for p in resultados:  # Si hay productos encontrados, los mostramos uno por uno
                    print(p)
            else:
                print("No se encontraron productos.")  # Mensaje si no hay coincidencias

        elif opcion == "5":  # Mostrar todos los productos
            inventario.mostrar_productos()  # Llamamos al método que imprime toda la lista de productos

        elif opcion == "6":  # Salir del programa
            print("¡Saliendo del sistema!")  # Mensaje de despedida
            break  # Salimos del bucle y terminamos el programa

        else:  # Si el usuario ingresa un número no válido
            print("Opción inválida, intente nuevamente.")  # Aviso de error y seguimos en el bucle


# Esta línea asegura que solo se ejecute main() si ejecutamos este archivo directamente
if __name__ == "__main__":
    main()  # Llamamos a la función principal para iniciar el programa
