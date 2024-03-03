# import PyPDF2
# a= PyPDF2.PdfReader("Python course outline.pdf")
# print(a.metadata)
# from PyPDF2 import PdfReader

# reader = PdfReader("Python course outline.pdf")
# page = reader.pages[0]
# print(page.extract_text())

# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
#im = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg")
im = Image.open(r"C:\Users\ayazb\OneDrive\Desktop\new.png")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
newsize = (200, 200)
im1 = im1.resize(newsize)
# Shows the image in image viewer
im1.show()


