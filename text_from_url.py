import sys
import requests
import pytesseract

from nltk.corpus import words
from PIL import Image, ImageFilter
from StringIO import StringIO


_ALL_WORDS = words.words()  # we use this later


def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)


def _get_image(url):
    return Image.open(StringIO(requests.get(url).content))


if __name__ == '__main__':
    """Tool to test the raw output of pytesseract with a given input URL"""

    url = raw_input("What is the url of the image you would like to analyze?\n")

    sys.stdout.write("The raw output from tesseract with no processing is:\n\n")
    sys.stdout.write(process_image(url))