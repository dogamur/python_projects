from PIL import Image, ImageFilter, ImageOps
import os

# Prompt user to enter image path
img_path = input("Enter the path of the image you want to edit: ")

# Create output directory if it doesn't exist
path_out = os.path.dirname(img_path) + "/editedImgs"
if not os.path.exists(path_out):
    os.mkdir(path_out)

# Open the image and apply colorize filter
img = Image.open(img_path)
pink_img = ImageOps.colorize(img.convert('L'), black="purple", white="pink")

# Save the edited image
clean_name = os.path.splitext(os.path.basename(img_path))[0]
pink_img.save(f"{path_out}/{clean_name}_pink.jpg")
print(f"Image saved to {path_out}/{clean_name}_pink.jpg")
