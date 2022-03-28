from turtle import *
import math
width(4)
speed(20)
#La fonction rectangle 
def rectangle(largeur,hauteur):    
    for i in range(2):
        fd(largeur)
        left(90)
        fd(hauteur)
        left(90)
#La fonction Triangle
def triangle(x):    
    for i in range(3):
        fd(x)
        left(120)
#La fonction carre
def carre(cote):
    for i in range(4):
        fd(cote)
        left(90)
#La fonction cercle    
def cercle(rayon):
    circle(rayon)
#La fonction demiCercle    
def demiCercle(rayon):
    circle(rayon,180)
#La fonction polygone
def polygone(cote):
    for i in range(cote):
        fd(100)
        left(360/cote)
#La fonction Trapeze    
def trapeze(x,y,z):
    for i in range(1):
        left(100)
        forward(z)
        left(80)
        forward(z)
        left(70)
        forward(z)
        goto(x,y)
#La fonction Losange
def losange(taille,angle):
    c=0
    while c<4:
        if c%2==0:
            right(angle)
            forward(taille)
        if c%2==1:
            right(180-angle)
            forward(taille)
        c=c+1