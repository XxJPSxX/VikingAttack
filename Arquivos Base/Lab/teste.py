__author__ = '115031035'
from pygame import  *
screen = pygame.display.set_mode((480, 360))
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

# render text
label = myfont.render("Some text!", 1, (255,255,0))
screen.blit(label, (100, 100))