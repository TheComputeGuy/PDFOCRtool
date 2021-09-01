# PDF OCR Tool

PDF OCR Tool is a Python-based tool for adding OCR to PDFs. It builds up on the great work done at [OCRmyPDF](https://github.com/jbarlow83/OCRmyPDF) and [pdftopng](https://github.com/vinayak-mehta/pdftopng) and acts as a wrapper for the same on Windows. It converts the incoming PDF into images and back to PDF to strip any old data/text present and then adds the OCR layer on top of it.

## Installation

Download the appropriate ZIP file from [releases](https://github.com/Shubham-272/PDFOCRtool/releases) and unzip it.

The downloaded ZIP file consists of two batch scripts
1. setup.bat
2. install-lib.bat

Run both the scripts in the same order **with administrative privileges**. This installs the prerequisites (Chocolatey as package manager, Python 3.8, Tesseract OCR engine and Ghostscript. And the python packages ocrmypdf, pdftopng and PyPDF2)

OR

1. Clone the repository
```
git clone git@github.com:Shubham-272/PDFOCRtool.git
```
2. Ensure you have Python 3 installed (tested on Python 3.8)
3. Install dependencies and libraries (preferably via chocolatey)
```
choco install --pre tesseract -y
choco install ghostscript -y
pip install ocrmypdf pdftopng PyPDF2
```
4. The src folder has the python scripts for individual operations as well as for the overall conversion.

## Usage

The **PDF OCR Tool.exe** runs the application. It consists of two options - the input PDF file and the folder where the output PDF should be saved. The output file will have the name paper.pdf

If cloned via git, the script pdfOCRtool.py is responsible for overall operation. You can run it via a terminal as
```
python pdfOCRtool.py
```

Conversion takes time and the progress is shown in the console that opens alongside. Once the conversion is complete, the UI shows a message in green saying "File converted and saved successfully!"

In case of errors, the message is printed in the UI with a red background. Contact the maintainers with the error message for resolution.

## Additional Language Support

PDF OCR Tool is based on Tesseract OCR engine. Tesseract supports a wide range of languages (you can check the list [here](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html))

PDF OCR Tool installs only English language by default. For adding support for languages other than English, download the respective language pack (.traineddata file) from [here](https://github.com/tesseract-ocr/tessdata/) and place it in **C:\\Program Files\\Tesseract-OCR\\tessdata** (or wherever Tesseract OCR is installed).

To perform OCR on a PDF with a language other than English, specify the language(s) to be used for OCR during run time as a comma separated list.

## Changelog
v1.0.0 - Initial release, support English OCR

v1.1.0 - Added language support via arguments

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)