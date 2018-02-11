from fpdf import FPDF
import os
import conexion

class PDF(FPDF):

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

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'UI', 8)
        self.cell(0 ,6 ,"NIF: B0000000", 0, 0, 'C')
        
def crearPDF():
    pdf = PDF('P', 'mm', 'A4')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial','B', 12)
    detallesCliente = conexion.listarCli()
    titulo = "    LISTADO DE CLIENTES   "
    pdf.cell(0,20,titulo,0,1,'C')  
    cabecera = "Dni              Nombre              Apellidos               Direccion            Telefono"
    pdf.cell(0,67,cabecera,0,1,'C')
    pdf.line(20,100,190,100)
    pdf.line(20,106,190,106)
    y = 110
    for row in detallesCliente:
        pdf.set_font('Arial','',10)
        dni = str(row[0])
        nombre = str(row[1])
        apellidos = str(row[2])
        direccion = str(row[3])
        telefono = str(row[4])
        x = 18
        pdf.text(x,y,"    " + dni)
        x = x + 40
        pdf.text(x,y,"    " + nombre)
        x = x + 30
        pdf.text(x,y,"    " + apellidos)
        x = x + 40
        pdf.text(x,y,"    " + direccion)
        x = x + 35
        pdf.text(x,y,"    " + telefono)
        y = y + 5

    archivo = 'cliente.pdf'
    pdf.output(archivo, 'F')
    os.system('/usr/bin/evince cliente.pdf')