from image_glitcher import image_glitcher
from PIL import Image
import random
import numpy

class flip_image_and_combine(image_glitcher):

    def __init__(self):
        self.image_glitch_type = "flip_image_and_combine"

    def glitch_image(self, image):
        print(str(image))
        im = Image.open(image)
        transformations = [Image.FLIP_LEFT_RIGHT, Image.FLIP_TOP_BOTTOM]
        im1 = im.transpose(random.choice(transformations))
        # im.show()
        # im1.show()

        orig_img = numpy.asarray(im)
        flip_img = numpy.asarray(im1)

        for i in range(0, len(orig_img), 2):
            orig_img[i] = flip_img[i]

        new_img = Image.fromarray(orig_img)
        new_img.save("altered" + image)

        Image.open("altered" + image).show()

    