"""
1. Capturar desde consola el nombre del producto, precio, categoría y stock disponible.
2. Validar tipos de datos: str para nombre y categoría, float para precio, int para stock.
3. Utilizar operadores para verificar si el producto está en oferta (por ejemplo: si el precio es menor o igual 1000).
4. Crear registros como diccionarios y almacenarlos en una lista de inventario.
5. Dividir el código en módulos reutilizables.

"""
#nom tenemos categorias para validar
registros = []

while True:
    opcion = int(input(
        """
        Ingrese una opcion
        1. Agregar producto
        2. Salir
        """
    ))
    if opcion == 1 :
        nombre_del_producto = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoria del producto: ")
        precio = float(input("Ingrese el precio producto: "))
        stock_disponible = int(input("Ingrese el stock disponible: "))
        oferta = False
        if precio <=  1000:
            oferta = True

        registros.append({
        "nombre_del_producto" :nombre_del_producto,
        "categoria" : categoria,
        "precio" : precio,
        "stock_disponible": stock_disponible,
        "oferta" : oferta,
        })
        print("registro existoso")
        
    elif opcion == 2:

        if len(registros)>0:
            for diccionario in registros:
                print(f"""
                      nombre: {diccionario["nombre_del_producto"]},
                      categoria: {diccionario["categoria"]}
                      precio: ${diccionario["precio"]}
                      stock disponible: {diccionario["stock_disponible"]}
                      oferta: {diccionario["oferta"]}
""")

        print("saliendo") 
        break
    else:
        print("Opcion no valida")

