"""
Base GameObject Class for creating a game object.
"""

import pygame

class GeneralObject:
    def __init__(self, x, y, w, h, rotate_angle=0):
        self.rect = pygame.Rect(x, y, w, h)
        self.rotate_angle = rotate_angle

    @property
    def left(self):
        """
        Return left-x coordinate of Rect object 
        """
        return self.rect.left

    @property
    def right(self):
        """
        Return right-x coordinate of Rect object 
        """
        return self.rect.right

    @property
    def top(self):
        """
        Return top-y coordinate of Rect object 
        """
        return self.rect.top

    @property
    def bottom(self):
        """
        Return bottom-y coordinate of Rect object 
        """
        return self.rect.bottom

    @property
    def width(self):
        """
        Return width of Rect object 
        """
        return self.rect.width

    @property
    def height(self):
        """
        Return height of Rect object 
        """
        return self.rect.height

    @property
    def center(self):
        return self.rect.center

    @property
    def centerx(self):
        return self.rect.centerx

    @property
    def centery(self):
        return self.rect.centery

    def draw(self, surface):
        pass

    def move(self, dx, dy):
        pass
        #self.rect = self.rect.move(dx, dy)

    def update(self):
        pass
        """
        Rotating an object at a specified angle
        """
        #if self.rotate_angle == 0:
            #return

        #print('Rotating')

        #pygame.transform.rotate(self.rect, self.rotate_angle)