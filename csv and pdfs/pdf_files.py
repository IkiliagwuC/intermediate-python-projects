import PyPDF2

#open the file for reading in binary format 'rb'
f = open('Working_Business_Proposal.pdf','rb')

#pdfFileReader has been deprecated
pdf_reader = PyPDF2.PdfReader(f)

#pdf_reader.numPages does not work because it has since been deprecated
number_of_pages = len(pdf_reader.pages)
print(number_of_pages)

#select page
page_one = pdf_reader.pages[0]

#extract text from one page
page_one_text = page_one.extract_text()

print(page_one_text)

f.close()

#write to a pdf_file file
f = open('Working_Business_Proposal.pdf','rb')

#pdfFileReader has been deprecated
pdf_reader = PyPDF2.PdfReader(f)

#select page
first_page = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()

pdf_writer.add_page(first_page)

pdf_output = open('new_file.pdf', 'wb')

pdf_writer.write(pdf_output)

f.close()
pdf_output.close()


#grab all the text in a pdf_file and append to list
f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
pdf_text = []
for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    pdf_text.append(page.extract_text())

print(pdf_text)
