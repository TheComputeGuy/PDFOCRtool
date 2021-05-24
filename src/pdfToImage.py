from pdftopng import pdftopng

def convertToImage(pdf_path, png_path):
    pdftopng.convert(pdf_path, png_path)

def test():
    pdf_path = "test/original.pdf"
    png_path = "temp/paper"
    from os import mkdir
    try:
        mkdir("temp")
    except FileExistsError:
        print("temp directory exists")

    convertToImage(pdf_path, png_path)