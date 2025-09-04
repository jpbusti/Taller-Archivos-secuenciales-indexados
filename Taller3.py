class F:
    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for linea in f:
                print(linea.strip())
  
    def read2(self, filename):
        clientes = []
        with open(filename, "r", encoding="utf-8") as f:
            next(f) 
            for linea in f:
                datos = linea.strip().split(",")
                cliente = {"id_cliente": datos[0], "nombre": datos[1], "apellido": datos[2], "telefono": datos[3],"activo": datos[4]}
                clientes.append(cliente)
        return clientes
                
    def write(self, filename, dictionary):
        enable = 1
        id = 1
        with open(filename, "w", encoding="utf-8") as f:
            labels = list(dictionary[0].keys())
            f.write("id,")
            for label in labels:
                f.write(label + ",")
            f.write("activo" + "\n")
            for a in dictionary:
                count = 0
                f.write(str(id)+ ",")
                for d in a.values():
                    f.write(d )
                    count+=1
                    f.write(",")
                id+=1 
                f.write(str(enable)+"\n")
           
    def delete(self, filename, id):
        list = []
        with open(filename, "r", encoding="utf-8") as f:
            list = f.readlines()
        newList = []
        for l in list:
            arr = l.strip().split(',')
            if str(arr[0]) == str(id):
                print(id)
                arr[len(arr)-1] = "0"
                ll = ""
                count = 1
                for a in arr:
                    ll = ll + str(a)  
                    if count < len(arr):
                        ll = ll + ","
                    count+=1
                l = ll + "\n"
            newList.append(l)
        self.write_array(filename, newList)

    def write_array(self, filename, list):
        with open(filename, "w", encoding="utf-8") as f:
            for l in list:
                f.write(l)

    def nuevocliente(clientes):
        nuevo_id = str(len(clientes) + 1)
        print ("Ingrese el nombre: ")
        nombre = input()
        print("Ingrese el apellido: ")
        apellido = input()
        print("Ingrese el teléfono: ")
        telefono = input()
        cliente = {"id_cliente": nuevo_id,"nombre": nombre,"apellido": apellido,"telefono": telefono,"activo": "1"}
        clientes.append(cliente)

    def nuevopedido(ventas):
        nuevo_id = str(len(ventas) + 1)
        print("Ingrese el ID del cliente: ")
        id_cliente = input()
        print("Ingrese el ID del producto: ")
        id_producto = input()
        print("Ingrese la cantidad: ")
        cantidad = input()
        nueva_venta = {"id_pedido": nuevo_id, "id_cliente": id_cliente, "id_producto": id_producto, "cantidad": cantidad}
        ventas.append(nueva_venta)

    def nuevoproducto(productos):
        nuevo_id = str(len(productos) + 1)
        print("Ingrese el nombre del producto: ")
        producto = input()
        print("Ingrese el precio: ")
        precio = input()
        producto_nuevo = {"id_producto": nuevo_id, "nombre": producto, "precio": precio, "activo": "1"}
        productos.append(producto_nuevo)

    def guardarventa():
        print("Ingrese el ID del cliente: ")
        id_cliente = input()
        print("Ingrese el producto: ")
        producto = input()
        print("Ingrese el precio: ")
        precio = input(float)
        print("Ingrese la cantidad: ")
        cantidad = input(int)
        venta = {"producto": producto, "cantidad": cantidad, "precio": precio}
        if id_cliente in ventas:
            ventas[id_cliente].append(venta)
        else:
            ventas[id_cliente] = [venta]

    def listarventas(nombrecliente):
        for c in clientes:
            if c["nombre"].lower() == nombrecliente.lower():
                cliente = c
                break  
        if cliente is None:
            print("Cliente no encontrado")
            return
    
        id_cliente = cliente["id_cliente"]
        total = 0

        for venta in ventas:
            if venta["id_cliente"] == id_cliente:
                id_producto = venta["id_producto"]
                cantidad = venta["cantidad"]

                for p in productos:
                    if p["id_producto"] == id_producto:
                        total += p["precio"] * cantidad
                        break 
        print(total)

ventastotales = {}
productos = [{"id_producto": "1", "nombre": "Laptop", "precio": "2500.00"},
             {"id_producto": "2", "nombre": "Mouse", "precio": "20.50"},
             {"id_producto": "3", "nombre": "Teclado", "precio": "45.00"},
             {"id_producto": "4", "nombre": "Monitor", "precio": "150.00"}]
             
ventas = [{"id_pedido": "1", "id_cliente": "1", "id_producto": "1", "cantidad": "1"},
           {"id_pedido": "2","id_cliente": "2", "id_producto": "2", "cantidad": "2"},
           {"id_pedido": "3","id_cliente": "1","id_producto": "3","cantidad": "1"},
           {"id_pedido": "4","id_cliente": "3","id_producto": "4","cantidad": "1"}]

clientes = [{"id_cliente": "1", "nombre": "Juan", "apellido": "Pérez", "telefono": "3123456789"},
            {"id_cliente": "2", "nombre": "María", "apellido": "Gómez", "telefono": "3112233445"},
            {"id_cliente": "3", "nombre": "Carlos", "apellido": "Ramírez", "telefono": "3205566778"}]
f = F()
f.write("productos.csv", productos)
f.write("clientes.csv", clientes)
f.write("ventas.csv", ventas)
f.read2("clientes.csv")
f.read2("ventas.csv")
f.read2("productos.csv")
while True:
    print("1. Registrar un cliente")
    print("2. Listar clientes")
    print("3. Eliminar un cliente")
    print("4. Registrar un producto")
    print("5. Guardar una venta")
    print("6. Listar las ventas realizadas por cliente")
    print("7. Salir")
    print("Seleccione una opción: ")
    op = input()
    if op == "1":
        F.nuevocliente(clientes)
        f.write("clientes.csv", clientes)
    elif op == "2":
        for cliente in clientes:
            print(cliente["nombre"] +" "+ cliente["apellido"])
    elif op == "3":
        id = input()
        print("Ingrese el ID del cliente a eliminar: ")
        id = input()
        f.delete("clientes.csv", id)   
    elif op == "4":
        F.nuevoproducto(productos)
        f.write("productos.csv", productos)
    elif op == "5":
        F.nuevopedido(ventas)
        f.write("ventas.csv", ventas)
    elif op == "6":
        print("Ingrese el nombre del cliente: ")
        nombre = input()
        F.listarventas(nombre)   
    elif op == "7":
        break
