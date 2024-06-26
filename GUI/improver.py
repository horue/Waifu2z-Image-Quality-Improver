from PIL import Image, ImageFilter, ImageEnhance
import os

def upscaling(imagePath, upscale, q):
    im = Image.open(imagePath)
    if q is False:

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
        pp3 = ImageEnhance.Contrast(pp3).enhance(1.2)





        fileName = os.path.basename(imagePath)

        pp3.save(f'{upscale}_2z_{fileName}.png')

    elif q is True:
        largura, altura = im.size
        nova_largura = int(largura * upscale)
        nova_altura = int(altura * upscale)
        nova_imagem = Image.new("RGBA", (nova_largura, nova_altura), (0, 0, 0, 0)) 
        
        def escalar_quadrante(x, y, w, h):
            if w <= 1 or h <= 1: 
                cor = im.getpixel((x, y)) 
                for dx in range(int(upscale)):
                    for dy in range(int(upscale)):
                        nx = int(x * upscale) + dx
                        ny = int(y * upscale) + dy
                        if nx < nova_largura and ny < nova_altura:
                            nova_imagem.putpixel((nx, ny), cor)
            else:
                pt_medio_x = x + w // 2
                pt_medio_y = y + h // 2

                escalar_quadrante(x, y, pt_medio_x - x, pt_medio_y - y)
                escalar_quadrante(pt_medio_x, y, x + w - pt_medio_x, pt_medio_y - y)
                escalar_quadrante(x, pt_medio_y, pt_medio_x - x, y + h - pt_medio_y)
                escalar_quadrante(pt_medio_x, pt_medio_y, x + w - pt_medio_x, y + h - pt_medio_y)
    
        escalar_quadrante(0, 0, largura, altura)
        fileName = os.path.basename(imagePath)
        nova_imagem.save(f'{upscale}_2z_{fileName}.png')