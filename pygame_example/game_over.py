
import pygame
import sys
pygame.init()
clock = pygame.time.Clock()

def main():
    #this creates a window 600 pixels wide by 400 pixels high
    window2 = pygame.display.set_mode((600, 400))
    
    #sets the caption in the left cover of the window 
    pygame.display.set_caption("Menu")

    import test1
    import test2

    #loads the background image
    bg = pygame.image.load("pygame_example/background2.jpg")
    window2.blit(bg, (0, 0))

    font1 = pygame.font.SysFont("Arial", 60, bold=True)
    text1 = font1.render("G A M E  O V E R", True, (36, 38, 37))
    text1_1 = font1.render("G A M E  O V E R", True, (200, 0, 0))
    text1_2 = font1.render("G A M E  O V E R", True, (255, 0, 0))
    window2.blit(text1,(95, 20))
    window2.blit(text1_1,(100, 22))
    window2.blit(text1_2, (105, 24))

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
                        test1.main()
                        sys.exit()
                    #if you click quit button, it exits the program
                    if 350 > mouse[0] > 200 and 375 > mouse[1] > 325:
                        pygame.quit()
                        sys.exit()
                        
            #if you hover over the play button it turns green, otherwise it is grey
            if 350 > mouse[0] > 200 and 175 > mouse[1] > 125:
                play_button = pygame.draw.rect(window2, (141, 183, 247), [200, 125, 150, 50])
                font2 = pygame.font.SysFont("Times New Roman", 30)
                text2 = font2.render("Play Again", True, (235, 12, 45))
            else:
                play_button = pygame.draw.rect(window2, (141*0.65, 183*0.65, 247*0.65), [200, 125, 150, 50])
                font2 = pygame.font.SysFont("Times New Roman", 30)
                text2 = font2.render("Play Again", True, (235, 12, 45))

            #if you hover over the help button it turns green, otherwise it is grey
            if 350 > mouse[0] > 200 and 275 > mouse[1] > 225:
                change_title = pygame.draw.rect(window2,(141, 183, 247) , [200, 225, 150, 50])
                font3 = pygame.font.SysFont("Times New Roman", 30)
                text3 = font3.render("Main Menu", True, (235, 12, 45))
            else:
                change_title = pygame.draw.rect(window2, (141*0.65, 183*0.65, 247*0.65), [200, 225, 150, 50])
                font3 = pygame.font.SysFont("Times New Roman", 30)
                text3 = font3.render("Main Menu", True, (235, 12, 45))

            #if you hover over the quit button it turns green, otherwise it is grey
            if 350 > mouse[0] > 200 and 375 > mouse[1] > 325:
                quit_button = pygame.draw.rect(window2, (141, 183, 247), [200, 325, 150, 50])
                font4 = pygame.font.SysFont("Times New Roman", 30)
                text4 = font4.render("Quit", True, (235, 12, 45))
            else:
                quit_button = pygame.draw.rect(window2, (141*0.65, 183*0.65, 247*0.65), [200, 325, 150, 50])
                font4 = pygame.font.SysFont("Times New Roman", 30)
                text4 = font4.render("Quit", True, (235, 12, 45))
            
            window2.blit(text2, (250, 135))
            window2.blit(text3, (250, 235))
            window2.blit(text4, (250, 335))
            pygame.display.flip()