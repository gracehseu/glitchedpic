from PIL import Image
import numpy
import metMuseum
import random

def transform(image):

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

if __name__ == '__main__':
    # transform("starrynight.jpg")
    # transform("Wheat Field with Cypresses.jpeg")
    image_to_transform = metMuseum.getMetImage()
    transform(image_to_transform)
