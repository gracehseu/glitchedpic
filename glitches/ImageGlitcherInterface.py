from PIL import Image
class ImageGlitcherInterface():
    def __init__(self):
        self.image_glitch_type = None
        

    def glitch_image(self):
        return self.image_glitch_type

    def save_image(self, image_name, image):
        new_img = Image.fromarray(image)

        new_img.save("images/altered" + image_name)

        Image.open("images/altered" + image_name).show()