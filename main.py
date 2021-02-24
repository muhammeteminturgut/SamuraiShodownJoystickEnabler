import ctypes, sys
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

is_admin=ctypes.windll.shell32.IsUserAnAdmin()
if is_admin==False:
    ctypes.windll.user32.MessageBoxW(None, "You'll need to provide administrator permission.", "Error", 0x30)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    os._exit(0)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((350, 200))
pygame.display.set_caption("SAMSHO JoyEnabler")
quitProgram = False
clock = pygame.time.Clock()
pygame.joystick.init()
textPrint = TextPrint()
joystick_count=0
joystick_keymap=(("7","8","0","9","p","u","o","I","space","backspace"),("a","s","f","d","v","z","c","x","space","backspace"))

while not quitProgram:
    screen.fill(BLACK)
    textPrint.reset()
    textPrint.tprint(screen,"Samurai Shodown 2019 Joystick Enabler v0.3")
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
            keyboard.press(joystick_keymap[event.joy][event.button])
        if event.type == pygame.JOYBUTTONUP:
            keyboard.release(joystick_keymap[event.joy][event.button])          

    pygame.display.flip()
    clock.tick(20)
pygame.quit()
