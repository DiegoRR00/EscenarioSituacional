import pygame
import os.path
import csv
size=(600,700)
fondo=(255,255,255)
letras=(0,0,0)
espacio=[100,100]
tamano=[150,150]
class Imagen:
    def __init__(self, archivo, coordenadas):
        self.archivo=pygame.image.load(archivo) 
        self.archivo=pygame.transform.scale(self.archivo,tamano)
        self.x=coordenadas[0]
        self.y=coordenadas[1]
    def print(self, win):
        win.blit(self.archivo,(self.x,self.y))


pygame.init()
imagenes=[]
with open("config.csv") as archivo:
    lector=csv.reader(archivo,delimiter=',')
    counter=0
    columna=0
    fila=0
    for renglon in lector:
        if counter!=0:
            counter+=1
            if (columna==2):
                fila+=1
                columna=0
            for dato in renglon:
                imagenes.append(Imagen(dato,[espacio[0]*(columna+1)+tamano[0]*columna,espacio[1]*(fila+1)+tamano[1]*fila]))
                break
            columna+=1
        else:
            counter+=1
win=pygame.display.set_mode(size)
pygame.display.set_caption("funko.com")
win.fill(fondo)
font=pygame.font.Font('freesansbold.ttf',15)
text=font.render('Simulación de interfaz',True,letras,fondo)
textRect=text.get_rect()
textRect.center=(100,50)
running=True
while running:
    pygame.time.delay(1000)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False
    win.fill(fondo)
    for imgObj in imagenes:
        imgObj.print(win)
    win.blit(text,textRect)
pygame.quit()