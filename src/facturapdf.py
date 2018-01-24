# -*- coding: utf-8 -*-
from fpdf import FPDF
import os
import conexion

def crearPDF(factura,cliente):
    
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

    
    pdf = PDF('P', 'mm', 'A4')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial','B', 12)
    pdf.cell(0,8,"Factura : " + str(factura), 0, 1, 'C')
    detallesVenta = conexion.listarVentasConcreta(factura)
    detallesCliente = conexion.listarClientesConcreto(cliente)
    for row in detallesCliente:
        pdf.cell(0,8,"DATOS CLIENTE", 0, 1, 'R')
        pdf.cell(0,8,"DNI/CIF : " + str(row[0]), 0,1,'R')
        pdf.cell(0,8,"NOMBRE:" + str(row[2]) + " " + str(row[1]), 0,1,'R')
        pdf.cell(0,8,"DIRECCION : " + str(row[3]),0,1,'R')
        pdf.cell(0,8,"TELÉFONO : " + str(row[4]) + "     MAIL: " +str(row[5]), 0,1,'R')
        
    cabecera = "Producto           Cantidad          Precio Unitario         Precio Total"
    pdf.cell(0,40,cabecera,0,1,'C')
    pdf.line(164,50,200,50)
    
    
    
    pdf = PDF()
    archivo = 'factura.pdf'
    pdf.output(archivo, 'F')
    os.system('/usr/bin/evince factura.pdf')