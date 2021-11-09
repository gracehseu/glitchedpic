import requests
import random

# top 100 photos
from app.main_module.museums.ImageRetrieverInterface import ImageRetrieverInterface

search_query = "https://api.artic.edu/api/v1/artworks/search?query[term][is_public_domain]=true&limit=100&fields=id,title,image_id"


def queryForObject(objectId):
    query_for_object = "https://api.artic.edu/api/v1/artworks/" + str(objectId) + "?fields=id,title,image_id"
    return query_for_object


class ArtInstituteChicagoRetriever(ImageRetrieverInterface):

    def get_image(self):
        search_query_result = requests.get(search_query)
        search_query_json = search_query_result.json()
        # print(information)
        object_id_list = search_query_json["data"]

        random_image = random.choice(object_id_list)

        image_result = requests.get(queryForObject(random_image["id"]))

        image_json = image_result.json()
        # print(image_json)
        saved_image_name = "{}.jpeg".format(image_json["data"]["title"])

        image_url = image_json["config"]["iiif_url"] + "/" + image_json["data"]["image_id"] + "/full/843,/0/default.jpg"
        # get_image = requests.get(image_url)

        # if get_image.status_code == 200:
        #     with open(saved_image_name, 'wb') as f:
        #         f.write(get_image.content)
        self.save_image(saved_image_name, image_url)
        self.name = saved_image_name
