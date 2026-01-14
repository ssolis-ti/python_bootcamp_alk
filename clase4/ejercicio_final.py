
class Producto:
    def __init__(self, nombre,categoria,descripcion, disponible):
        self.nombre = nombre
        self.categoria = categoria
        self.descripcion = descripcion
        self.disponible = disponible

radio = Producto("Radio","Audio","dispositivo para escuchar musica", True)
lavadora = Producto("Lavadora","electrodomestico","dispositivo para lavar la ropa", True)
celular = Producto("Celular","telefono","dispositivo para llamar", True)
audifono = Producto("Audifono","accesorio","dispositivo para escuchar musica en movimiento", False)


#lista de los productos
productos = [ radio, lavadora, celular, audifono]

for producto in productos:

    #por que el atributo disponible marca si hay o no stock del producto en la tienda
    if producto.disponible == True:
        
        if producto.categoria == "electrodomestico":
            print("el producto pertenece a la categoria electrodomestico")
            print(f"Descripcion: {producto.descripcion}")
            
        elif producto.categoria == 'telefono':
            print("el producto pertenece a la categoria teléfono")
            print(f"Descripcion: {producto.descripcion}")

        elif producto.categoria == 'computadora':
            print("el producto pertenece a la categoria computadora")
            print(f"Descripcion: {producto.descripcion}")

        elif producto.categoria == 'accesorio':
            print("el producto pertenece a la categoria accesorio")
            print(f"Descripcion: {producto.descripcion}")
        else:
            print("El producto no pertenece a ningua de las categorias del sistema (electrodomestico, telefono, computadora, accesorio)")

    else:
        print(f"el producto {producto.nombre} se encuentra agotado")