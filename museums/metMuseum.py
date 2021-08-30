from museums.ImageRetrieverInterface import ImageRetrieverInterface
import requests
search_query = "https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&hasImages=true&q=sunflowers"

def queryForObject(objectId):
    query_for_object = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
    return query_for_object + str(objectId)

class MetMuseumRetriever(ImageRetrieverInterface):

    def get_image(self):
        search_query_result = requests.get(search_query)
        search_query_json = search_query_result.json()
        # print(information)
        object_id_list = search_query_json["objectIDs"]
        object_id_result = requests.get(queryForObject(object_id_list[3]))
        image_json = object_id_result.json()
        image_url = image_json["primaryImage"]
        # print(imageUrl)
        saved_image_name = "{}.jpeg".format()
        # getImage = requests.get(imageUrl)
        # if getImage.status_code == 200:
        #     with open(saved_image_name, 'wb') as f:
        #         f.write(getImage.content)
        self.save_image(saved_image_name, image_url)
        self.name = saved_image_name
