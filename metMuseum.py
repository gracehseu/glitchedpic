import requests
search_query = "https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&hasImages=true&q=sunflowers"

def queryForObject(objectId):
    query_for_object = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"
    return query_for_object + str(objectId)


def getMetImage():
    r = requests.get(search_query)
    information = r.json()
    # print(information)
    object_id_list = information["objectIDs"]
    imageSave = requests.get(queryForObject(object_id_list[3]))
    imageSaveResponse = imageSave.json()
    imageUrl = imageSaveResponse["primaryImage"]
    # print(imageUrl)
    saved_image = "{}.jpeg".format(imageSaveResponse["title"])
    getImage = requests.get(imageUrl)
    if getImage.status_code == 200:
        with open(saved_image, 'wb') as f:
            f.write(getImage.content)
    return saved_image
