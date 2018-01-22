# -*- coding: utf-8 -*-
from fpdf import FPDF
import os
import conexion

class PDF(FPDF):
    
    ## CABECERA DE LA FACTURA
    def header(self):
        self.image('factura.png', 15, 8, 20)
        self.set_font('Arial', 'B', 12)
        self.cell(80)
        titulo = "FRUTAS El niño de Cádiz, S.L"
        self.cell(60, 5, titulo, 1, 1, 'C')
        self.ln(10)
        self.set_font('Arial', 'I', 10)
        titulo2 = "Compra Fruta Pisha"
        self.cell(60, 5, titulo2, 0, 1, 'L')
        self.ln(5)
        
    ## PIE DE LA FACTURA
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'UI', 8)
        self.cell(0 ,6 ,"NIF: B0000000", 0, 0, 'C')
        
def getFactura(factura, cliente):
    pdf = PDF('P', 'mm', 'A4')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial','B', 12)
    pdf.cell(0,8,"Factura : " + str(factura), 0, 1, 'C')
        
archivo = 'factura.pdf'
pdf.output(archivo, 'F')
os.system("evince" + archivo)