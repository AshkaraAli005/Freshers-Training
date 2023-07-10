import pypdfium2 as pdfium
from PIL import Image

#Pdf to Image

# Load a document
filepath = input("Enter the pdf path : ")
pdf = pdfium.PdfDocument(filepath)
# render a single page (in this case: the first one)
for i in range(len(pdf)):
    page = pdf[i]
    pil_image = page.render(scale=4).to_pil()
    pil_image.save(f"output{i}.jpg".format(i))





#convert jpg to pdf

image1 = Image.open(r'output0.jpg')
outputImage = image1.convert('RGB')
outputImage.save(r'image_to_pdf.pdf')
print("Image convert to PDF")