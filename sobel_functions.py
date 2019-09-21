# Daniel Holmes
# 2018/11/2
# sobel_functions.py


import math
from urllib.request import Request, urlopen
from PIL import Image


def open_image_url(url):
    """ open image from url """
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    img = Image.open(urlopen(request))
    width, height = img.size

    return img, width, height


def get_pixels(img, width, height):
    """ get pixels from an image """
    pixels = []
    for y in range(height):
        pixels.append([])
        for x in range(width):
            pixel_tuple = img.getpixel((x, y))

            pixels[y].append([pixel_tuple[0], pixel_tuple[1], pixel_tuple[2]])

    return pixels


def convert_pixels_to_grayscale(pixels, width, height):
    """ converts the pixels to grayscale """
    for y in range(height):
        for x in range(width):
            sum_rgb = 0

            for i in range(3):
                sum_rgb += pixels[y][x][i]

            avg_rgb =  int(sum_rgb/3)
            pixels[y][x] = (avg_rgb, avg_rgb, avg_rgb)

    return pixels


def get_horizontal_values(pixels, width, height):
    """ get the horizontal values of the sobel filter """
    horizontal_values = []

    stop_y = height-1
    stop_x = width-1

    for y in range(1, stop_y):
        horizontal_values.append([])
        for x in range(1, stop_x):
            value = 0

            value += pixels[y-1][x-1][0]
            value += pixels[y-1][x][0] * 2
            value += pixels[y-1][x+1][0]

            value += -pixels[y+1][x-1][0]
            value += -pixels[y+1][x][0] * 2
            value += -pixels[y+1][x+1][0]

            horizontal_values[y-1].append(value)

    return horizontal_values


def get_vertical_values(pixels, width, height):
    """ get the vertical values of the sobel filter """
    vertical_values = []

    stop_y = height - 1
    stop_x = width - 1

    for y in range(1, stop_y):
        vertical_values.append([])
        for x in range(1, stop_x):
            value = 0

            value += pixels[y-1][x-1][0]
            value += pixels[y][x-1][0] * 2
            value += pixels[y+1][x-1][0]

            value += -pixels[y-1][x+1][0]
            value += -pixels[y][x+1][0] * 2
            value += -pixels[y+1][x+1][0]

            vertical_values[y-1].append(value)

    return vertical_values


def get_new_pixels(pixels, horizontal_values, vertical_values, width, height):
    """ get the new values for each pixel """
    stop_y = height - 2
    stop_x = width - 2

    for y in range(0, stop_y):
        for x in range(0, stop_x):
            vh = math.pow(horizontal_values[y][x], 2)   # pythagorean theorem
            vv = math.pow(vertical_values[y][x], 2)     # for the vertical and horizontal values

            v = int(math.sqrt(vh+vv))

            pixels[y+1][x+1] = (v, v, v)

    return pixels


def create_image(pixels, width, height):
    """ create the PIL image """
    img = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            img.putpixel((x,y), pixels[y][x])

    return img


def sobel_from_url(image_url):
    """ Apply sobel operator to an image from a url """
    image, width, height = open_image_url(image_url)

    pixels = get_pixels(image, width, height)
    pixels = convert_pixels_to_grayscale(pixels, width, height)

    horizontal_values = get_horizontal_values(pixels, width, height)
    vertical_values = get_vertical_values(pixels, width, height)

    new_pixels = get_new_pixels(pixels, horizontal_values, vertical_values, width, height)

    sobel_image = create_image(new_pixels, width, height)

    return sobel_image
