from pypdf import PdfReader,PdfWriter,PdfMerger
import os

#Splitting pdf pages

input_pdf=PdfReader(input('Enter pdf path :'))

print("split operation is in proccess")

for index,page in enumerate(input_pdf.pages):
    output = PdfWriter()
    output.add_page(page)
    output.write(f"{index+1}-page.pdf")

print("Split operation completed")

#Merging pdf files

print("Merge operation in process ")

output=PdfMerger()

merge_path = input("Enter path to be merged : ")
for pdf in os.listdir(merge_path):
    if(pdf.endswith(".pdf")):
         pdf_file=PdfReader(f'{merge_path}\\' +pdf)
         output.append(pdf_file)
         print(pdf)
output.write('merged.pdf')

print("Merge operation completed")

#Crop the pdf file

cropinput=PdfReader('merged.pdf')
print("croping on process")

cropoutput=PdfWriter()

single_page=cropinput.pages[0]

single_page.mediabox.upper_left=[550,0]

single_page.mediabox.lower_right=[50,112]

cropoutput.add_page(single_page)

cropoutput.write('crop.pdf')

print("cropping successfull")

#tilting the pdf page

tilt_output=PdfWriter()
print("Tilting is in process")
tilt_page=cropinput.pages[2]
tilt_page.rotate(270)
tilt_output.add_page(tilt_page)
tilt_output.write('tilt.pdf')
print("Tilt successfull")



