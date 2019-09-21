# Daniel Holmes
# 2018/11/2
# arguments.py


from urllib.request import Request, urlopen
from PIL import Image
from constants import MAX_PIXELS


def image_is_valid(url):
    """ Makes sure the url is a valid image """
    try:
        # Make sure the url is valid
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    except ValueError:
        return False, 'URL you entered is not valid'

    try:
        # Make sure the url is an image
        img = Image.open(urlopen(request))
    except OSError:
        return False, 'URL you entered is not an image'

    # Make sure the image is not too large
    width, height = img.size
    num_pixels = width*height

    if num_pixels > MAX_PIXELS:
        return False, f'image exceeds maximum number of pixels ({MAX_PIXELS}) you entered {num_pixels}'

    # Image is valid
    return True, None


def get_sobel_arguments(message):
    """ Get arguments for the sobel command """
    args = message.content.split(" ")
    url = " ".join(args[1:])
    return url


def get_compression_arguments(message):
    """ Get arguments for compression """
    args = message.content.split(" ")
    num_colours = int(args[1])
    url = " ".join(args[2:])

    return url, num_colours


def check_sobel_arguments(message):
    """ Check sobel arguments """
    args = message.content.split(" ")

    if len(args) > 1:
        # check if the url is an image
        url = " ".join(args[1:])
        return image_is_valid(url)

    return False


def check_compression_arguments(message):
    """ Check compression arguments """
    args = message.content.split(" ")

    if len(args) > 2:
        try:
            num_colours = int(args[1])
        except ValueError:
            return False, 'number you entered is invalid'

        if num_colours > 16:
            return False, 'number you entered is to high ('+str(num_colours)+') must be at most 16'
        elif num_colours < 2:
            return False, 'number you entered is to low ('+str(num_colours)+') must be at least 2'

        # check if the url is an image
        url = " ".join(args[2:])
        return image_is_valid(url)

    return False
