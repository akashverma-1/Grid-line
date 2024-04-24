from PIL import Image, ImageFilter

image_path = "input_image.jpg"
image = Image.open(image_path)

image.show()

width, height = image.size
new_width = int(width * 0.5)  
new_height = int(height * 0.5)  
resized_image = image.resize((new_width, new_height))
resized_image.show()

left = 100
top = 100
right = 400
bottom = 400
cropped_image = image.crop((left, top, right, bottom))
cropped_image.show()

blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()

grayscale_image = image.convert("L")
grayscale_image.show()

resized_image.save("resized_image.jpg")
cropped_image.save("cropped_image.jpg")
blurred_image.save("blurred_image.jpg")
grayscale_image.save("grayscale_image.jpg")
