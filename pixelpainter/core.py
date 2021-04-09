from PIL import ImageTk, Image
from .libs import *
import numpy as np
import pyperclip
import argparse
import os


def user():
    return os.path.join('C:', os.environ["HOMEPATH"], "Desktop")


class Image2HTML(object):
    """docstring for Image2HTML"""

    def __init__(self, image, pixsize, outfolder):
        super(Image2HTML, self).__init__()
        self.outfolder = outfolder
        self.IMG = Image.open(image, 'r')
        self.IMG = self.IMG.convert("RGBA")

        self.WIDTH, self.HEIGHT = self.IMG.size

        RGBC = list(self.IMG.getdata())                        # RGB COLORS
        HEXC = ['#%02x%02x%02x%02x' % color for color in RGBC]  # HEX COLORS

        MATRIX = np.array(HEXC).reshape(self.HEIGHT, self.WIDTH)
        self.HTMLCODE = Array2Table(MATRIX, pixsize)

    def Save(self):
        path = os.path.join(self.outfolder, "FILE.html")
        FOut = open(path, "w")
        FOut.write(self.HTMLCODE)
        FOut.close()
        print("HTML file saved correctly!")

    def Get(self):
        pyperclip.copy(self.HTMLCODE)
        print("HTML code copied correctly!")


def main():
    analyser = argparse.ArgumentParser(description='Convert images to HTML.')

    # IMAGE PATH ARGUMENT
    analyser.add_argument(
        '-i', '--image',
        required=True,
        type=str,
        help="Absolute path of the image to be processed."
    )

    # PIXEL SIZE ARGUMENT
    analyser.add_argument(
        '-ps', '--pixelsize',
        default=2,
        type=int,
        help="Pixel size."
    )

    # OUTPUT FOLDER
    analyser.add_argument(
        '-f', '--folder',
        default=user(),
        type=str,
        help="Output folder to HTML file (in case of using -save mode in --mode argument) The default save folder is the desktop."
    )

    # MODE ARGUMENT
    analyser.add_argument(
        '-m', '--mode',
        default="save",
        choices=["save", "copy"],
        help="Copy the generated code to clipboard (copy) or generate a HTML file (save)."
    )

    prms = analyser.parse_args()

    I2H = Image2HTML(prms.image, prms.pixelsize, prms.folder)
    if prms.mode == 'copy':
        I2H.Get()
    elif prms.mode == 'save':
        I2H.Save()


if __name__ == '__main__':
    main()
