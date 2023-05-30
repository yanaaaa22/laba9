from PIL import Image
import os

input_dir = 'pic'
output_dir = 'filtered_pic'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

files = os.listdir(input_dir)

for file in files:
    if file.lower().endswith(('.jpg', '.png')):
        image_path = os.path.join(input_dir, file)

        with Image.open(image_path) as image:
            grayscale_image = image.convert('L')
            output_path = os.path.join(output_dir, file)
            grayscale_image.save(output_path)
