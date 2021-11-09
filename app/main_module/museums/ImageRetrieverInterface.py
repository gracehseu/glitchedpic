import requests

from app.main_module.DateUtil import getTodaysDateAsString


class ImageRetrieverInterface():

    def __init__(self):
        self.name = None

    def get_image(self):
        return self.name
    
    def save_image(self, saved_image_name, url):
        # saved_image_name = "{}.jpeg".format(title)
        saved_image_name = saved_image_name.strip("\"")
        getImage = requests.get(url)
        if getImage.status_code == 200:
            with open("{image_location}/{date}.jpeg".format(image_location=self.image_location, date=getTodaysDateAsString(), image_name=saved_image_name), 'wb') as f:
                f.write(getImage.content)