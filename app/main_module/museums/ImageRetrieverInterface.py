import requests

from app.main_module.DateUtil import getTodaysDateAsString
from app.main_module.image_config import IMAGE_LOCATION


class ImageRetrieverInterface():

    def __init__(self):
        self.name = None
        self.image_location = IMAGE_LOCATION

    def get_image(self):
        return self.name
    
    def save_image(self, saved_image_name, url):
        # saved_image_name = "{}.jpeg".format(title)
        saved_image_name = saved_image_name.strip("\"")
        print(saved_image_name)
        getImage = requests.get(url)
        if getImage.status_code == 200:
            with open("{image_location}/{date}.jpeg".format(image_location=self.image_location, date=getTodaysDateAsString(), image_name=saved_image_name), 'wb') as f:
                f.write(getImage.content)