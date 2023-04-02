from PIL import Image, ImageFilter, ImageOps
import os

path = r"C:\Users\murabıt\Desktop"
pathOut = r"C:\Users\murabıt\Desktop\editedImgs"

if not os.path.exists(pathOut):
    os.mkdir(pathOut)

img = Image.open(f"{path}/img.jpg")

pink_img = ImageOps.colorize(img.convert('L'), black="white", white="pink")
clean_name = os.path.splitext("img.jpg")[0]
pink_img.save(f"{pathOut}/{clean_name}_pink.jpg")
