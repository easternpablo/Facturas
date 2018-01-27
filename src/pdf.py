from fpdf import FPDF
import os
import conexion


class PDF(FPDF):
    ## CABECERA DE LA FACTURA
    def header(self):
        self.image('factura.png', 15, 8, 20)
        self.set_font('Arial', 'B', 12)
        self.cell(80)
        titulo = "FRUTAS VILCHES, S.L"
        self.cell(60, 5, titulo, 1, 1, 'C')
        self.ln(10)
        self.set_font('Arial', 'I', 10)
        titulo2 = "Compra Fruta Pisha"
        self.cell(60, 20, titulo2, 0, 1, 'L')
        self.ln(5)

    ## PIE DE LA FACTURA
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'UI', 8)
        self.cell(0 ,6 ,"NIF: B0000000", 0, 0, 'C')
    
## MUESTRA LA FACTURA COMPLETA
def crearPDF(factura,cliente):
    pdf = PDF('P', 'mm', 'A4')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial','B', 12)
    pdf.cell(0,8,"Factura : " + str(factura), 0, 1, 'C')
    detallesVenta = conexion.listarVentasConcreta(factura)
    detallesCliente = conexion.listarClientesConcreto(cliente)
    ## MUESTRA TODOS LOS DATOS DEL CLIENTE
    for row in detallesCliente:
        print row
        pdf.cell(0,8,"DATOS CLIENTE", 0, 1, 'R')
        pdf.cell(0,8,"DNI/CIF:  " + str(row[0]), 0,1,'R')
        pdf.cell(0,8,"NOMBRE:  " + str(row[2]) + "   " + str(row[1]), 0,1,'R')
        pdf.cell(0,8,"DIRECCION:  " + str(row[3]),0,1,'R')
        pdf.cell(0,8,"TELEFONO:  " + str(row[4]) + "  -  MAIL: " +str(row[5]), 0,1,'R')
    ## MUESTRA EL DETALLE DE LAS VENTAS    
    cabecera = "Producto           Cantidad           Precio Unitario           Precio Total"
    pdf.cell(0,40,cabecera,0,1,'C')
    pdf.line(164,50,200,50)
    pdf.line(20,100,190,100)
    pdf.line(20,106,190,106)
    suma = 0
    iva = 0.21
    total = 0
    y = 110
    for item in detallesVenta:
        pdf.set_font('Arial','',10)
        prodnom = conexion.verProd(str(item[2]))
        cantidad = "{0:.2f}".format(float(item[3]))
        precio = float(item[4])
        subtotal = float(item[5])
        x = 20
        pdf.text(x,y,"  |  " + str(prodnom[0]))
        x = x + 50
        pdf.text(x,y,"  |  " + str(cantidad))
        x = x + 40
        pdf.text(x,y,"  |  " + str(precio))
        x = x + 55
        pdf.text(x,y,"  |  " + str(subtotal))
        x = x + 15
        pdf.text(x,y,"  |  " )
        y = y + 5
        suma = suma + subtotal
    
    iva = suma * 0.21
    total = iva + suma
    suma = "{0:.2f}".format(suma)
    iva = "{0:.2f}".format(iva)
    total = "{0:.2f}".format(total)
    pdf.ln(70)
    pdf.set_font('Arial','B',10)
    lineaTotal = "Suma de conceptos                      IVA %              Cuota IVA                    Importe Total"
    pdf.cell(0,7,lineaTotal,1,1, 'C')
    pdf.text(115,210,str(iva) + " Euros")
    pdf.text(155,210, str(total) + " Euros" )
   
    archivo = 'factura.pdf'
    pdf.output(archivo, 'F')
    os.system('/usr/bin/evince factura.pdf')