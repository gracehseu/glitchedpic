from app.main_module.glitches.ImageGlitcherInterface import ImageGlitcherInterface
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import random
import numpy

class FlipImageAndCombine(ImageGlitcherInterface):

    def __init__(self):
        self.image_glitch_type = "flip_image_and_combine"

    def glitch_image(self, image_name):
        print(str(image_name))
        im = Image.open("{}/{}".format(self.image_location, image_name))
        transformations = [Image.FLIP_LEFT_RIGHT, Image.FLIP_TOP_BOTTOM, Image.ROTATE_180]
        im1 = im.transpose(random.choice(transformations))
        # im.show()
        # im1.show()

        orig_img = numpy.array(im)
        flip_img = numpy.array(im1)

        # orig_img.setflags(write=1)
        # flip_img.setflags(write=1)

        for i in range(0, len(orig_img), 2):
            orig_img[i] = flip_img[i]

        orig_img = Image.fromarray(orig_img)

        self.save_image(image_name, orig_img)

    