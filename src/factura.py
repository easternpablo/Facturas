import conexion
import modulos
import os
import pdf
import time
os.environ['UBUNTU_MENUPROXY']='0'
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Facturas:
    
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file("ventana.glade")
        ## VENTANAS Y LABELS
        self.ventana = b.get_object("window1")
        self.etiquetaCod = b.get_object("lblnumfactura")
        self.etiquetaPrecio = b.get_object("lblprecio")
        ## CAMPOS DE TEXTOS
        self.entDni = b.get_object("entrydni")
        self.entName = b.get_object("entryname")
        self.entApellidos = b.get_object("entryapellidos")
        self.entDireccion = b.get_object("entrydireccion")
        self.entTelefono = b.get_object("entrytelefono")
        self.entEmail = b.get_object("entryemail")
        self.entProd = b.get_object("entryprod")
        self.entPrecio = b.get_object("entryprecio")
        self.entStock = b.get_object("entrystock")
        self.entCliente = b.get_object("entrycliente")
        self.entCantidad = b.get_object("entrycantprod")
        ## BOTONES
        self.insert = b.get_object("btninsert")
        self.delete = b.get_object("btndelete")
        self.update = b.get_object("btnupdate")
        self.salir = b.get_object("btnsalir")
        self.insert2 = b.get_object("btninsert2")
        self.delete2 = b.get_object("btndelete2")
        self.update2 = b.get_object("btnupdate2")
        self.salir2 = b.get_object("btnsalir2")
        self.iniV = b.get_object("btnstartV")
        self.finV = b.get_object("btnfinishV")
        self.agregarV = b.get_object("btnagregarcarrito")
        self.imprimir = b.get_object("btnprint")
        ## LISTAS
        self.listaC = b.get_object("listaclientes")
        self.listaP = b.get_object("listaproductos")
        self.listaP2 = b.get_object("listaprod")
        self.listaF = b.get_object("listafacturas")
        self.listaV = b.get_object("listadetalles")
        ## VISTAS
        self.vistaC = b.get_object("vistaclientes")
        self.vistaP = b.get_object("vistaproductos")
        self.vistaF = b.get_object("vistafacturas")
        self.vistaV = b.get_object("vistadetalles")
        ## OTROS WIDGETS
        self.comboproducto = b.get_object("cmbproducto")
        #self.imagen = b.get_object("imagen")
        #self.dlgimg = b.get_object("filechooser")
        ## DICCIONARIO CON EVENTOS
        dic = {"on_window1_destroy": self.cerrar,
               "on_btninsert_clicked": self.insertarC,
               "on_btninsert2_clicked": self.insertarP,
               "on_btndelete_clicked": self.borrarC,
               "on_btndelete2_clicked": self.borrarP,
               "on_btnupdate_clicked": self.modificarC,
               "on_btnupdate2_clicked": self.modificarP,
               "on_btnsalir_clicked": self.cerrar,
               "on_btnsalir2_clicked": self.cerrar,
               "on_btnstartV_clicked": self.agregarFactura,
               "on_btnagregarcarrito_clicked": self.agregarVenta,
               "on_btnprint_clicked": self.formarPDF,
#              "on_btnfinishV_clicked": self.eliminarFactura,
               "on_cmbproducto_changed": self.selectProd,
               "on_vistaclientes_cursor_changed": self.selectC,
               "on_vistaproductos_cursor_changed": self.selectP,
               "on_vistafacturas_cursor_changed": self.selectF,}
        b.connect_signals(dic)
        self.ventana.show_all()
        self.listarclientes()
        self.listarproductos()
        self.listarfacturas()
        self.cargarProductos(self)
        
    def cerrar(self, widget):
        Gtk.main_quit()
        
    def formarPDF(self, widget):
        self.numFactura = self.etiquetaCod.get_text()
        self.dniCliente = self.entCliente.get_text()
        pdf.crearPDF(self.numFactura, self.dniCliente)
    
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
            self.entCliente.set_text(sdni)
         
    def listarclientes(self):
        resultado = conexion.listarCli()
        for registroC in resultado:
            self.listaC.append(registroC)
            
    ## OPERACIONES PRODUCTOS ( INSERTAR, MODIFICAR, ELIMINAR, SELECCIONAR )
    
    def insertarP(self, widget, data = None):
        self.producto = self.entProd.get_text()
        self.precio = self.entPrecio.get_text()
        self.stock = self.entStock.get_text()
        fila = (self.producto,self.precio,self.stock)
        if self.producto != '' and self.precio != '' and self.stock != '':
            conexion.insertarPro(fila)
            modulos.limpiarProductos(self)
            self.listaP.clear()
            self.listarproductos()
        else:
            print("No puedes dejar campos vacios...")
            
    def borrarP(self, widget, data = None):
        if self.scodigoP != '':
            conexion.eliminarPro(self.scodigoP)
            modulos.limpiarProductos(self)
            self.listaP.clear()
            self.listarproductos()
        else:
            print("Tienes que seleccionar el producto a eliminar")
            
    def modificarP(self, widget, data = None):
        self.producto = self.entProd.get_text()
        self.precio = self.entPrecio.get_text()
        self.stock = self.entStock.get_text()
        if self.scodigoP != '':
            conexion.modificarPro(self.scodigoP,self.producto,self.precio,self.stock)
            self.listaP.clear()
            self.listarproductos()
            
    def selectP(self, widget):
        model, iter = self.vistaP.get_selection().get_selected()
        if iter != None:
            self.scodigoP = model.get_value(iter, 0)
            sproducto = model.get_value(iter, 1)
            sprecio = model.get_value(iter, 2)
            sstock = model.get_value(iter, 3)
            self.entProd.set_text(sproducto)
            self.entPrecio.set_text(str(sprecio))
            self.entStock.set_text(str(sstock))
            
    def listarproductos(self):
        resultado = conexion.listarPro()
        for registroP in resultado:
            self.listaP.append(registroP)
            
    ## OPERACIONES FACTURACION
    
    def cargarProductos(self, widget):
        lista = conexion.productos()
        for row in lista:
            self.listaP2.append(row)
            
    def selectProd(self, widget):
        index = self.comboproducto.get_active()
        model = self.comboproducto.get_model()
        self.producto = model[index]
        precio = conexion.cogerPrecio(self.producto[0])
        self.etiquetaPrecio.set_text(str(precio))
        
    def agregarFactura(self, widget):
        self.cliente = self.entCliente.get_text()
        self.fecha = time.strftime("%d/%m/%y")
        fila = (self.cliente,self.fecha)
        if self.cliente != '':
            conexion.insertarFac(fila)
            self.listaF.clear()
            self.listarfacturas()
        else:
            print("No puedes dejar el campo cliente vacio...")
            
    def selectF(self, widget):
        model, iter = self.vistaF.get_selection().get_selected()
        if iter != None:
            self.scodigo = model.get_value(iter, 0)
            scliente = model.get_value(iter, 1)
            sfecha = model.get_value(iter, 2)
            self.entCliente.set_text(scliente)
            self.etiquetaCod.set_text(str(self.scodigo))
            self.listaV.clear()
            self.listarventas2(self.scodigo)
            
    def listarfacturas(self):
        resultado = conexion.listarFac()
        for registroF in resultado:
            self.listaF.append(registroF)
            
    ## OPERACIONES VENTA
            
    def agregarVenta(self, widget):
        self.factura = self.etiquetaCod.get_text()
        self.codProd = conexion.cogerCodigo(self.producto[0])
        self.cantidad = self.entCantidad.get_text()
        self.precioUnidad = float(self.etiquetaPrecio.get_text())
        self.precioFinal = float(self.cantidad)*float(self.precioUnidad)
        fila = (self.scodigo,self.codProd,self.cantidad,self.precioUnidad,self.precioFinal)
        if self.scodigo != '' and self.cantidad != '':
            conexion.insertarVent(fila)
            self.stockObtenido = conexion.cogerStock(self.producto[0])
            self.newStock = int(self.stockObtenido)-int(self.cantidad)
            conexion.actualizarStock(self.newStock,self.codProd)
            self.listaP.clear()
            self.listarproductos()
            modulos.limpiarDetalle(self)
            self.listaV.clear()
            self.listarventas2(self.factura)
        else:
            print("No puedes dejar campos vacios....")
            
    def listarventas(self):
        resultado = conexion.listarVen()  
        for registroV in resultado:
            self.listaV.append(registroV)
            
    def listarventas2(self,factura):
        resultado = conexion.listarVentasConcreta(factura)  
        for registroV in resultado:
            self.listaV.append(registroV)
            
#   def eliminarFactura(self, widget, data = None):
#       if self.scodigo != '':
#           conexion.eliminarFac(self.scodigo)
#           modulos.limpiarFacturas(self)
#           self.listaF.clear()
#           self.listarfacturas()
#       else:
#           print("No puedes dejar el campo dni vacio...")
                     
if __name__ == "__main__":
    main = Facturas()
    Gtk.main()