from PIL import Image, ImageFilter
import easygui
import os

def upscaling(take, upscale):

    im = Image.open(take)


    up_w = int(im.width * upscale)
    up_h = int(im.height * upscale)

    resize = im.resize((up_w, up_h), Image.Resampling.LANCZOS)
    pp = resize.filter(ImageFilter.EDGE_ENHANCE)


    fileName = os.path.basename(take)

    pp.save(f'{upscale}_2z_{fileName}')


take = easygui.fileopenbox()
upscale = float(input('Upscale how many times? '))
upscaling(take, upscale)