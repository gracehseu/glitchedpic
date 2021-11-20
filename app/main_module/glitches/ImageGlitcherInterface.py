from PIL import Image

from app.main_module.DateUtil import getTodaysDateAsString
from app.main_module.image_config import IMAGE_LOCATION


class ImageGlitcherInterface:

    image_location = IMAGE_LOCATION

    def __init__(self):
        self.image_glitch_type = None


    def glitch_image(self, image_name):
        return self.image_glitch_type

    def save_image(self, image_name, new_img):
        new_img.save("{image_location}/{date}altered.jpeg".format(image_location=self.image_location, date=getTodaysDateAsString(), name=image_name))

        # Image.open("{image_location}/{date}altered.jpeg".format(image_location=self.image_location, date=getTodaysDateAsString(), name=image_name)).show()
