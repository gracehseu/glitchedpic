from glitches.ImageGlitcherInterface import ImageGlitcherInterface
from PIL import Image
import numpy as np
import math

class SwirlImage(ImageGlitcherInterface):
    def __init__(self):
        self.image_glitch_type = "swirl image"
        

    def glitch_image(self, image_name):
        im = Image.open("images/" + image_name)

        image_arr = np.asarray(im).copy()
        # print(image_arr)
        im_width, im_height = im.size
        print(im_width, im_height) # 1023 817

        col0 = 0.5 * (float(im_width)  - 1.0)
        row0 = 0.5 * (float(im_height) - 1.0)

        image_arr_2 = np.asarray(image_arr).copy()

        # Compute the swirl.
        for new_col in range(im_width):
            for new_row in range(im_height):
                dCol = float(new_col) - col0
                dRow = float(new_row) - row0
                r = math.sqrt(dCol * dCol + dRow * dRow)
                angle = math.pi / 256.0 * r
                old_col = int(dCol * math.cos(angle) - dRow * math.sin(angle) + col0)
                old_row = int(dCol * math.sin(angle) + dRow * math.cos(angle) + row0)

                try:

                    if (old_col >= 0) and (old_col < im_height) and (old_row >= 0) and (old_row < im_width):
                        image_arr_2[new_col][new_row] = image_arr[old_col][old_row]

                except:
                    continue
                    # print (old_col, old_row)
                    # print(im_width, im_height)
        new_image = Image.fromarray(image_arr_2, 'RGB')
        self.save_image(image_name, new_image)




        new_image = Image.fromarray(image_arr, 'RGB')
        self.save_image(image_name, image_arr_2)
