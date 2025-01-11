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

