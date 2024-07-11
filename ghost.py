#!/usr/bin/env python3

"""
Stanford CS106A Ghost Project
"""

import os
import sys

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage


def pix_dist2(pix1, pix2):
    """
    Returns the square of the color distance between 2 pix tuples.
    >>> pix_dist2((2, 5, 6), (1, 3, 5))
    6
    >>> pix_dist2((5, 4, 3), (3, 2, 1))
    12
    """
    distance = ((pix1[0]-pix2[0])**2) + ((pix1[1]-pix2[1])**2) + ((pix1[2]-pix2[2])**2)
    return distance


def avg_pix(pixs):
    """
    Given a list of 1 or more pix, returns the best pix.
    >>> avg_pix([(3, 2, 3), (6, 5, 6), (7, 8, 9), (10, 13, 12)])
    (6.5, 7.0, 7.5)
    >>> avg_pix([(6, 8, 2), (3, 4, 6), (3,9,4)])
    (4.0,7.0,4.0)
    """
    r_count = 0
    g_count = 0
    b_count = 0

    for i in range(len(pixs)):
        p = pixs[i]
        r_count += p[0]
        g_count += p[1]
        b_count += p[2]

    avg = (r_count/len(pixs),g_count/len(pixs),b_count/len(pixs))
    return avg

def best_pix(pixs):
    """
    Given a list of 1 or more pix, returns the best pix.
    >>> best_pix([(1, 1, 1), (1, 1, 1), (28, 28, 28)])
    (1,1,1)
    >>> best_pix([(1, 1, 1), (1, 1, 1), (1,1,1) (28, 28, 28)])
    (1,1,1)
    """
    return min(pixs, key=lambda pix:pix_dist2(pix, avg_pix(pixs)))


def good_apple_pix(pixs):
    """
    Given a list of 2 or more pix, return the best pix
    according to the good-apple strategy.
    >>> good_apple_pix([(18, 18, 18), (20, 20, 20), (20, 20, 20), (20, 20, 20), (0, 2, 0), (1, 0, 1)])
    (20, 20, 20)
    """

    f = sorted(pixs, key=lambda pix:pix_dist2(pix, avg_pix(pixs)))
    good = f[:(len(f)//2)]
    return best_pix(good)


def pix_at_xy(images, x, y):

    ls= []
    for image in images:
        pixel = image.get_pix(x,y)
        ls.append(pixel)
    return ls



''
def solve(images, mode):
    """
    Given a list of image objects and mode,
    compute and show a Ghost solution image based on these images.
    Mode will be None or '-good'.
    There will be at least 3 images and they will all be
    the same size.
    """
    out = SimpleImage.blank(images[0].width, images[0].height)
    for x in range(out.width):
        for y in range(out.height):
            if mode == None:
                out.set_pix(x, y, best_pix(pix_at_xy(images, x, y)))
            if mode == '-good':
                out.set_pix(x, y, good_apple_pix(pix_at_xy(images, x, y)))
    out.show()


def jpgs_in_dir(dir):
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = SimpleImage.file(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # Command line args
    # 1 arg:  dir-of-images
    # 2 args: -good dir-of-images
    if len(args) == 1:
        images = load_images(args[0])
        solve(images, None)

    if len(args) == 2 and args[0] == '-good':
        images = load_images(args[1])
        solve(images, '-good')


if __name__ == '__main__':
    main()
