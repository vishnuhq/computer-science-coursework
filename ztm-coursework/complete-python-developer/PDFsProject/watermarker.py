import PyPDF2


def add_watermark(sourcefile, watermarkfile):
    reader = PyPDF2.PdfReader(watermarkfile)
    watermark = reader.pages[0]
    sourcepdf = PyPDF2.PdfReader(sourcefile)
    writer = PyPDF2.PdfWriter()
    for page in sourcepdf.pages:
        page.merge_page(watermark)
        writer.add_page(page)
    with open("watermarked.pdf", "wb") as outputfile:
        writer.write(outputfile)


with open("supermerged.pdf", "rb") as source:
    with open("wtr.pdf", "rb") as watermark:
        add_watermark(source, watermark)
