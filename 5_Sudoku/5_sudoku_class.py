import pygame
import sys
import sudoku_resolt

class SudokuResolver():
#Definición de la clase ventana de interfaz gráfica
    def __init__(self, width=550, height=600):
        #Definición de las variables del tamaño de la ventana principal
        self.width=width
        self.height=height

        #Inicialización de la ventana
        self.screen=pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku")
        self.screen.fill('white')

        #Definición de variables de texto
        self.black=(0,0,0)
        self.orange=(255,165,0)
        self.font=pygame.font.SysFont('Helvetica',35)
        self.font_button=pygame.font.SysFont('Helvetica',25)

        #Definición del boton solución
        self.button_text=self.font_button.render('Solution',True,self.black)
        self.button_rect=self.button_text.get_rect(center=(275,550))

    def print_board(self):
        #Dibujamos el tablero
        for i in range(10):
            if i%3==0:
                pygame.draw.line(self.screen,self.black,(50,50+(50*i)),(500,50+(50*i)),4)
                pygame.draw.line(self.screen,self.black,(50*i+50,50),(50*i+50,500),4)
            else:
                pygame.draw.line(self.screen,self.black,(50,50+(50*i)),(500,50+(50*i)),2)
                pygame.draw.line(self.screen,self.black,(50*i+50,50),(50*i+50,500),2)
    
    def print_sudoku(self,sudoku):
        #Escribimos los números del sudoku
        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                value=sudoku[i][j]
                if value != 0:
                    text=self.font.render(str(value),True,self.black)
                    text_rect=text.get_rect(center=(50*j +75, 50*i+75))
                    self.screen.blit(text,text_rect)
    
    def solution_button(self):
        #Dibuja el boton de solucionar
        pygame.draw.rect(self.screen,self.orange,self.button_rect)
        self.screen.blit(self.button_text,self.button_rect)

        #Change the cursor when is on the solution button
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def solve_print_solution(self,sudoku):
        #Funcion que llama a otra función para resolver el sudoku y dibuja el panel resuelto
        solution=sudoku_resolt.solve_sudoku(sudoku)
        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                value_2=solution[i][j]
                if value_2 != 0:
                    text_sol=self.font.render(str(value_2),True,self.black)
                    text_rect_sol=text_sol.get_rect(center=(50*j +75, 50*i+75))
                    self.screen.blit(text_sol,text_rect_sol)

    def run(self,sudoku):
        #Bucle principal necesario para Pygame
        while True:
            for event in pygame.event.get():
                #Acción para cerrar programa
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #Acción para solucionar el sudoku
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        self.solve_print_solution(sudoku)

            self.print_board()
            self.print_sudoku(sudoku)
            self.solution_button()

            pygame.display.update()


#Sudoku
sudoku_resolver=[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

pygame.init()
solve_sudoku=SudokuResolver()
solve_sudoku.run(sudoku_resolver)