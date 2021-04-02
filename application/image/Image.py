import base64
import re


class Image:
    def __init__(self, name, binary):
        self.name = name
        self.binary = binary

    @staticmethod
    def decodeImage(imageName, encryptedImage):
        result = re.split(r",", encryptedImage, maxsplit=1)
        binaryImage = base64.b64decode(result[1])
        return Image(imageName, binaryImage)
