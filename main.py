from PIL import Image, ImageFilter, ImageEnhance
import easygui
import os

def upscaling(imagePath, upscale):

    im = Image.open(imagePath)


    up_w = int(im.width * upscale)
    up_h = int(im.height * upscale)

    resize = im.resize((up_w, up_h), Image.Resampling.LANCZOS)

    sharp = ImageEnhance.Sharpness(resize)
    if upscale < 4:
        pp = sharp.enhance(7.0)
    elif upscale <= 10:
        pp = sharp.enhance(7.0 * (upscale/2))
    pp2 = pp.filter(ImageFilter.DETAIL)
    pp3 = pp2.filter(ImageFilter.SMOOTH_MORE)
    pp3 = ImageEnhance.Color(pp3).enhance(1.2)





    fileName = os.path.basename(imagePath)

    pp3.save(f'{upscale}_2z_{fileName}')


imagePath = easygui.fileopenbox()
upscale = float(input('Upscale how many times? '))
upscaling(imagePath, upscale)