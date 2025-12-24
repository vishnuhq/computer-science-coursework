from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")

print(img)
img.show()

# filtered_image = img.filter(ImageFilter.BLUR)
# filtered_image.show()
# filtered_image.save("blurredPikaPika.png", "png")

greyscale_image = img.convert("L")
greyscale_image.show()
