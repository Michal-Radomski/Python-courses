import PyPDF2  # type: ignore
import sys

# * Run: python3 pdf_merger.py ./PDF/dummy.pdf ./PDF/twopager.pdf

inputs = sys.argv[
    1:
]  # this will stores all the arguments passes except the first one, and store them in a list


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfMerger()
    print(merger)  # <PyPDF2._merger.PdfMerger object at 0x700ba6d34170>
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("./PDF/merged.pdf")


pdf_merger(inputs)
