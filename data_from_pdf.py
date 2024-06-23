from PyPDF2 import PdfReader

# Creating a pdf file object
pdf = open("NLTK.pdf", "rb")

# Creating pdf reader object
pdf_reader = PdfReader(pdf)

# Checking number of pages in a pdf file
print(len(pdf_reader.pages))

# Creating a page object
page = pdf_reader.pages[0]

# Finally extracting text from the page
print(page.extract_text())

# Closing the pdf file
pdf.close()
