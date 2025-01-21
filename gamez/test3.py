import pygame
import sys
pygame.init()
clock = pygame.time.Clock()

def help():
    import burger_rush
    #this creates a window 600 pixels wide by 400 pixels high
    window2 = pygame.display.set_mode((600, 400))
    
    #sets the caption in the left cover of the window 
    pygame.display.set_caption("Menu")

    #loads the background image
    bg = pygame.image.load("background2.jpg")
    window2.blit(bg, (0, 0))

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
               if 350 > mouse[0] > 200 and 275 > mouse[1] > 225:
                   burger_rush.main()
               #if you click quit button, it exits the program
               if 350 > mouse[0] > 200 and 375 > mouse[1] > 325:
                   pygame.quit()
                   sys.exit()
        #if you hover over the back button it turns green, otherwise it is grey
        if 350 > mouse[0] > 200 and 275 > mouse[1] > 225:
            change_title = pygame.draw.rect(window2, "green", [200, 225, 150, 50])
            font3 = pygame.font.SysFont("Times New Roman", 30)
            text3 = font3.render("Back Button", True, (235, 12, 45))
        else:
            change_title = pygame.draw.rect(window2, "dark grey", [200, 225, 150, 50])
            font3 = pygame.font.SysFont("Times New Roman", 30)
            text3 = font3.render("Back Button", True, (235, 12, 45))

        #if you hover over the quit button it turns green, otherwise it is grey
        if 350 > mouse[0] > 200 and 375 > mouse[1] > 325:
            quit_button = pygame.draw.rect(window2, "green", [200, 325, 150, 50])
            font4 = pygame.font.SysFont("Times New Roman", 30)
            text4 = font4.render("Quit Button", True, (235, 12, 45))
        else:
            quit_button = pygame.draw.rect(window2, "dark grey", [200, 325, 150, 50])
            font4 = pygame.font.SysFont("Times New Roman", 30)
            text4 = font4.render("Quit Button", True, (235, 12, 45))
        
       
        window2.blit(text3, (200, 235))
        window2.blit(text4, (200, 335))
        pygame.display.flip()
