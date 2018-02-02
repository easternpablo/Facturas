try:
    import sqlite3
    bbdd = "Facturas.sqlite"
    conexion = sqlite3.connect(bbdd)
    conexion.text_factory = str
    cursor = conexion.cursor()
except:
    print("Error de conexion...")
    
## OPERACIONES CLIENTES

def insertarCli(registro):
    try:
        cursor.execute(" insert into Cliente(Id_Cliente,Nombre,Apellidos,Direccion,Telefono,Email) values(?,?,?,?,?,?)",registro)
        conexion.commit()
        print(">> Nuevo Cliente ingresado")
    except:
        print("Fallo durante la insercion de un cliente....")
        conexion.rollback()
        
def eliminarCli(dni):
    try:
        cursor.execute(" delete from Cliente where Id_Cliente=?",(dni,))
        conexion.commit()
        print(">> Cliente eliminado")
    except:
        print("Fallo durante la eliminacion de un cliente....")
        conexion.rollback()
        
def modificarCli(dni,nombre,apellidos,direccion,telefono,email):
    try:
        cursor.execute(" update Cliente set Nombre=?, Apellidos=?, Direccion=?, Telefono=?, Email=? where Id_Cliente=?",(nombre,apellidos,direccion,telefono,email,dni))
        conexion.commit()
    except:
        print("Fallo durante la modificacion de un cliente....")
        conexion.rollback()
        
def listarCli():
    try:
        cursor.execute(" select * from Cliente")
        resultado = cursor.fetchall()
        return resultado
    except:
        print("Fallo durante el listado de los clientes....")
        conexion.rollback()
        
## OPERACIONES PRODUCTOS

def insertarPro(registro):
    try:
        cursor.execute(" insert into Producto(Nombre,Precio,Stock) values(?,?,?)",registro)
        conexion.commit()
        print(">> Nuevo Producto ingresado")
    except:
        print("Fallo durante la insercion de un producto....")
        conexion.rollback()
        
def eliminarPro(codigo):
    try:
        cursor.execute(" delete from Producto where Id_Producto=?",(codigo,))
        conexion.commit()
        print(">> Producto eliminado")
    except:
        print("Fallo durante la eliminacion de un producto....")
        conexion.rollback()
        
def modificarPro(codigo,producto,precio,stock):
    try:
        cursor.execute(" update Producto set Nombre=?, Precio=?, Stock=? where Id_Producto=?",(producto,precio,stock,codigo))
        conexion.commit()
    except:
        print("Fallo durante la modificacion de un producto....")
        conexion.rollback()
        
def listarPro():
    try:
        cursor.execute(" select * from Producto")
        resultado = cursor.fetchall()
        return resultado
    except:
        print("Fallo durante el listado de los productos....")
        conexion.rollback()
        
## OPERACIONES CON EL COMBO BOX

def productos():
    try:
        cursor.execute("select Nombre from Producto")
        listado = cursor.fetchall()
        return listado
    except:
        print("Hubo problemas al cargar los productos....")
        conexion.rollback
        
def cogerPrecio(producto):
    try:
        cursor.execute("select Precio from Producto where Nombre=?",(producto,))
        referencia = cursor.fetchone()
        conexion.commit()
        Precio = referencia[0]
        return Precio
    except:
        print("Hubo problemas al seleccionar un producto....")
        conexion.rollback
        
def cogerCodigo(producto):
    try:
        cursor.execute("select Id_Producto from Producto where Nombre=?",(producto,))
        referencia = cursor.fetchone()
        conexion.commit()
        codigo = referencia[0]
        return codigo
    except:
        print("Hubo problemas al seleccionar un producto....")
        conexion.rollback
        
def cogerStock(producto):
    try:
        cursor.execute("select Stock from Producto where Nombre=?",(producto,))
        referencia = cursor.fetchone()
        conexion.commit()
        stock = referencia[0]
        return stock
    except:
        print("Hubo problemas al seleccionar un producto....")
        conexion.rollback

## OPERACIONES VENTAS
        
def insertarFac(registro):
    try:
        cursor.execute(" insert into Factura(Id_Cliente,Fecha) values(?,?)",registro)
        conexion.commit()
        print(">> Nueva factura agregada")
    except:
        print("Fallo durante la insercion de una factura....")
        conexion.rollback()
        
def insertarVent(registro):
    try:
        cursor.execute(" insert into Venta(Id_Factura,Id_Producto,Cantidad,Precio,PrecioFinal) values(?,?,?,?,?)",registro)
        conexion.commit()
        print(">> Nueva venta agregada")
    except:
        print("Fallo durante la insercion de una venta....")
        conexion.rollback()
        
def eliminarVent(detalle):
    try:
        cursor.execute(" delete from Venta where Num_Detalle=?",(detalle,))
        conexion.commit()
        print(">> Venta eliminada")
    except:
        print("Fallo durante la eliminacion de una venta....")
        conexion.rollback()
        
def actualizarStock(stock,codigo):
    try:
        cursor.execute(" update Producto set Stock=? where Id_Producto=?",(stock,codigo))
        conexion.commit()
        print("Stock actualizado con exito")
    except:
        print("Fallo durante la actualizacion del stock....")
        conexion.rollback()
        
def listarVen():
    try:
        cursor.execute(" select * from Venta")
        resultado = cursor.fetchall()
        return resultado
    except:
        print(">> Fallo durante el listado de las ventas....")
        conexion.rollback()
        
def listarVentasConcreta(numfactura):
    try:
        cursor.execute(" select * from Venta where Id_Factura=?",(numfactura,))
        resultado = cursor.fetchall()
        return resultado
    except:
        print("Fallo durante el listado de las ventas....")
        conexion.rollback()
        
def listarClientesConcreto(dni):
    try:
        cursor.execute(" select * from Cliente where Id_Cliente=?",(dni,))
        resultado = cursor.fetchall()
        return resultado
    except:
        print("Fallo durante el listado de los clientes....")
        conexion.rollback()
        
def verProd(codigo):
    try:
        cursor.execute(" select Nombre from Producto where Id_Producto=?",(codigo,))
        referencia = cursor.fetchone()
        conexion.commit()
        nombre = referencia[0]
        return nombre
    except:
        print("Fallo durante el listado del producto....")
        conexion.rollback()
#def eliminarFac(codigo):
#    try:
#        cursor.execute(" delete from Factura where Num_Factura=?",(codigo,))
#        conexion.commit()
#        print(">> Factura eliminada")
#    except:
#        print("Fallo durante la eliminacion de una factura....")
#        conexion.rollback()
        
def listarFac():
    try:
        cursor.execute(" select * from Factura")
        resultado = cursor.fetchall()
        return resultado
    except:
        print("Fallo durante el listado de las facturas....")
        conexion.rollback()