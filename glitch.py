
from flip_image_and_combine import flip_image_and_combine
import numpy
from metMuseum import met_museum_retriver

museum_list = [met_museum_retriver]
glitch_list = [flip_image_and_combine]

if __name__ == '__main__':
    # transform("starrynight.jpg")
    # transform("Wheat Field with Cypresses.jpeg")
    source = museum_list[0]()
    source.get_image()
    glitch = glitch_list[0]()
    glitch.glitch_image(source.name)
