from PIL import Image

def upscaling(take, upscale):

    im = Image.open(take)


    up_w = int(im.width * upscale)
    up_h = int(im.height * upscale)

    resize = im.resize((up_w, up_h), Image.Resampling.LANCZOS)


    resize.save(f'2z_{im.name}')


take = input('Image path: ')
upscale = int(input('Upscale how many times? '))
upscaling(take, upscale)