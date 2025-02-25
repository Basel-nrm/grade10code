import pygame
import sys
pygame.init()
clock = pygame.time.Clock()
import random

def game():
    #creates counters to keep track of certain factors of the game
    burger_counter = 0
    score_counter = 0
    life_counter = 3
    character_speed = 7
    #this creates a window 600 pixels wide by 400 pixels high
    window1 = pygame.display.set_mode((600, 400))

    #sets the caption in the left corner of the window
    pygame.display.set_caption("Burger Rush")
    
    import game_over
    import burger_rush
    #loads the fat guy image & starting position of image
    fatguy = pygame.image.load("pygame_example/fatguy.png")
    
    #initial position of the fat guy
    x = 0
    y = 480-fatguy.get_height()
    #initial position of the burger
    y1 = 0
    x1 = random.randint(30, 570)
    #initial position of the broccoli
    y2 = 0
    x2 = random.randint(30, 570)

    #loads the burger and broccoli image 
    broccoli = pygame.image.load("pygame_example/broccoli_scaled_nobkg.png")
    burger = pygame.image.load("pygame_example/burger.png")
    
    #the fat guy starts not moving
    to_right = False
    to_left = False

    while True:
        #loads the background image
        bg = pygame.image.load("pygame_example/background1.png")
        window1.blit(bg, (0, 0))
        #score
        font1 = pygame.font.SysFont("Times New Roman", 30)
        text1 = font1.render("Score: "+ str(score_counter), True, (36, 38, 37), (255, 155, 255))
        window1.blit(text1,(10, 5))
        #lives
        font1 = pygame.font.SysFont("Times New Roman", 30)
        text1 = font1.render("Lives: "+ str(life_counter), True, (36, 38, 37), (255, 155, 255))
        window1.blit(text1,(485, 5))

        #gets the rectangle around the fat, burger, and broccoli
        fatguy_surface = pygame.Rect(x+10, y, fatguy.get_width()-30, fatguy.get_height())
        burger_surface = pygame.Rect(x1, y1, burger.get_width(), burger.get_height())
        broccoli_surface = pygame.Rect(x2, y2, broccoli.get_width(), broccoli.get_height())
        #returns true if the 2 rectangles overlap with each other and decreases the speed of the character if 5 burgers are collected
        if fatguy_surface.colliderect(burger_surface):
            y1 = 0
            x1 = random.randint(30, 570)
            score_counter += 1
            if burger_counter < 5:
                burger_counter += 1
            else:
                burger_counter = 0
                character_speed -= 1 
        #returns true if the 2 rectangles overlap with each other and increases the speed of the character if 1 broccoli is collected
        if fatguy_surface.colliderect(broccoli_surface):
            y2 = 0
            x2 = random.randint(30, 570)
            if life_counter < 3: life_counter += 1
            character_speed += 1 if character_speed < 9 else 0 

        #if the burger reaches the ground, the player loses a life and the burger drops from the top again
        if y1 == 400:
            y1 = 0
            x1 = random.randint(30, 570)
            life_counter -= 1
            if life_counter <= 0: 
                pygame.time.wait(1000)
                game_over.main(score_counter)
        y1 += 5
        #if the broccoli reaches the ground, it drops from the top again
        if y2 == 400:
            y2 = 0
            x2 = random.randint(30, 570)
        y2 += 8

        for event in pygame.event.get():
            #controls for when pressing the key down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True

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
                
            #when you press the button down in the rectangular areas
            if event.type == pygame.MOUSEBUTTONDOWN:
               #gets the current position of the mouse on the screen
               mouse1 = pygame.mouse.get_pos()
               if 590 > mouse[0] > 440 and 400 > mouse[1] > 350:
                   burger_rush.main()
                   
        # this gets the current position of the mouse
        mouse = pygame.mouse.get_pos()

        # if you hover over the main menu button it turns green, otherwise it is grey
        if 590 > mouse[0] > 440 and 400 > mouse[1] > 350:
            play_button = pygame.draw.rect(window1, "green", [440, 350, 150, 50])
            font2 = pygame.font.SysFont("Times New Roman", 30)
            text2 = font2.render("Main Menu", True, (235, 12, 45))
        else:
            play_button = pygame.draw.rect(window1, "dark grey", [440, 350, 150, 50])
            font2 = pygame.font.SysFont("Times New Roman", 30)
            text2 = font2.render("Main Menu", True, (235, 12, 45))
        
        # keeps the fat guy from going off the left or right of the screen
        if x+fatguy.get_width() <= fatguy.get_width():
            x = 0 
        if x+fatguy.get_width() >= 600:
            x = 600 - fatguy.get_width()
        
        # keeps the fat guy from going off the top or bottom of the screen
        if y+fatguy.get_height() <= fatguy.get_height():
            y = 0 
        if y+fatguy.get_height() >= 400:
            y = 400 - fatguy.get_height()
        
        # if left or right arrow is pressed, moves fat guy 2 pixels left or right
        if to_right:
            x += character_speed
        if to_left:
            x -= character_speed
       
        # prints everything to the window
        window1.blit(text2, (440, 355))
        window1.blit(fatguy, (x, y))
        window1.blit(burger, (x1, y1))
        # makes the broccoli stop appearing if the player has 3 lives
        if life_counter < 3: 
            window1.blit(broccoli, (x2, y2))
        else:
            y2 = 0  # makes the broccoli not appear when it shouldn't
        pygame.display.flip()
        clock.tick(60)
game()