import os

def limpiarClientes(self):
    self.entDni.set_text('')
    self.entName.set_text('')
    self.entApellidos.set_text('')
    self.entDireccion.set_text('')
    self.entTelefono.set_text('')
    self.entEmail.set_text('')
    
def limpiarProductos(self):
    self.entProd.set_text('')
    self.entPrecio.set_text('')
    self.entStock.set_text('')
    
def limpiarFacturas(self):
    self.entCliente.set_text('')
    self.etiquetaCod.set_text('')
    
def limpiarDetalle(self):
    self.entCantidad.set_text('')
    self.etiquetaPrecio.set_text('')