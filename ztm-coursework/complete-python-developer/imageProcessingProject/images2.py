from PIL import Image, ImageFilter

img = Image.open("./astro.jpg")
print(img.size)
new_img = img.resize((400, 400))
print(new_img.size)
new_img.show()
