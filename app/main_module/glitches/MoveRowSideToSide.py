from PIL import Image
from scipy.ndimage import rotate
import random
import numpy as np

from app.main_module.glitches.ImageGlitcherInterface import ImageGlitcherInterface


class MoveRowSideToSide(ImageGlitcherInterface):

    # def __init__(self):
    #     self.image_glitch_type = "move random row from side to side"

    def glitch_image(self, image_name):
        print(str(image_name))
        im = Image.open("{}/{}".format(self.image_location, image_name))

        image_arr = np.asarray(im).copy()
        # print(image_arr)
        im_width, im_height = im.size

        # print(im_width, im_height)

        glitch_start = int(im_height * (3 / 5) + (random.randint(int(im_height * (1 / 8)), int(im_height * (1 / 7))) * (1 if random.random() < 0.5 else -1)))

        for row in range(glitch_start, glitch_start + (random.randint(int(im_height * (1 / 6)), int(im_height * (1 / 5)))), 5):

            row_shift =  random.randint(-50, 50)

            for i in range(0, 5):
                
                # shifted_arr = image_arr[row + i]
                # shifted_arr = np.roll(shifted_arr, row_shift,  axis=0)
                # image_arr[row + i] = shifted_arr
                image_arr[row + i] = shiftRow(image_arr[row + i], row_shift)


        new_image = Image.fromarray(image_arr, 'RGB')
        self.save_image(image_name, new_image)

def shiftRow(row, shift_amount):
    shifted_arr = np.roll(row, shift_amount,  axis=0)
    return shifted_arr


# def shiftColumn(col, shift_amount):
