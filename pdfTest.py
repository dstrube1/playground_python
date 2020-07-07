#pdfTest.py: read in pdf file, output the file's text
#based off of this:
#https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file

fileName = "pdfTest.pdf"
""" 
#take 1 - doesn't work:
import PyPDF2 #pip install PyPDF2
pdf_file = open(fileName)
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print (page_content)

#error: io.UnsupportedOperation: can't do nonzero end-relative seeks
"""
"""
#take 2 - works:

from tika import parser # pip install tika

raw = parser.from_file(fileName)
print(raw['content'])
"""
"""
#take 3 - works, but is much more verbose; 
#output doesn't include "undefined" field names like take 2:
#pip install pdfminer
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    #codec = 'utf-8'
    laparams = LAParams()
    #device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    #TypeError: __init__() got an unexpected keyword argument 'codec'
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()


    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)


    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

text= convert_pdf_to_txt(fileName)
print(text)
"""

#take 4 - works best so far- include field data, doesn't require separate java app:
#https://github.com/jalan/pdftotext
import pdftotext

# Load your PDF
with open(fileName, "rb") as f:
    pdf = pdftotext.PDF(f)

# How many pages?
print(len(pdf))

# Iterate over all the pages
for page in pdf:
    print(page)

#finally, take 5: pytesseract
#import pytesseract
#wait, this is for converting from images, not pdfs
#https://pypi.org/project/pytesseract/