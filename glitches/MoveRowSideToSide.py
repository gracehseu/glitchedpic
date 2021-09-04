from glitches.ImageGlitcherInterface import ImageGlitcherInterface
from PIL import Image
from scipy.ndimage import rotate
import random
import numpy as np


class MoveRowSideToSide(ImageGlitcherInterface):

    def __init__(self):
        self.image_glitch_type = "move random row from side to side"

    def glitch_image(self, image_name):
        print(str(image_name))
        image_name = "Love of Winter.jpeg"
        im = Image.open("images/" + image_name)

        image_arr = np.asarray(im).copy()
        # print(image_arr)
        im_width, im_height = im.size

        print(im_width, im_height)

        glitch_start = int(im_height * (3 / 5) + (random.randint(int(im_height * (1 / 8)), int(im_height * (1 / 7))) * (1 if random.random() < 0.5 else -1)))

        for row in range(glitch_start, glitch_start + (random.randint(int(im_height * (1 / 6)), int(im_height * (1 / 5))))):
            # print(type(image_arr))
            # print(image_arr[row])
            shifted_arr = image_arr[row]
            shifted_arr = np.roll(shifted_arr, random.randint(-50, 50))
            image_arr[row] = shifted_arr

        new_image = Image.fromarray(image_arr, 'RGB')
        self.save_image(image_name, new_image)

    