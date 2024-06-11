import argparse
import qrcode 
from PIL import Image, ImageDraw, ImageFont
from OpenFolders import openFolder, getDownloadsFolders
import os

def generate_qr(url, logo=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=14,
        border=2
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    if logo:
        logo_img = Image.open(logo)
        logo_img = logo_img.convert()
        basewidth = 100
        wpercent = (basewidth / float(logo_img.size[0]))
        hsize = int((float(logo_img.size[1]) * float(wpercent)))
        logo_img = logo_img.resize((basewidth, hsize), Image.LANCZOS)

        if logo_img.mode == 'RGBA':
            logo_img = logo_img.convert('RGB')

        pos = ((img.size[0] - logo_img.size[0]) // 2, (img.size[1] - logo_img.size[1]) // 2)

        img.paste(logo_img, pos)
 

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/tienne/tienne-latin-700-normal.ttf", 16)
    text_bbox = draw.textbbox((0, 0), url, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    text_position = ((img.size[0] - text_width) // 2, 4)
 
    draw.text(text_position, url, font=font, fill="black")
    
    folder = getDownloadsFolders();
    file   = "qr"
    index  = 0

    while os.path.isfile(folder / (file+".png")):
        index+= 1
        file = file+"_"+str(index)
    
    file = file+".png"
    img.save(folder / file)

    openFolder(folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generar un código QR con bordes redondeados.')
    parser.add_argument('url', help='La URL que se desea codificar en el código QR.') 
    parser.add_argument('-l', '--logo', help='El nombre del archivo de imagen del logo a agregar al código QR.')

    args = parser.parse_args()

    generate_qr(args.url, args.logo)
