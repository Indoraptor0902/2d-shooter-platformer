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

class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True
    
    def img(self):
        return self.images[int(self.frame / self.img_duration)]