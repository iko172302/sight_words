import pygame

##Screen settings##
display_width = 800
display_height = 600
background_blue = (8, 156, 204)
background_light_green = (144, 238, 144)
text_black = (0, 0, 0)
screen = pygame.display.set_mode((display_width, display_height))

##Misc colors##
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

##Game clock / FPS## 
clock = pygame.time.Clock()

##Music & sounds##
pygame.init()
the = pygame.mixer.Sound("the.wav")
ambient = pygame.mixer.music.load('Dancing_on_Green_Grass.mp3')

def play_ambient():
	ambient
	pygame.mixer.music.play(-1)

##Word player function##
def play_sounds(word):
	pygame.mixer.Sound.play(word)

def settings(): 		
	#defines the window title caption
	pygame.display.set_caption("Grace's Sight Words Game")

##Text to screen functions##
def opening_message():
	basicfont = pygame.font.SysFont(None, 48)
	text = basicfont.render('Click to Start!', True, (255, 255, 0), (8, 156, 204))
	textrect = text.get_rect()
	screen.blit(text, (300, 350))

def directions_message1():
	basicfont = pygame.font.SysFont(None, 48)
	text = basicfont.render('In this game you will ', True, (127, 127, 127), (144, 238, 144))
	textrect = text.get_rect()
	screen.blit(text, (50, 150))

def directions_message2():
	basicfont = pygame.font.SysFont(None, 48)
	text = basicfont.render('listen to the sight word ', True, (127, 127, 127), (144, 238, 144))
	textrect = text.get_rect()
	screen.blit(text, (75, 200))

def directions_message3():
	basicfont = pygame.font.SysFont(None, 48)
	text = basicfont.render('then choose the correct box!', True, (127, 127, 127), (144, 238, 144))
	textrect = text.get_rect()
	screen.blit(text, (100, 250))

def opening_message2():
	basicfont = pygame.font.SysFont(None, 48)
	text = basicfont.render('Click to Start!', True, (30, 144, 255), (144, 238, 144))
	textrect = text.get_rect()
	screen.blit(text, (300, 500))
	
def start_button(x,y):
	screen.blit(play_button, (x,y))



