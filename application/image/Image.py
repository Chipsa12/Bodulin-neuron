import base64
import re


class Image:
    def __init__(self, name, binary, formatImg):
        self.name = name
        self.binary = binary
        self.formatImg = formatImg

    @staticmethod
    def decodeImage(imageName, encryptedImage):
        result = re.split(r",", encryptedImage, maxsplit=1)
        imageFormat = ""
        binaryImage = base64.b64decode(result[1])
        if "image/jpeg" in result[0]:
            imageFormat = "jpeg"
        elif "image/png" in result[0]:
            imageFormat = "png"
        return Image(imageName, binaryImage, imageFormat)
