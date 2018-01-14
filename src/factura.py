import os
import modulos
import conexion
os.environ['UBUNTU_MENUPROXY']='0'
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Facturas:
    
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file("ventana.glade")
        ## VENTANAS
        self.ventana = b.get_object("window1")
        ## CAMPOS DE TEXTOS
        self.entDni = b.get_object("entrydni")
        self.entName = b.get_object("entryname")
        self.entApellidos = b.get_object("entryapellidos")
        self.entDireccion = b.get_object("entrydireccion")
        self.entTelefono = b.get_object("entrytelefono")
        self.entEmail = b.get_object("entryemail")
        ## BOTONES
        self.insert = b.get_object("btninsert")
        self.delete = b.get_object("btndelete")
        self.update = b.get_object("btnupdate")
        self.salir = b.get_object("btnsalir")
        ## OTROS WIDGETS
        self.vistaC = b.get_object("vistaclientes")
        self.listaC = b.get_object("listaclientes")
        dic = {"on_window1_destroy": self.cerrar,
               "on_btninsert_clicked": self.insertarC,
               "on_btndelete_clicked": self.borrarC,
               "on_btnupdate_clicked": self.modificarC,
               "on_btnsalir_clicked": self.cerrar,
               "on_vistaclientes_cursor_changed": self.selectC,}
        b.connect_signals(dic)
        self.ventana.show_all()
        self.listarclientes()
        
    def cerrar(self, widget):
        Gtk.main_quit()
    
    ## OPERACIONES CLIENTES ( INSERTAR, MODIFICAR, ELIMINAR, SELECCIONAR ) 
    
    def insertarC(self, widget, data = None):
        self.dni = self.entDni.get_text()
        self.nombre = self.entName.get_text()
        self.apellidos = self.entApellidos.get_text()
        self.direccion = self.entDireccion.get_text()
        self.telefono = self.entTelefono.get_text()
        self.email = self.entEmail.get_text()
        fila = (self.dni,self.nombre,self.apellidos,self.direccion,self.telefono,self.email)
        if self.dni != '' and self.nombre != '' and self.apellidos != '' and self.direccion != '' and self.telefono != '' and self.email != '':
            conexion.insertarCli(fila)
            modulos.limpiarClientes(self)
            self.listaC.clear()
            self.listarclientes()
        else:
            print("No puedes dejar campos vacios...")
            
    def borrarC(self, widget, data = None):
        self.dni = self.entDni.get_text()
        if self.dni != '':
            conexion.eliminarCli(self.dni)
            modulos.limpiarClientes(self)
            self.listaC.clear()
            self.listarclientes()
        else:
            print("No puedes dejar el campo dni vacio...")
            
    def modificarC(self, widget, data = None):
        self.dni = self.entDni.get_text()
        self.nombre = self.entName.get_text()
        self.apellidos = self.entApellidos.get_text()
        self.direccion = self.entDireccion.get_text()
        self.telefono = self.entTelefono.get_text()
        self.email = self.entEmail.get_text()
        if self.dni != '' and self.nombre != '' and self.apellidos != '' and self.direccion != '' and self.telefono != '' and self.email != '':
            conexion.modificarCli(self.dni,self.nombre,self.apellidos,self.direccion,self.telefono,self.email)
            self.listaC.clear()
            self.listarclientes()
            
    def selectC(self, widget):
        model, iter = self.vistaC.get_selection().get_selected()
        if iter != None:
            sdni = model.get_value(iter, 0)
            snombre = model.get_value(iter, 1)
            sapellidos = model.get_value(iter, 2)
            sdireccion = model.get_value(iter, 3)
            stelefono = model.get_value(iter, 4)
            semail = model.get_value(iter, 5)
            self.entDni.set_text(sdni)
            self.entName.set_text(snombre)
            self.entApellidos.set_text(sapellidos)
            self.entDireccion.set_text(sdireccion)
            self.entTelefono.set_text(str(stelefono))
            self.entEmail.set_text(semail)
            
    def listarclientes(self):
        resultado = conexion.listarCli()
        for registroC in resultado:
            self.listaC.append(registroC)
            
if __name__ == "__main__":
    main = Facturas()
    Gtk.main()