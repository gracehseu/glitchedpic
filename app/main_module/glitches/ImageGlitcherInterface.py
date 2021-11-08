from PIL import Image
from app.main_module.image_config import IMAGE_LOCATION


class ImageGlitcherInterface:
    def __init__(self):
        self.image_glitch_type = None
        self.image_location = IMAGE_LOCATION

    def glitch_image(self, image_name):
        return self.image_glitch_type

    def save_image(self, image_name, new_img):
        new_img.save("{}/altered{}".format(self.image_location, image_name))

        Image.open("{}/altered{}".format(self.image_location, image_name)).show()
