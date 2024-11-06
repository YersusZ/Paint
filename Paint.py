import pygame
from pygame.locals import *

Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Amarillo = (255, 255, 0)
Azul = (0, 0, 255)
Naranja = (255, 165, 0)
Morado = (128, 0, 128)
Cian = (0, 255, 255)
Rojo = (255, 0, 0)
Rosa = (255, 192, 203)
Verde = (0, 255, 0)
Gris = (128, 128, 128)

pygame.init()
Screen = pygame.display.set_mode((800, 600))
Clock = pygame.time.Clock()
pygame.display.set_caption("")
font = pygame.font.SysFont(None, 18)

def PaletaFiguras():
    #Dibujar un rectangulo
    pygame.draw.rect(Screen, Blanco, (0, 0, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (0, 0, 50, 50),3)
    pygame.draw.rect(Screen, Negro, (10, 10, 30, 30),2)
    #Dibujar un circulo
    pygame.draw.rect(Screen, Blanco, (0, 50, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (0, 50, 50, 50),3)
    pygame.draw.circle(Screen, Negro, (25, 75), 15, 2)
    #Dibujar un triangulo
    pygame.draw.rect(Screen, Blanco, (0, 100, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (0, 100, 50, 50),3)
    pygame.draw.polygon(Screen, Negro, [(10,135), (40,135), (25,110)], 2)
    #Dibujar una linea recta
    pygame.draw.rect(Screen, Blanco, (0, 150, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (0, 150, 50, 50),3)
    pygame.draw.line(Screen, Negro, (10,180), (40,170), 2)
    #Dibujar un elipse
    pygame.draw.rect(Screen, Blanco, (0, 200, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (0, 200, 50, 50),3)
    pygame.draw.ellipse(Screen, Negro, (10, 215, 30, 20), 2)
    #Dibujar una linea
    pygame.draw.rect(Screen, Blanco, (0, 250, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (0, 250, 50, 50),3)
    pygame.draw.lines(Screen, Negro, False, [(10, 290), (11, 274), (18, 269), (23, 275), (25, 282), (33, 287), (41, 274), (41, 274)], 2)
    
    
def PaletaColores():
    #Rojo
    pygame.draw.rect(Screen, Rojo, (0, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (0, 550, 50, 50),1)
    #Naranja
    pygame.draw.rect(Screen, Naranja, (50, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (50, 550, 50, 50),1)
    #Amarrillo
    pygame.draw.rect(Screen, Amarillo, (100, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (100, 550, 50, 50),1)
    #Verde
    pygame.draw.rect(Screen, Verde, (150, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (150, 550, 50, 50),1)
    #Cian
    pygame.draw.rect(Screen, Cian, (200, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (200, 550, 50, 50),1)
    #Azul
    pygame.draw.rect(Screen, Azul, (250, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (250, 550, 50, 50),1)
    #Morado
    pygame.draw.rect(Screen, Morado, (300, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (300, 550, 50, 50),1)
    #Rosado
    pygame.draw.rect(Screen, Rosa, (350, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (350, 550, 50, 50),1)
    #Blanco
    pygame.draw.rect(Screen, Blanco, (400, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (400, 550, 50, 50),1)
    #Negro
    pygame.draw.rect(Screen, Negro, (450, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (450, 550, 50, 50),1)
    #Gris
    pygame.draw.rect(Screen, Gris, (500, 550, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (500, 550, 50, 50),1)
    
def PaletaGrosores():
    #Grosor 1
    pygame.draw.rect(Screen, Blanco, (0, 350, 100, 25),0)
    pygame.draw.rect(Screen, Negro, (0, 350, 100, 25),3)
    pygame.draw.line(Screen, Negro, (20,362), (80,362), 1)
    #Grosor 2
    pygame.draw.rect(Screen, Blanco, (0, 375, 100, 25),0)
    pygame.draw.rect(Screen, Negro, (0, 375, 100, 25),3)
    pygame.draw.line(Screen, Negro, (20,387), (80,387), 2)
    #Grosor 3
    pygame.draw.rect(Screen, Blanco, (0, 400, 100, 25),0)
    pygame.draw.rect(Screen, Negro, (0, 400, 100, 25),3)
    pygame.draw.line(Screen, Negro, (20,412), (80,412), 3)
    #Grosor 4
    pygame.draw.rect(Screen, Blanco, (0, 425, 100, 25),0)
    pygame.draw.rect(Screen, Negro, (0, 425, 100, 25),3)
    pygame.draw.line(Screen, Negro, (20,437), (80,437), 4)

def PaletaRelleno():
    #Relleno
    pygame.draw.rect(Screen, Blanco, (0, 450, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (0, 450, 50, 50),3)
    pygame.draw.rect(Screen, Negro, (10, 460, 30, 30),1)
    #Sin Relleno
    pygame.draw.rect(Screen, Blanco, (50, 450, 50, 50),0)
    pygame.draw.rect(Screen, Negro, (50, 450, 50, 50),3)
    pygame.draw.rect(Screen, Negro, (60, 460, 30, 30),0)
    
def MarcoFigura():
    pygame.draw.rect(Screen, Negro, (650, 505, 140, 90),2)
    
def LimpiarMarcoFigura():
    pygame.draw.rect(Screen, Blanco, (650, 505, 140, 90),0)

def Lienzo():
    pygame.draw.rect(Screen, Negro, (130, 0, 660, 500),2)

def Fondo():
    pygame.draw.rect(Screen, Blanco, (0, 0, 130, 600))
    pygame.draw.rect(Screen, Blanco, (0, 500, 800, 100))

    
def SeleccionarFigura(x, y):
    if(x >= 0 and x <= 50 and y > 0 and y < 50):
        return("Rectangulo")
    if(x >= 0 and x <= 50 and y > 50 and y < 100):
        return("Circulo")
    if(x >= 0 and x <= 50 and y > 100 and y < 150):
        return("Triangulo")
    if(x >= 0 and x <= 50 and y > 150 and y < 200):
        return("Linea recta")
    if(x >= 0 and x <= 50 and y > 200 and y < 250):
        return("Elipse")
    if(x >= 0 and x <= 50 and y > 250 and y < 300):
        return("Linea")
    
def SeleccionarColor(x, y):
    if(x > 0 and x < 50 and y >= 550 and y <= 600):
        return(Rojo)
    if(x > 50 and x < 100 and y >= 550 and y <= 600):
        return(Naranja)
    if(x > 100 and x < 150 and y >= 550 and y <= 600):
        return(Amarillo)
    if(x > 150 and x < 200 and y >= 550 and y <= 600):
        return(Verde)
    if(x > 200 and x < 250 and y >= 550 and y <= 600):
        return(Cian)
    if(x > 250 and x < 300 and y >= 550 and y <= 600):
        return(Azul)
    if(x > 300 and x < 350 and y >= 550 and y <= 600):
        return(Morado)
    if(x > 350 and x < 400 and y >= 550 and y <= 600):
        return(Rosa)
    if(x > 400 and x < 450 and y >= 550 and y <= 600):
        return(Blanco)
    if(x > 450 and x < 500 and y >= 550 and y <= 600):
        return(Negro)
    if(x > 500 and x < 550 and y >= 550 and y <= 600):
        return(Gris)

def SeleccionarGrosor(x, y):
    if(x >= 0 and x <= 100 and y > 350 and y < 375):
        return(1)
    if(x >= 0 and x <= 100 and y > 375 and y < 400):
        return(2)
    if(x >= 0 and x <= 100 and y > 400 and y < 425):
        return(3)
    if(x >= 0 and x <= 100 and y > 425 and y < 450):
        return(4)
    if(x > 0 and x < 50 and y >= 450 and y <= 500):
        return(1)
    if(x > 50 and x < 100 and y >= 450 and y <= 500):
        return(0)
    
def DibujarFiguraSeleccionada(Figura, Color, Grosor):
    if Figura == "Rectangulo":
        pygame.draw.rect(Screen, Color, (695, 526, 50, 50),Grosor)
    elif Figura == "Circulo":
        pygame.draw.circle(Screen, Color, (720, 550), 25, Grosor)
    elif Figura == "Triangulo":
        pygame.draw.polygon(Screen, Color, [(690,570), (720,530), (750,570)], Grosor)
    elif Figura == "Linea recta":
        pygame.draw.line(Screen, Color, (690,570), (750,530), Grosor)
    elif Figura == "Elipse":
        pygame.draw.ellipse(Screen, Color, (690, 530, 60, 40), Grosor)
    elif Figura == "Linea":
        pygame.draw.lines(Screen, Color, False, [(697, 569), (699, 554), (705, 551), (721, 553), (730, 557), (739, 547), (745, 533)], Grosor)

def botonlimpiarlienzo():
    pygame.draw.rect(Screen, Negro, (0, 510, 100, 30),3)
    text = font.render("Limpiar", True, Negro)
    text_rect = text.get_rect()
    text_rect.center = (50, 525)
    Screen.blit(text, text_rect)

def LimpiarLienzo():
    pygame.draw.rect(Screen, Blanco, (130, 0, 660, 500), 0)

def main():
    ContClick = 0
    Screen.fill(Blanco)
    Figura = "Linea"
    Color = Negro
    Grosor = 1
    Dibujar = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botón izquierdo del mouse
                    Dibujar = True
                    UltimaPos = event.pos
                    x, y = pygame.mouse.get_pos()
                    if(x <= 50 and y < 300):
                        Figura = SeleccionarFigura(x, y)
                        ContClick = 0
                        LimpiarMarcoFigura()
                    if(x <= 550 and y >= 550):
                        Color = SeleccionarColor(x, y)
                        ContClick = 0
                        LimpiarMarcoFigura()
                    if(x <= 100 and y >= 350 and y <= 500):
                        Grosor = SeleccionarGrosor(x, y)
                        ContClick = 0
                        LimpiarMarcoFigura()
                    if(x <= 100 and y >= 510 and y <= 540):
                        ContClick
                        pygame.draw.rect(Screen, Blanco, (131, 1, 789 - 131, 499 - 1))
                    print("Click en: ", x, y)
                    if(x > 130 and y < 500):
                        if Figura == "Rectangulo":
                            ContClick = ContClick + 1
                            if ContClick == 1:
                                x1 = x
                                y1 = y
                            if ContClick == 2:
                                x2 = x
                                y2 = y
                                ContClick = 0
                                if (x1 <= x2 and y1 <= y2):
                                    pygame.draw.rect(Screen, Color, (x1, y1, x2 - x1, y2 - y1), Grosor)
                                elif (x1 <= x2 and y1 >= y2):
                                    pygame.draw.rect(Screen, Color, (x1, y2, x2 - x1, y1 - y2), Grosor)
                                elif (x1 >= x2 and y1 <= y2):
                                    pygame.draw.rect(Screen, Color, (x2, y1, x1 - x2, y2 - y1), Grosor)
                                elif (x1 >= x2 and y1 >= y2):
                                    pygame.draw.rect(Screen, Color, (x2, y2, x1 - x2, y1 - y2), Grosor)
                                    
                        if Figura == "Circulo":
                            ContClick = ContClick + 1
                            if ContClick == 1:
                                x1 = x
                                y1 = y
                            if ContClick == 2:
                                x2 = x
                                y2 = y
                                ContClick = 0
                                if (x1 <= x2 and y1 <= y2):
                                    pygame.draw.circle(Screen, Color, (x1, y1), (x2 - x1), Grosor)
                                elif (x1 <= x2 and y1 >= y2):
                                    pygame.draw.circle(Screen, Color, (x1, y2), (x2 - x1), Grosor)
                                elif (x1 >= x2 and y1 >= y2):
                                    pygame.draw.circle(Screen, Color, (x2, y2), (x1 - x2), Grosor)
                                elif (x1 >= x2 and y1 <= y2):
                                    pygame.draw.circle(Screen, Color, (x2, y1), (x1 - x2), Grosor)
                        if Figura == "Triangulo":
                            ContClick = ContClick + 1
                            if ContClick == 1:
                                x1 = x
                                y1 = y
                            if ContClick == 2:
                                x2 = x
                                y2 = y
                            if ContClick == 3:
                                x3 = x
                                y3 = y
                                ContClick = 0
                                pygame.draw.polygon(Screen, Color, [(x1,y1), (x2,y2), (x3,y3)], Grosor)
                        if Figura == "Linea recta":
                            ContClick = ContClick + 1
                            if ContClick == 1:
                                x1 = x
                                y1 = y
                            if ContClick == 2:
                                x2 = x
                                y2 = y
                                ContClick = 0
                                pygame.draw.line(Screen, Color, (x1, y1), (x2, y2), Grosor)
                        if Figura == "Elipse":
                            ContClick = ContClick + 1
                            if ContClick == 1:
                                x1 = x
                                y1 = y
                            if ContClick == 2:
                                x2 = x
                                y2 = y
                                ContClick = 0
                                if (x1 <= x2 and y1 <= y2):
                                    pygame.draw.ellipse(Screen, Color, (x1, y1, x2 - x1, y2 - y1), Grosor)
                                elif (x1 <= x2 and y1 >= y2):
                                    pygame.draw.ellipse(Screen, Color, (x1, y2, x2 - x1, y1 - y2), Grosor)
                                elif (x1 >= x2 and y1 <= y2):
                                    pygame.draw.ellipse(Screen, Color, (x2, y1, x1 - x2, y2 - y1), Grosor)
                                elif (x1 >= x2 and y1 >= y2):
                                    pygame.draw.ellipse(Screen, Color, (x2, y2, x1 - x2, y1 - y2), Grosor)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    Dibujar = False
        if Figura == "Linea":
            if Dibujar:
                PosicionActual = pygame.mouse.get_pos()
                if UltimaPos is not None:
                    pygame.draw.line(Screen, Color, UltimaPos, PosicionActual, Grosor)
                UltimaPos = PosicionActual
                
                            
                        

        pygame.display.flip()
        Fondo()
        PaletaFiguras()
        PaletaColores()
        PaletaGrosores()
        PaletaRelleno()
        Lienzo()
        MarcoFigura()
        botonlimpiarlienzo()
        DibujarFiguraSeleccionada(Figura, Color, Grosor)
        Clock.tick(60)

#Execute game:
main()
                    