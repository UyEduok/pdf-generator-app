from fpdf import FPDF
import pandas as pd

# Initialize PDF object
pdf = FPDF(orientation='p', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

# Read data from CSV file
df = pd.read_csv('topics.csv')

# Iterate over each row in the DataFrame
for index, row in df.iterrows():

    # Add a new page to the PDF
    pdf.add_page()

    # Set text color and draw a line
    pdf.set_text_color(100, 100, 100)
    pdf.line(10, 21, 200, 21)

    # Set font and add the topic title as a cell
    pdf.set_font(family='Times', style='B', size=12)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='l', ln=1)

    # Set footer for the page
    pdf.ln(265)
    pdf.set_text_color(180, 180, 180)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R', ln=1)

    # Add additional pages based on the 'Pages' value
    for i in range(row['Pages']-1):
        pdf.add_page()

        # Set footer for the iterated pages
        pdf.ln(277)
        pdf.set_text_color(180, 180, 180)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R', ln=1)

# Output the PDF file
pdf.output('output.pdf')
