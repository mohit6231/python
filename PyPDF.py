import PyPDF2

with open("invoice_view.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)
