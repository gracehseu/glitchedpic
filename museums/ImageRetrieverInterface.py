import requests

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
            with open("images/" + saved_image_name, 'wb') as f:
                f.write(getImage.content)