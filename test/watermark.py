from PIL import Image, ImageFilter
try:
    original = Image.open("test.png")
    print("The size of the Image is: ")
    print(original.format, original.size, original.mode)
    blurred = original.filter(ImageFilter.BLUR)
    blurred.save('blurred.png')
except:
    print("Unable to load image")
