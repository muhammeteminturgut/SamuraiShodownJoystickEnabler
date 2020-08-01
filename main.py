import ctypes
ctypes.windll.user32.SetProcessDPIAware()
import pygame
import os
import keyboard
GREEN = pygame.Color('green')
BLACK = pygame.Color('black')

class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, GREEN)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode((350, 200))
pygame.display.set_caption("SAMSHO JoyEnabler")
quitProgram = False
clock = pygame.time.Clock()
pygame.joystick.init()
textPrint = TextPrint()
joystick_count=0
while not quitProgram:
    screen.fill(BLACK)
    textPrint.reset()
    textPrint.tprint(screen,"Samurai Shodown 2019 Joystick Enabler v0.1")
    textPrint.tprint(screen,"Muhammet Emin TURGUT | 01.07.2020")
    textPrint.tprint(screen," ")
    joystick_count = pygame.joystick.get_count()
    textPrint.tprint(screen,"{} Joystick Detected".format(joystick_count))
    if joystick_count==1:
        pygame.joystick.Joystick(0).init()
        textPrint.tprint(screen,"Joystick 1 succesfully initalized.")
        textPrint.tprint(screen," ")
        textPrint.tprint(screen,"Now you can start Samurai Shodown.")
    elif joystick_count==2:
        pygame.joystick.Joystick(0).init()
        textPrint.tprint(screen,"Joystick 1 succesfully initalized.")
        pygame.joystick.Joystick(1).init()
        textPrint.tprint(screen,"Joystick 2 succesfully initalized.")
        textPrint.tprint(screen," ")
        textPrint.tprint(screen,"Now you can start Samurai Shodown.")
    elif joystick_count<=0:
        keyboard.add_hotkey("enter", lambda: os._exit(0))
        textPrint.tprint(screen,"No Joystick Detected. Press enter to exit.")
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitProgram = True
            
        if event.type == pygame.JOYAXISMOTION:
            if event.joy==0:
                if int(event.value)==-1 and event.axis==1:
                    keyboard.press("up")
                if event.value>-1 and event.value<0 and event.axis==1:
                    keyboard.release("up")
                    
                if int(event.value)==1 and event.axis==1:
                    keyboard.press("down")
                if event.value<1 and event.value>-0.5 and event.axis==1:
                    keyboard.release("down")
                    
                if int(event.value)==1 and event.axis==0:
                    keyboard.press("right")
                if event.value<1 and event.value>-0.5 and event.axis==0:
                    keyboard.release("right")
                    
                if int(event.value)== -1 and event.axis==0:
                    keyboard.press("left")
                if event.value>-1 and event.value<0 and event.axis==0:
                    keyboard.release("left")
            if event.joy==1:
                if int(event.value)==-1 and event.axis==1:
                    keyboard.press("h")
                if event.value>-1 and event.value<0 and event.axis==1:
                    keyboard.release("h")
                    
                if int(event.value)==1 and event.axis==1:
                    keyboard.press("n")
                if event.value<1 and event.value>-0.5 and event.axis==1:
                    keyboard.release("n")
                    
                if int(event.value)==1 and event.axis==0:
                    keyboard.press("m")
                if event.value<1 and event.value>-0.5 and event.axis==0:
                    keyboard.release("m")
                    
                if int(event.value)== -1 and event.axis==0:
                    keyboard.press("b")
                if event.value>-1 and event.value<0 and event.axis==0:
                    keyboard.release("b")

        if event.type == pygame.JOYBUTTONDOWN:
            if event.joy==0:
                if event.button==0:
                    keyboard.press("7")
                if event.button==1:
                    keyboard.press("8")
                if event.button==2:
                    keyboard.press("0")
                if event.button==3:
                    keyboard.press("9")
                if event.button==4:
                    keyboard.press("p")
                if event.button==5:
                    keyboard.press("u")
                if event.button==6:
                    keyboard.press("o")
                if event.button==7:
                    keyboard.press("I")
                if event.button==8:
                    keyboard.press("space")
                if event.button==9:
                    keyboard.press("backspace")
            if event.joy==1:
                if event.button==0:
                    keyboard.press("a")
                if event.button==1:
                    keyboard.press("s")
                if event.button==2:
                    keyboard.press("f")
                if event.button==3:
                    keyboard.press("d")
                if event.button==4:
                    keyboard.press("v")
                if event.button==5:
                    keyboard.press("z")
                if event.button==6:
                    keyboard.press("c")
                if event.button==7:
                    keyboard.press("x")
                if event.button==8:
                    keyboard.press("space")
                if event.button==9:
                    keyboard.press("backspace")
        if event.type == pygame.JOYBUTTONUP:
            if event.joy==0:
                if event.button==0:
                    keyboard.release("7")
                if event.button==1:
                    keyboard.release("8")
                if event.button==2:
                    keyboard.release("0")
                if event.button==3:
                    keyboard.release("9")
                if event.button==4:
                    keyboard.release("p")
                if event.button==5:
                    keyboard.release("u")
                if event.button==6:
                    keyboard.release("o")
                if event.button==7:
                    keyboard.release("I")
                if event.button==8:
                    keyboard.release("space")
                if event.button==9:
                    keyboard.release("backspace")
            if event.joy==1:
                if event.button==0:
                    keyboard.release("a")
                if event.button==1:
                    keyboard.release("s")
                if event.button==2:
                    keyboard.release("f")
                if event.button==3:
                    keyboard.release("d")
                if event.button==4:
                    keyboard.release("v")
                if event.button==5:
                    keyboard.release("z")
                if event.button==6:
                    keyboard.release("c")
                if event.button==7:
                    keyboard.release("x")
                if event.button==8:
                    keyboard.release("space")
                if event.button==9:
                    keyboard.release("backspace")                

    pygame.display.flip()
    clock.tick(20)
pygame.quit()
