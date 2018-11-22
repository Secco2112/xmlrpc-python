import requests
import os

class ImageWebCrawler:
    def __init__(self):
        self._url = "" # Initial url to retrieve list of images
        self._path_to_download = ""

    def setUrl(self, iiu):
        self._initial_image_url = iiu
        return self

    def getUrl(self):
        return self._initial_image_url

    def setPathToDownload(self, ptd):
        self._path_to_download = ptd
        self.repositoryExists()
        return self

    def getPathToDownload(self):
        return self._path_to_download

    def repositoryExists(self, return_value=False):
        if return_value:
            return os.path.isdir(self.getPathToDownload())
        else:
            if os.path.isdir(self.getPathToDownload()) == False:
                raise Exception("The directory \"%s\" don't exists" %self.getPathToDownload())

    def downloadImage(self, image_url):
        self.repositoryExists()

        img_data = requests.get(image_url).content
        with open('image_name.jpg', 'wb') as handler:
            handler.write(img_data)

