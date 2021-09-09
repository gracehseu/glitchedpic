from glitches.ImageGlitcherInterface import ImageGlitcherInterface
from PIL import Image
import numpy as np
import random

class randomPixelSwap(ImageGlitcherInterface):

    def __init__(self):
        self.image_glitch_type = "random pixel swap"

    def glitch_image(self, image_name):
        print(str(image_name))
        im = Image.open("images/" + image_name)

        image_arr = np.asarray(im).copy()

        im_width, im_height = im.size
        print(im_width, im_height)

        # only swap like 1/8 of the image
        num_swap = int(im_width * im_height / 8)
        for i in range(num_swap):
            swap_height_1 = random.randint(0, im_height - 1)
            swap_width_1 = random.randint(0, im_width - 1)
            swap_height_2 = random.randint(0, im_height - 1)
            swap_width_2 = random.randint(0, im_width - 1)
            image_arr[swap_height_2][swap_width_2], image_arr[swap_height_1][swap_width_1] = image_arr[swap_height_1][swap_width_1], image_arr[swap_height_2][swap_width_2]

        new_image = Image.fromarray(image_arr, 'RGB')
        self.save_image(self.image_glitch_type + image_name, new_image)
