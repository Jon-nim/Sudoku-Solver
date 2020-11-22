import sys
import pygame as pygame
import sudokuSolver

screenWidth = 630 
screenHeight = 630
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('calibri', int(screenWidth/10))

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

def drawRect(screen,xpos, ypos):
    if (xpos == None or ypos == None):
        return
    else:
        x = (xpos * (screenWidth/9)+1)
        y = (ypos * (screenHeight/9)+1)

        pygame.draw.rect(screen, (233,233,233), (x,y,((screenWidth/9) - 1),((screenHeight/9)-1)))

newGrid = [ [1,2,3,  4,5,6,  7,8,9],
		    [0,0,0,  0,0,0,  0,0,0],
			[0,0,0,  0,0,0,  0,0,0],

			[0,0,0,  0,0,0,  0,0,0],
		    [0,0,0,  0,0,0,  0,0,0],
		    [0,0,0,  0,0,0,  0,0,0],

     	    [0,0,0,  0,0,0,  0,0,0], 
		    [0,0,0,  0,0,0,  0,0,0],
		    [0,0,0,  0,0,0,  0,0,0]]

def drawNums(screen):
    for i in range(9):
        for j in range(9):
            if newGrid[i][j] == 0:
                continue
            x = font.render(str(newGrid[i][j]),False,(0,0,0))
            screen.blit(x, ((j * screenWidth/9 + 20), (i * screenHeight/9 + 10)))


def main():
    screen = pygame.display.set_mode((screenHeight,screenWidth))
    inputbox = pygame.Rect(0,0,screenWidth/9,screenHeight/9)
    start = True
    xpos = None
    ypos = None
    

    while(start == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                xpos = int(x/(screenWidth/9))
                ypos = int(y/(screenHeight/9))
            elif event.type == pygame.KEYDOWN():
                
        drawSudokuScreen(screen)
        drawRect(screen,xpos, ypos)
        drawNums(screen)
        pygame.display.flip()




main()






