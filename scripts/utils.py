import pygame
import os
from scripts.colors import *
from scripts.settings import *

pygame.init()

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    unscaled_img = pygame.image.load(BASE_IMG_PATH + path)
    img = pygame.transform.scale(unscaled_img, (unscaled_img.get_width() * IMG_SCALE, unscaled_img.get_height() * IMG_SCALE)).convert()
    img.set_colorkey(BLACK)
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))
    
    return images