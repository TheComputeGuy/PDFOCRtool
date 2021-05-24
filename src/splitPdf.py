from PyPDF2 import PdfFileWriter, PdfFileReader

def splitPages(inputPath, outputPrefix):
    inputpdf = PdfFileReader(open(inputPath, "rb"))

    numPages = inputpdf.numPages

    for i in range(numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(outputPrefix + "%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
    print("Written %s pdf pages" % numPages)
    return numPages

def test():
    from os import mkdir
    inputPath = "test/original.pdf"
    outputPrefix = "temp/page-"

    try:
        mkdir("temp")
    except FileExistsError:
        print("temp directory exists")

    splitPages(inputPath, outputPrefix)