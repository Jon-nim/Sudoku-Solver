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

def drawRect(screen,xpos, ypos, rectColor):
    if (xpos == None or ypos == None):
        return
    elif xpos * screenWidth/9 +1 > screenWidth:
        return
    else:
        x = (xpos * (screenWidth/9)+1)
        y = (ypos * (screenHeight/9)+1)

        pygame.draw.rect(screen, (rectColor), (x,y,((screenWidth/9) - 1),((screenHeight/9)-1)))

def drawNums(screen, newGrid):
    for i in range(9):
        for j in range(9):
            if newGrid[i][j] == 0:
                continue
            x = font.render(str(newGrid[i][j]),True,(0,0,0))
            screen.blit(x, ((j * screenWidth/9 + 20), (i * screenHeight/9 + 10)))

def drawTemp(screen, text,xpos, ypos):
    if (xpos == None or ypos == None):
        return
    elif xpos * screenWidth/9 +1 > screenWidth:
        return
    temp = font.render(text, True, (100,100,100))
    screen.blit(temp, ((xpos * screenWidth/9 + 20), (ypos * screenHeight/9 + 10)) )

def solve(sudoku, newGrid):
    for i in range(9):
        for spot in range(9):
               newGrid[i][spot] = sudoku.puzzleSolution[i][spot]





def main():
    screen = pygame.display.set_mode((screenHeight + 250,screenWidth))
    inputbox = pygame.Rect(0,0,screenWidth/9,screenHeight/9)
    newGrid = []
    chooseDifficulty = 0
    titleScreen = True
    startPuzzle = False
    xpos = None
    ypos = None
    text = ""
    rectColor1 = (233,233,233)
    active = False
    sudoku = sudokuSolver.Sudoku()
    easyButton = (screenWidth/4, screenHeight/2)
    normalButton = (screenWidth/2, screenHeight/2)
    hardButton = (screenWidth * .88, screenHeight/2)


    
    while(titleScreen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if ((x >= easyButton[0] and x < normalButton[0] - 50) and (y >= easyButton[1] and  y < screenHeight/2 + 50)):
                    chooseDifficulty = 1
                    titleScreen = False
                    startPuzzle = True
                elif (x >= normalButton[0] and x < hardButton[0] -50) and (y >= normalButton[1] and y < screenHeight/2 + 50):
                    chooseDifficulty = 2
                    titleScreen = False
                    startPuzzle = True
                elif (x >= hardButton[0] and x < hardButton[0] + 100) and (y >= hardButton[1] and y < screenHeight/2 + 50):
                    chooseDifficulty = 3
                    titleScreen = False
                    startPuzzle = True
        screen.fill((255,255,255))
        title = font.render("Sudoku", True, (0,0,0))
        screen.blit(title, (screenWidth/2,screenHeight/6))
        easy = font.render("Easy", True, (0,0,0))
        normal = font.render('Normal', True, (0,0,0))
        hard = font.render("Hard", True, (0,0,0))
        screen.blit(easy, (easyButton))
        screen.blit(normal, (normalButton))
        screen.blit(hard, (hardButton))

        #pygame.draw.rect(screen, (255,), (x,y,((screenWidth/9) - 1),((screenHeight/9)-1)))
        pygame.display.flip()
    
    if chooseDifficulty == 1:
        newGrid = sudoku.puzzleEasy
    elif chooseDifficulty == 2:
        newGrid = sudoku.puzzleNormal
    elif chooseDifficulty == 3:
        newGrid = sudoku.puzzleHard
    
    
    solution = sudoku.puzzleSolution
    
   
        

    while(startPuzzle == True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                active = True
                x,y = pygame.mouse.get_pos()
                rectColor1 = (233,233,233)
                xpos = int(x/(screenWidth/9))
                ypos = int(y/(screenHeight/9))
                text = ""
                if  xpos * screenWidth/9 +1 < screenWidth:
                    if newGrid[ypos][xpos] > 0:
                        active = False
                        xpos = None
                        ypos = None

            elif event.type == pygame.KEYDOWN:
                rectColor1 = (233,233,233)
                if (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER) and active :
                    if text == "":
                        pass
                    elif int(text) == solution[ypos][xpos]:
                        newGrid[ypos][xpos] = solution[ypos][xpos]
                        text = ""
                        active = False
                        rectColor1 = (255,255,255)
                    else:
                        rectColor1 = (255,0,0)
                        text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = ""
                elif event.key == pygame.K_SPACE:
                    solve(sudoku, newGrid)


                else:
                    if len(text) == 0:
                        if event.unicode.isdigit() and active:
                            text += event.unicode
        drawSudokuScreen(screen)
        drawRect(screen,xpos, ypos, rectColor1)
        drawNums(screen, newGrid)
        drawTemp(screen, text, xpos,ypos)
        pygame.display.flip()




main()




