import PyPDF2

with open("dummy.pdf", "rb") as my_file:
    reader = PyPDF2.PdfReader(my_file)
    print(len(reader.pages))
    print(reader.pages[0])
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("tilted.pdf", "wb") as new_file:
        writer.write(new_file)
