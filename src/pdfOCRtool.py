from os import makedirs, path
from shutil import rmtree
from tkinter import filedialog
import tkinter
import subprocess
from splitPdf import splitPages
from pdfToImage import convertToImage
from imageToPdf import combineToPdf

filename=''
dirname=''

root = tkinter.Tk()
root.title("PDF OCR Tool")

tkinter.Label(root, text="Choose input PDF file: ").grid(row=0)
def filebrowsefunc():
    global filename
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    filepathlabel.config(text=filename)
filebrowsebutton = tkinter.Button(root, text="Browse", command=filebrowsefunc)
filebrowsebutton.grid(row=0, column=1)
filepathlabel = tkinter.Label(root)
filepathlabel.grid(row=0, column=2)

tkinter.Label(root, text="Select save folder: ").grid(row=1)
def dirbrowsefunc():
    global dirname
    dirname = filedialog.askdirectory()
    dirpathlabel.config(text=dirname)
dirbrowsebutton = tkinter.Button(root, text="Browse", command=dirbrowsefunc)
dirbrowsebutton.grid(row=1, column=1)
dirpathlabel = tkinter.Label(root)
dirpathlabel.grid(row=1, column=2)

def runTool():
    inputPath = filename
    outputPrefix = "temp/pdfs/page-"
    try:
        if path.isdir("temp"):
            rmtree("temp")

        makedirs("temp/pdfs")
        numPages = splitPages(inputPath, outputPrefix)
        
        makedirs("temp/images")
        paths = []
        for page in range(numPages):
            pdfPath = "temp/pdfs/page-" + str(page) + ".pdf"
            pngPath = "temp/images/page-" + str(page)
            convertToImage(pdfPath, pngPath)
            paths.append(pngPath + ".png")
            print("Converted image #%s" %page)
        print("Converted all pages to images")

        pdfPathWithoutOCR = "temp/withoutOCR.pdf"
        combineToPdf(paths, pdfPathWithoutOCR)
        print("Creating PDF without OCR...")
        print("PDF without OCR created!")

        pdfOutputPath = dirname + "/paper.pdf"
        subprocess.run(["ocrmypdf", pdfPathWithoutOCR, pdfOutputPath])

        statuslabel.config(text="File converted and saved successfully!", bg="green")
    except Exception as err:
        print("Failed: {0}".format(err))
        statuslabel.config(text="Failed: {0}".format(err), bg="red")
    finally:
        rmtree("temp")

submitbutton = tkinter.Button(root, text="Submit and convert", command=runTool)
submitbutton.grid(row=3, column=1)
statuslabel = tkinter.Label(root)
statuslabel.grid(row=4, column=1)

if __name__ == "__main__":
    root.mainloop()