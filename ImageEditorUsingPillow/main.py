from PIL import Image , ImageFilter , ImageEnhance

with Image.open("red.JPG") as picture:
    #picture.show()
    black_white = picture.convert("L")
    black_white.save("Grey.jpg")

    mirror = picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save("Mirror.JPG")

    blur = picture.filter(ImageFilter.BLUR)
    blur.show()