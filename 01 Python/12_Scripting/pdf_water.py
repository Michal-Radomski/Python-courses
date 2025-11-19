import pypdf  # type: ignore


template = pypdf.PdfReader(open("./PDF/twopager.pdf", "rb"))
print(template)  # <pypdf._reader.PdfReader object at 0x71f536bfedb0>
watermark = pypdf.PdfReader(open("./PDF/water.pdf", "rb"))
print(watermark)  # <pypdf._reader.PdfReader object at 0x71f535d9cb00>
output = pypdf.PdfWriter()


for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open("./PDF/watermaked_output.pdf", "wb") as outputFile:
    print(outputFile)  # <_io.BufferedWriter name='./PDF/watermaked_output.pdf'>
    output.write(outputFile)
