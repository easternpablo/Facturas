import conexion
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
        dic = {"on_window1_destroy": self.cerrar,
               "on_btninsert_clicked": self.insertarC,
               "on_btnsalir_clicked": self.cerrar,}
        b.connect_signals(dic)
        self.ventana.show_all()
        
    def cerrar(self, widget):
        Gtk.main_quit()
        
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
        else:
            print("No puedes dejar campos vacios...")

if __name__ == "__main__":
    main = Facturas()
    Gtk.main()
