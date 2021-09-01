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

languages=tkinter.StringVar()

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

tkinter.Label(root, text="List language codes for OCR separated by commas (corresponding traineddata has to be already installed)").grid(row=3)
languageEntry = tkinter.Entry(root, textvariable=languages, bd=5)
languageEntry.grid(row=3, column=1)
tkinter.Label(root, text="(Leave empty for English-only OCR, mention English if combined with other languages)").grid(row=4)

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
        print("Creating PDF without OCR...")
        combineToPdf(paths, pdfPathWithoutOCR)
        print("PDF without OCR created!")

        languageListRaw = languages.get().split(",")
        languageList=[]
        for language in languageListRaw:
            if(language.strip()):
                languageList.append("-l")
                languageList.append(language.strip())

        pdfOutputPath = dirname + "/paper.pdf"

        subprocess.run(["ocrmypdf", pdfPathWithoutOCR, pdfOutputPath] + languageList).check_returncode()

        print("File converted and saved successfully!")
        statuslabel.config(text="File converted and saved successfully!", bg="green")
    except Exception as err:
        print("Failed: {0}".format(err))
        statuslabel.config(text="Failed: {0}\nCheck console for more error information".format(err), bg="red")
    finally:
        rmtree("temp")

submitbutton = tkinter.Button(root, text="Submit and convert", command=runTool)
submitbutton.grid(row=6, column=1)
statuslabel = tkinter.Label(root)
statuslabel.grid(row=7, column=1)

if __name__ == "__main__":
    root.mainloop()