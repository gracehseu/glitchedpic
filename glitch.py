from PIL import Image
import numpy

def transform(image):

    im = Image.open(image)
    im1 = im.transpose(Image.FLIP_LEFT_RIGHT)
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
    transform("starrynight.jpg")
