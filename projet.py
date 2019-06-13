# Créé par Aurélie, le 12/06/2019 en Python 3.4
from graphics import *

#Définition de la taille de la fenêtre
LARGEUR=900
HAUTEUR=600
f=init_graphics(LARGEUR,HAUTEUR)

p1=(50,50)
draw_circle(p1,50,rouge,f)
#attente pour terminer
wait_escape(f)

quit_graphics()

class Voyageur:
    def __init__(self,x,y,dx,dy,numeroPorte):
        position=[x,y]
        rayon=5
        deplacement=[dx,dy]
        porteDeSortie=numeroPorte
        #couleur="mettre une couleur"


class Porte :
    def __init__(self,x1,y1,x2,y2,d):
        extremite1=[x1,y1]
        extremite2= [x2,y2]
        milieu=[(x1+x2)//2,(y1+y2)//2]
        debit=d
        debitEnCours=d

class ObstaclePoteau :
    def __init__(self,x,y):
        position=[x,y]
        rayon=10
        #couleur="mettre une couleur"

class Listes :
    def __init__(self):
        listeVoyageurs=[]

    def ajouterVoyageurs(self,voyageur): #voyageur est un objet de la classe Voyageur
        voyageur = Voyageur()
        self.listeVoyageurs.append(voyageur)




