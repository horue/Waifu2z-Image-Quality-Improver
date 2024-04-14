from PIL import Image
import os

def upscaling(take, upscale):

    im = Image.open(take)


    up_w = int(im.width * upscale)
    up_h = int(im.height * upscale)

    resize = im.resize((up_w, up_h), Image.Resampling.LANCZOS)


    fileName = os.path.basename(take)

    resize.save(f'2z_{fileName}')


take = input('Image path: ')
upscale = float(input('Upscale how many times? '))
upscaling(take, upscale)