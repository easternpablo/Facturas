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
        
def listarCli():
    try:
        cursor.execute(" select * from Cliente")
        resultado = cursor.fetchall()
        return resultado
    except:
        print("Fallo durante el listado de los clientes....")
        cursor.rollback()