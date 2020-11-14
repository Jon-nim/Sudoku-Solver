import sys
import pygame as pygame
import sudokuSolver

screenWidth = 601
screenHeight = 601
pygame.init()

def drawSudokuScreen(screen):
    
    screen.fill((255,255,255))
    for i in range(10):
        pygame.draw.line(screen,(128,128,128),(0,i * round((screenWidth/9))), (screenHeight,i * round((screenWidth/9))), 1)
    for i in range(10):
        pygame.draw.line(screen,(128,128,128),((i * round((screenWidth/9)),0)), (i * round((screenWidth/9)),screenHeight), 1)
    for i in range(4):
        pygame.draw.line(screen,(0,0,0),(0,i * round((screenWidth/3))), (screenHeight,i * round((screenWidth/3))), 2)
    for i in range(4):
        pygame.draw.line(screen,(0,0,0),((i * round((screenWidth/3)),0)), (i * round((screenWidth/3)),screenHeight), 2)    
    pygame.display.flip()
 

def main():
    screen = pygame.display.set_mode((screenHeight,screenWidth))
    inputbox = pygame.Rect(0,0,screenWidth/9,screenHeight/9)
    ibActive = False
    color = (200,200,200)
    ibcolorActive = (100,100,100)
    ibcolorInactive = (200,200,200)
    start = True

    while(start == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if inputbox.collidepoint(event.pos):
                    ibActive = True
                    color = ibcolorActive
                else:
                    ibActive = False
                    color = ibcolorInactive
                    
        drawSudokuScreen(screen)
        pygame.draw.rect(screen, color, inputbox, 2)
        pygame.display.flip()


main()




