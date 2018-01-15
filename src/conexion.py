try:
    import sqlite3
    bbdd = "Facturas.sqlite"
    conexion = sqlite3.connect(bbdd)
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
        cursor.rollback()
        
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
        cursor.rollback()