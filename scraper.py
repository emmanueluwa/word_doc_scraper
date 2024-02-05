from docx import Document

PATH_TO_FILE = ""

document = Document("PATH_TO_FILE")

text_file = open("output.txt", "w")

for para in document.paragraphs:
  print(para.text)
  text_file.write(para.text)

text_file.close()

