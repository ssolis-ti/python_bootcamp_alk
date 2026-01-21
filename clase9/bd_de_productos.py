"""
1. Crear un diccionario productos donde cada clave sea un ID ("P001", "P002", etc.)
2. Cada valor será un diccionario con los campos: nombre, precio, stock
3. Acceder a los datos de un producto por su ID
4. Agregar un nuevo producto al diccionario
5. Modificar el stock de un producto existente
6. Eliminar un producto usando pop()
7. Iterar sobre todos los productos mostrando:
8. "Producto: Teclado | Precio: $5000 | Stock: 10"
9. Bonus: Mostrar solo los productos con stock menor a 10"""

#1 y #2
productos = {
    "P001":{"nombre":"Arroz", "precio":1200, "stock":11},
    "P002":{"nombre":"Fideos", "precio":900, "stock":9},
    "P003":{"nombre":"Azucar", "precio":1100, "stock":6},
    "P004":{"nombre":"Aceite", "precio":2500, "stock":10},
    "P005":{"nombre":"Sal", "precio":900, "stock":8},
    "P006":{"nombre":"Leche", "precio":1200, "stock":7},
    "P007":{"nombre":"Pan", "precio":2000, "stock":100},
    "P008":{"nombre":"Huevos", "precio":300, "stock":50},
}

#3 acceder a los elementos por ID
lista_llaves = productos.keys()

# for llave in lista_llaves:
#     print(productos[llave])
#es lo mismo que
#    print(productos["P001"]) etc

#4 update o por llave

productos["P009"] = {"nombre":"Cafe", "precio":4500, "stock":15}

# print(productos)

#por update
# productos.update({"P009":{"nombre":"Cafe", "precio":4500, "stock":15}})

#5 modificaremos el stock del pan P007

productos["P007"]["stock"] = 5


#6 eliminamos el arroz usando pop

productos.pop("P001")
# print(productos)

#7 "Producto: Teclado | Precio: $5000 | Stock: 10" iterar

#estaba pensando en hacerlo suponiendo que no conozco las llaves del diccionario anidado
# for llave in productos.keys(): #["P002","P003"......]

#     for clave, valor in productos[llave]:

#modo hard

#si ya sabemos que las claves del diccionario anidado son nombre, precio, stock

for producto in productos.values():
    print(f"Producto: {producto["nombre"]}| Precio: {producto["precio"]}| Stock: {producto["stock"]}")

#8 bonus mostrar elementos con stock menor a 10

for producto in productos.values():
    if producto["stock"] <10:
        print(f"Producto: {producto["nombre"]}| Precio: {producto["precio"]}| Stock: {producto["stock"]}")
