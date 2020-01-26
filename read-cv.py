import PyPDF2 as pyPDF

#pdf file object
pdfFileObj = open('data/ba-ex10.pdf', 'rb')

#pdf rader object
pdfReader = pyPDF.PdfFileReader(pdfFileObj, strict=False)

#print number of pages in pdf
print(pdfReader.numPages)

# print text 
for page in range(pdfReader.numPages):  
	print(pdfReader.getPage(page).extractText())
	print('#'*100)

pdfFileObj.close()