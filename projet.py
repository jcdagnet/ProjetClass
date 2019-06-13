# Créé par Aurélie, le 12/06/2019 en Python 3.4
from graphics import *

#Définition de la taille de la fenêtre
LARGEUR=900
HAUTEUR=600
f=init_graphics(LARGEUR,HAUTEUR)

p1=[50,50]
draw_circle(p1,50,rouge,f)
#attente pour terminer
wait_escape(f)

quit_graphics()

class Voyageur:
    def __init__(self,p,v,numPorte):
        position=p
        rayon=5
        deplacement=v
        porteDeSortie=numPorte
        choix=alea_int(1,4)
        if (choix==1):
            couleur=rouge
        elif (choix==2):
            couleur=vert
        elif (choix==3):
            couleur=bleu
        else:
            couleur=orange
                
    def dessinVoyageur(self):
        draw_fill_circle(self.position,self.rayon,self.couleur,f)

class Porte :
    def __init__(self,p1,p2,d):
        extremite1=p1
        extremite2= p2
        milieu=[(p1[0]+p2[0])//2,(p1[1]+p2[1])//2]
        debit=d
        debitEnCours=d
        couleur=marron

    def dessinPorte(self):
        draw_line(self.extremite1,self.extremite2,self.couleur,f)

class Poteau :
    def __init__(self,p):
        position=p
        rayon=10
        couleur=jaune

    def dessinPoteau(self):
        draw_fill_circle(self.position,self.rayon,self.couleur)

class Salle :
    def __init__(self):
        listeVoyageurs=[]
        listePortes = []
        listePoteaux=[]

    def ajouterVoyageur(self,p,v,numPorte): #voyageur est un objet de la classe Voyageur
        voyageur = Voyageur(p,v,numPorte)
        self.listeVoyageurs.append(voyageur)
        
    def effaceVoyageur(self,voyageur):
        self.listeVoyageurs.remove(voyageur)
   
    def ajouterPorte(self,p1,p2,d):
        porte = Porte(p1,p2,d)
        self.listePortes.append(porte)

    def effacePorte(self,porte):
        self.listeVoyageurs.remove(porte)
   
   
    def ajouterPoteau(self,p):
        poteau = Poteau(p)
        self.listePortes.append(poteau)

    def effacePorte(self,poteau):
        self.listeVoyageurs.remove(poteau)
 

