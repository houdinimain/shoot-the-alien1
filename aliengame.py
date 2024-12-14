import pgzrun
import random

TITLE = "shoot the alien game by houd"

score = 0

WIDTH = 500
HEIGHT = 500    


alien = Actor("alien.png")

message = ""

def draw():
    screen.clear()
    screen.fill("black")
    alien.draw()
    screen.draw.text(message,(300,10),fontsize = 30)
    screen.draw.text(str(score),(100,10),fontsize = 30)



def place_alien():
    alien.x = random.randint(50,450)
    alien.y = random.randint(50,450)


def on_mouse_down(pos):
    global message
    global score
    if alien.collidepoint(pos):
        message = "good shot"
        score = score +10
        place_alien()
        
    else:
        message = "you missed the shot"
        score = score -10

place_alien()














pgzrun.go()





























