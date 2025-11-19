import PyPDF2  # type: ignore

with open("./PDF/dummy.pdf", "rb") as file:
    # 'rb' is read binary, for pdf we append 'b' to it.
    # so it converts the file to binary and PyPDF2 works with binary files.
    reader = PyPDF2.PdfReader(file)
    print(file)  # <_io.BufferedReader name='./PDF/dummy.pdf'>
    print(reader)  # <PyPDF2._reader.PdfReader object at 0x7b067d030350>
    print(reader.pages)  # <PyPDF2._page._VirtualList object at 0x7b067c65be30>

    page = reader.pages[0]
    print(
        page
    )  # {'/Type': '/Page', '/Parent': IndirectObject(4, 0, 135267797369680), '/Resources': IndirectObject(11, 0, 135267797369680), '/MediaBox': [0, 0, 595, 842], '/Group': {'/S': '/Transparency', '/CS': '/DeviceRGB', '/I': True}, '/Contents': IndirectObject(2, 0, 135267797369680)}
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)

    with open("./PDF/rotated.pdf", "wb") as new_file:
        writer.write(new_file)
