# inventario.py
# Clase que gestiona el inventario completo

from producto import Producto  # Importamos la clase Producto para poder usarla aquí

class Inventario:
    def __init__(self):
        # Inicializa el inventario como una lista vacía donde guardaremos los productos
        self.productos = []

    def agregar_producto(self, producto):
        # Función para agregar un producto al inventario
        for p in self.productos:
            if p.get_id() == producto.get_id():
                # Si ya existe un producto con el mismo ID, mostramos un error
                print("Error: Ya existe un producto con ese ID.")
                return
        # Si el ID es único, agregamos el producto a la lista
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        # Función para eliminar un producto por su ID
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)  # Lo eliminamos de la lista
                print("Producto eliminado correctamente.")
                return
        # Si no encontramos el producto, mostramos un mensaje de error
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Función para actualizar la cantidad y/o precio de un producto
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)  # Actualizamos la cantidad si nos pasan un valor
                if precio is not None:
                    p.set_precio(precio)      # Actualizamos el precio si nos pasan un valor
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")  # Si no existe, mostramos error

    def buscar_producto(self, nombre):
        # Busca productos por nombre (puede ser parcial) y devuelve la lista de resultados
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        # Muestra todos los productos del inventario
        if not self.productos:
            print("El inventario está vacío.")  # Si no hay productos, avisamos
        for p in self.productos:
            print(p)  # Imprimimos cada producto usando su __str__
