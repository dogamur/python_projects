from PIL import Image, ImageEnhance, ImageFilter
import os

path = r"C:\Users\murabıt\Desktop"
pathOut = r"C:\Users\murabıt\Desktop\editedImgs"

if not os.path.exists(pathOut):
    os.mkdir(pathOut)

img = Image.open(f"{path}/img.jpg")

edit = img.filter(ImageFilter.SHARPEN)
clean_name = os.path.splitext("img.jpg")[0]
edit.save(f"{pathOut}/{clean_name}_edited.jpg")
