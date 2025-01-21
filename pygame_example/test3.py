import pygame
import sys
pygame.init()
clock = pygame.time.Clock()


def help():
    import test1
    #this creates a window 600 pixels wide by 400 pixels high
    window2 = pygame.display.set_mode((600, 400))
    
    #sets the caption in the left cover of the window 
    pygame.display.set_caption("Help")

    #loads the background image
    bg = pygame.image.load("pygame_example/help_bkg.jpg")
    window2.blit(bg, (0, 0))

    font1 = pygame.font.SysFont("Arial", 60, bold=True)
    text1 = font1.render("How To Play", True, (36, 38, 37))
    window2.blit(text1,(130, 5))

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
               #if you click back button, it goes to the game
               if 175 > mouse[0] > 25 and 375 > mouse[1] > 325:
                   test1.main()
               #if you click quit button, it exits the program
               if 575 > mouse[0] > 425 and 375 > mouse[1] > 325:
                   pygame.quit()
                   sys.exit()
            pygame.display.update()
        #if you hover over the back button it turns light blue, otherwise it is grey
        if 175 > mouse[0] > 25 and 375 > mouse[1] > 325:
            change_title = pygame.draw.rect(window2, (141, 183, 247), [25, 325, 150, 50])
            font3 = pygame.font.SysFont("Times New Roman", 30)
            text3 = font3.render("Back", True, (235, 12, 45))
        else:
            change_title = pygame.draw.rect(window2, (141*0.65, 183*0.65, 247*0.65), [25, 325, 150, 50])
            font3 = pygame.font.SysFont("Times New Roman", 30)
            text3 = font3.render("Back", True, (235, 12, 45))

        #if you hover over the quit button it turns green, otherwise it is grey
        if 575 > mouse[0] > 425 and 375 > mouse[1] > 325:
            quit_button = pygame.draw.rect(window2, (141, 183, 247), [425, 325, 150, 50])
            font4 = pygame.font.SysFont("Times New Roman", 30)
            text4 = font4.render("Quit", True, (235, 12, 45))
        else:
            quit_button = pygame.draw.rect(window2, (141*0.65, 183*0.65, 247*0.65), [425, 325, 150, 50])
            font4 = pygame.font.SysFont("Times New Roman", 30)
            text4 = font4.render("Quit", True, (235, 12, 45))
        

        window2.blit(text3, (65, 330))
        window2.blit(text4, (475, 330))
        pygame.display.flip()