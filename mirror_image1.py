import os
from PIL import Image

path = "F:\set1"

def flip_images():
    for filename in os.listdir(path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img = Image.open(os.path.join(path, filename))
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            new_filename = "1" + filename
            img.save(os.path.join(path, new_filename))
flip_images()

