from PIL import Image, ImageEnhance, ImageFilter
import os

# get user input for image name
img_name = input("Enter the name of the image file (including extension): ")

# define input and output paths
path = r"C:\Users\murabıt\Desktop"
pathOut = r"C:\Users\murabıt\Desktop\editedImgs"

if not os.path.exists(pathOut):
    os.mkdir(pathOut)

# open and edit the image
img = Image.open(f"{path}/{img_name}")
edit = img.filter(ImageFilter.SHARPEN)
clean_name = os.path.splitext(img_name)[0]

# save the edited image
edit.save(f"{pathOut}/{clean_name}_edited.jpg")
