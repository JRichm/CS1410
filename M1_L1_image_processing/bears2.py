from PIL import Image

file_in = './starr_bears.jpg'
file_out = './bears2.jpg'

image = Image.open(file_in)
new_image = image.convert("L")

new_image.save(file_out)
