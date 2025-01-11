'''
import pygame
import sys
pygame.init()
clock = pygame.time.Clock()
import random

if __name__ == "__main__":

    counter = 0
    #this creates a window 600 pixels wide by 400 pixels high
    window1 = pygame.display.set_mode((600, 400))

    #sets the caption in the left cover of the window
    pygame.display.set_caption("Game")

    #loads the robot image & starting position of image
    robot = pygame.image.load("robot.png")

    #initial position of the robot
    x = 0
    y = 360-robot.get_height()

    #initial position of the bolt
    y1 = 0
    x1 = random.randint(30, 570)

    #loads the bolt image 
    bolt = pygame.image.load("bolt.png")
    rect1 = robot.get_rect()
    rect2 = bolt.get_rect()

    #the robot starts not moving
    to_right = False
    to_left = False
    to_up = False
    to_down = False
        
    while True:
        #loads the background image
        bg = pygame.image.load("background2.png")
        window1.blit(bg, (0, 0))
        #score
        font1 = pygame.font.SysFont("Times New Roman", 30)
        text1 = font1.render("Score: "+ str(counter), True, (36, 38, 37))
        window1.blit(text1,(10, 5))

        #gets the rectangle around the robot and the bolt
        rectangle1 = pygame.Rect(x, y, robot.get_width(), robot.get_height())
        rectangle2 = pygame.Rect(x1, y1, bolt.get_width(), bolt.get_height())

        #returns true if the 2 rectangles overlap with each other
        if rectangle1.colliderect(rectangle2):
            y1 = 0
            x1 = random.randint(30, 570)
            counter += 1

        #if the bolt reaches 
        if y1 == 400:
            y1 = 0
            x1 = random.randint(30, 570)
        y1 += 5
        for event in pygame.event.get():
            #controls for when pressing the key down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True
                if event.key == pygame.K_UP:
                    to_up = True
                if event.key == pygame.K_DOWN:
                    to_down = True

            #controls for when no key is pressed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    to_left = False
                if event.key == pygame.K_RIGHT:
                    to_right = False
                if event.key == pygame.K_UP:
                    to_up = False
                if event.key == pygame.K_DOWN:
                    to_down = False
                    
            #if you click on x to close the window, it will quit without freezing 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        #keeps the robot from going off the left or right of the screen
        if x+robot.get_width() <= robot.get_width():
            x = 0 
        if x+robot.get_width() >= 600:
            x = 600 - robot.get_width()

        #keeps the robot from going off the ground which is at 360 pixels
        
        if y+robot.get_height() <= 360:
            y = 360 
        if y+robot.get_height() >= 360:
            y = 360 - robot.get_height()
        
        #if left or right arrow is pressed, moves robot 5 pixels left or right
        if to_right:
            x += 5
        if to_left:
            x -= 5
        #if up or down arrow is pressed, moves robot 5 pixels up or down
        if to_down:
            y += 5
        if to_up:
            y -= 5

        #prints everything to the window
        window1.blit(robot,(x, y))
        window1.blit(bolt, (x1, y1))
        pygame.display.flip()
        clock.tick(160)
'''
import pygame
import sys
pygame.init()

def main():
    #importing the game screen 
    import test2
    import test3
    #this creates a window 600 pixels wide by 400 pixels high
    window = pygame.display.set_mode((600, 400))
    
    #sets the caption in the left cover of the window 
    pygame.display.set_caption("Menu")

    #loads the background image
    bg = pygame.image.load("background.jpg")
    window.blit(bg, (0, 0))

    #this creates the text for the title
    font1 = pygame.font.SysFont("Times New Roman", 60)
    text1 = font1.render("Main Menu Screen", True, (36, 38, 37))
    window.blit(text1,(70, 20))

    while True:
        #gets the current position of the mouse on the screen
        mouse = pygame.mouse.get_pos()
        

        for event in pygame.event.get():
           #if you click on x to close the window, it will quit without freezing 
           if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
           #when you press the button down in the rectangular areas
           if event.type == pygame.MOUSEBUTTONDOWN:
               #if you click play button, it goes to the game
               if 350 > mouse[0] > 200 and 175 > mouse[1] > 125:
                   test2.game()
                   sys.exit()
               #if you click help button, it goes to the game
               if 350 > mouse[0] > 200 and 275 > mouse[1] > 225:
                   test3.help()
                   sys.exit()
               #if you click quit button, it exits the program
               if 350 > mouse[0] > 200 and 375 > mouse[1] > 325:
                   pygame.quit()
                   sys.exit()
               #if you click on the play music button, it plays the music
               if 575 > mouse[0] > 425 and 300 > mouse[1] > 250:
                   pygame.mixer.music.load('AmongUs.mp3')
                   pygame.mixer.music.play()
               #if you click on the pause music button, it pauses the music
               if 575 > mouse[0] > 425 and 410 > mouse[1] > 350:
                   pygame.mixer.music.pause()
                   

        #if you hover over the play button it turns light blue, otherwise it is dark blue
        if 350 > mouse[0] > 200 and 175 > mouse[1] > 125:
            play_button = pygame.draw.rect(window, (141, 183, 247), [200, 125, 150, 50])
            font2 = pygame.font.SysFont("Times New Roman", 30)
            text2 = font2.render("Play Button", True, (235, 12, 45))
        else:
            play_button = pygame.draw.rect(window, (141*0.65, 183*0.65, 247*0.65), [200, 125, 150, 50])
            font2 = pygame.font.SysFont("Times New Roman", 30)
            text2 = font2.render("Play Button", True, (235, 12, 45))

        #if you hover over the help button  it turns light blue, otherwise it is dark blue
        if 350 > mouse[0] > 200 and 275 > mouse[1] > 225:
            change_title = pygame.draw.rect(window,(141, 183, 247) , [200, 225, 150, 50])
            font3 = pygame.font.SysFont("Times New Roman", 30)
            text3 = font3.render("Help Button", True, (235, 12, 45))
        else:
            change_title = pygame.draw.rect(window, (141*0.65, 183*0.65, 247*0.65), [200, 225, 150, 50])
            font3 = pygame.font.SysFont("Times New Roman", 30)
            text3 = font3.render("Help Button", True, (235, 12, 45))

        #if you hover over the quit button it turns light blue, otherwise it is dark blue
        if 350 > mouse[0] > 200 and 375 > mouse[1] > 325:
            quit_button = pygame.draw.rect(window, (141, 183, 247), [200, 325, 150, 50])
            font4 = pygame.font.SysFont("Times New Roman", 30)
            text4 = font4.render("Quit Button", True, (235, 12, 45))
        else:
            quit_button = pygame.draw.rect(window, (141*0.65, 183*0.65, 247*0.65), [200, 325, 150, 50])
            font4 = pygame.font.SysFont("Times New Roman", 30)
            text4 = font4.render("Quit Button", True, (235, 12, 45))

        #if you hover over the play button it turns green, otherwise it is grey
        if 575 > mouse[0] > 425 and 300 > mouse[1] > 250:
            play_button = pygame.draw.rect(window, (141, 183, 247), [425, 250, 150, 50])
            font5 = pygame.font.SysFont("Times New Roman", 30)
            text5 = font5.render("Play Music", True, (235, 12, 45))
        else:
            play_button = pygame.draw.rect(window, (141*0.65, 183*0.65, 247*0.65), [425, 250, 150, 50])
            font5 = pygame.font.SysFont("Times New Roman", 30)
            text5 = font5.render("Play Music", True, (235, 12, 45))

        #if you hover over the pause button it turns green, otherwise it is grey
        if 575 > mouse[0] > 425 and 410 > mouse[1] > 350:
            pause_button = pygame.draw.rect(window, (141, 183, 247), [425, 350, 160, 50])
            font6 = pygame.font.SysFont("Times New Roman", 30)
            text6 = font6.render("Pause Music", True, (235, 12, 45))
        else:
            pause_button = pygame.draw.rect(window, (141*0.65, 183*0.65, 247*0.65), [425, 350, 160, 50])
            font6 = pygame.font.SysFont("Times New Roman", 30)
            text6 = font6.render("Pause Music", True, (235, 12, 45))

        #prints everything to the window
        window.blit(text2, (200, 135))
        window.blit(text3, (200, 235))
        window.blit(text4, (200, 335))
        window.blit(text5, (425, 250))
        window.blit(text6, (425, 350))
        pygame.display.flip()
        
main()
