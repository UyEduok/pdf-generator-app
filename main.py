from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p', unit='mm', format='A4')

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():

    pdf.add_page()

    pdf.set_text_color(100, 100, 100)
    pdf.line(10, 21, 200, 21)

    pdf.set_font(family='Times', style='B', size=12)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='l', ln=1)

    for i in range(row['Pages']-1):
        pdf.add_page()

pdf.output('output.pdf')
