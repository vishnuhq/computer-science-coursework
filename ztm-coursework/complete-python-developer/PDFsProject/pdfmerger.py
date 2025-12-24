# my initial code
# import PyPDF2
# import sys
#
# inputs = sys.argv
# inputs.pop(0)
#
# writer = PyPDF2.PdfWriter()
#
# for filename in inputs:
#     with open(filename, "rb") as my_file:
#         reader = PyPDF2.PdfReader(my_file)
#         for page in reader.pages:
#             writer.add_page(page)
#
# with open("combined.pdf", "wb") as outputfile:
#     writer.write(outputfile)


# Code from the course
import PyPDF2
import sys

inputs = sys.argv[1:]


def pdfmerger(pdflist):
    merger = PyPDF2.PdfMerger()
    for pdf in pdflist:
        merger.append(pdf)
    merger.write("supermerged.pdf")


pdfmerger(inputs)
# Use this command to run: python pdfmerger.py dummy.pdf twopage.pdf
