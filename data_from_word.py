from docx import Document
docs = open("ssp.docx", "rb")
document = Document(docs)

docu = ""
for para in document.paragraphs:
     docu += para.text



length = (len(docu))
print(length)
print(docu.count("a"))