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
            f.write("status" + "\n")
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
        print("Cliente registrado exitosamente.")
    
    def nuevopedido(pedidos):
        nuevo_id = str(len(pedidos) + 1)
        print("Ingrese el ID del cliente: ")
        id_cliente = input()
        print("Ingrese el producto: ")
        producto = input()
        print("Ingrese el precio: ")
        precio = input()
        print("Ingrese la cantidad: ")
        cantidad = input()
        pedido = {"id_pedido": nuevo_id, "id_cliente": id_cliente, "producto": producto, "precio": precio, "cantidad": cantidad, "activo": "1"}
        pedidos.append(pedido)

    def guardarventa():
        print("Ingrese el ID del cliente: ")
        id_cliente = input()
        print("Ingrese el producto: ")
        producto = input()
        print("Ingrese el precio: ")
        precio = input()
        print("Ingrese la cantidad: ")
        cantidad = input()
        venta = {"producto": producto, "cantidad": cantidad, "precio": precio}
        if id_cliente in ventas:
            ventas[id_cliente].append(venta)
        else:
            ventas[id_cliente] = [venta]
    def listarventas():
        print ("Ingrese el ID del cliente: ")
        id_cliente = input()
        if id_cliente not in ventas:
            print("No hay ventas registradas para este cliente.")
            return
        total = 0
        print("Ventas del cliente:")
        for venta in ventas[id_cliente]:
            p = venta["cantidad"] * venta["precio"]
            print(f"- {venta['producto']} Cantidad: {venta['cantidad']} "f"Precio unitario: {venta['precio_unitario']} Subtotal: {p}")            
            total += p
        print("Total de la venta:" + {total})    

ventas = {}
             
pedidos = [{"id_pedido": "1", "id_cliente": "1", "producto": "Laptop", "precio": "2500.00", "cantidad": "1", "activo": "1"},
           {"id_pedido": "2","id_cliente": "2", "producto": "Mouse", "precio": "20.50", "cantidad": "2", "activo": "1"},
           {"id_pedido": "3","id_cliente": "1","producto": "Teclado","precio": "45.00","cantidad": "1","activo": "1"},
           {"id_pedido": "4","id_cliente": "3","producto": "Monitor","precio": "150.00","cantidad": "1","activo": "0"}]

clientes = [{"id_cliente": "1", "nombre": "Juan", "apellido": "Pérez", "telefono": "3123456789", "activo": "1"},
            {"id_cliente": "2", "nombre": "María", "apellido": "Gómez", "telefono": "3112233445", "activo": "1"},
            {"id_cliente": "3", "nombre": "Carlos", "apellido": "Ramírez", "telefono": "3205566778", "activo": "1"}]
f = F()
f.write("clientes.csv", clientes)
f.write("pedidos.csv", pedidos)
f.read2("clientes.csv")
f.read2("pedidos.csv")
while True:
    print("1. Registrar un cliente")
    print("2. Listar clientes")
    print("3. Eliminar un cliente")
    print("4. Registrar un pedido")
    print("5. Listar pedidos de un cliente")
    print("6. Guardar una venta")
    print("7. Listar las ventas realizadas por cliente")
    print("8. Salir")
    print("Seleccione una opción: ")
    op = input()
    if op == "1":
        F.nuevocliente(clientes)
        f.write("clientes.csv", clientes)
    
    elif op == "2":
        for cliente in clientes:
            print(cliente["nombre"])
    
    elif op == "3":
        print("Ingrese el ID del cliente a eliminar: ")
        id = input()
        f.delete("clientes.csv", id)
    
    elif op == "4":
        F.nuevopedido(pedidos)
        f.write("pedidos.csv", pedidos)

    elif op == "5":
        print("Ingrese el ID del cliente para listar sus pedidos: ")
        id_cliente = input()
        for pedido in pedidos:
            if pedido["id_cliente"] == id_cliente:
                print(pedido)
    elif op == "6":
        F.guardarventa()
    elif op == "7":
        F.listarventas()   
    elif op == "8":
        break
