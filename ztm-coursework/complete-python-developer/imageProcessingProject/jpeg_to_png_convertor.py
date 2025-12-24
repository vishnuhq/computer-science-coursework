import sys
import os
from PIL import Image

# grab the first and second arguments
# 1. Pokedex/
# 2. new/
source_dir = sys.argv[1]
destination_dir = sys.argv[2]

# check if destination folder exists, if not create new folder
if os.path.isdir(destination_dir):
    pass
else:
    current_dir = os.getcwd()
    path = os.path.join(current_dir, destination_dir)
    os.mkdir(path)

# loop through source folder jpg files and convert then to png and save to destination folder
for filename in os.listdir(source_dir):
    if filename.endswith(".jpg"):
        image_path = os.path.join(source_dir, filename)
        img = Image.open(image_path)
        new_path = destination_dir + filename[:-4] + ".png"
        img.save(new_path, "png")

# SOLUTION FROM THE COURSE
# import sys
# import os
# from PIL import Image
#
# path = sys.argv[1]
# directory = sys.argv[2]
#
# if not os.path.exists(directory):
#     os.makedirs(directory)
#
# for filename in os.listdir(path):
#     clean_name = os.path.splitext(filename)[0]
#     img = Image.open(f'{path}{filename}')
#     # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
#     img.save(f'{directory}/{clean_name}.png', 'png')
#     print('all done!!')
