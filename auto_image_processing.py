import os
from PIL import Image, ImageFilter, ImageOps
import zipfile
import shutil
# Automate tasks like image resizing and filtering for all the images uploaded  and save them in a zip file for download

def resize_images(src, size=(200, 200), filter='b/w', format='JPEG', ):
    print(size)
    os.makedirs(f'{src}/temp', exist_ok=True)
    print(len(os.listdir(src)))
    for file in os.listdir(src):
        if file.endswith(('jpg', 'jpeg', 'png', 'gif')):
            img = Image.open(f'{src}/{file}')
            img = img.resize(size, reducing_gap=2.0)
            # apply filter
            if filter == 'b/w':
                img = img.convert('L')
            elif filter == 'blur':
                img = img.filter(ImageFilter.GaussianBlur(5))
            elif filter == 'edges':
                img = img.filter(ImageFilter.FIND_EDGES)
            elif filter == 'contour':
                img = img.filter(ImageFilter.CONTOUR)
            elif filter == 'emboss':
                img = img.filter(ImageFilter.EMBOSS)
            elif filter == 'sharpen':
                img = img.filter(ImageFilter.SHARPEN)
            elif filter == 'smooth':
                img = img.filter(ImageFilter.SMOOTH)
            
            img.save(f'{src}/temp/{file}', format=format)
            print(f'File saved: {file}')
    # Create a zip file
    with zipfile.ZipFile(f'{src}/images.zip', 'w') as zipf:
        for file in os.listdir(f'{src}/temp'):
            zipf.write(f'{src}/temp/{file}', file)
    # Remove temp folder
    shutil.rmtree(f'{src}/temp')
    return f'{src}/images.zip'
        
if __name__ == '__main__':
    src = r'c:/users/zaid/pictures'
    resize_images(src)