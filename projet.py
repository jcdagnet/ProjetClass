﻿# Créé par Aurélie, le 12/06/2019 en Python 3.4
from graphics import *

#Définition de la taille de la fenêtre
LARGEUR=900
HAUTEUR=600
f=init_graphics(LARGEUR,HAUTEUR)



class Voyageur:
    def __init__(self,p,numPorte):
        self.position=p
        self.rayon=5
        self.deplacement=[0,0]
        self.vitesse=5
        self.porteDeSortie=numPorte
        choix=alea_int(1,4)
        if (choix==1):
            self.couleur=rouge
        elif (choix==2):
            self.couleur=vert
        elif (choix==3):
            self.couleur=bleu
        else:
            self.couleur=orange

    def __str__(self):
        mes=""
        mes=mes+"position "+str(self.position[0])+str(self.position[1])
        mes=mes+" rayon "+str(self.rayon)
        mes=mes+" deplacement "+str(self.deplacement[0])+str(self.deplacement[1])
        mes=mes+" vitesse "+str(self.vitesse)
        mes=mes+" Porte de Sortie "+str(self.porteDeSortie)
        mes=mes+" couleur "+str(self.couleur[0])+str(self.couleur[1])+str(self.couleur[2])
        return mes

    def dessinVoyageur(self):
        draw_fill_circle(self.position,self.rayon,self.couleur,f)

    def effaceVoyageur(self):
        draw_fill_circle(self.position,self.rayon,noir,f)

    def deplacementVoyageur(self):
        self.position[0]+=self.deplacement[0]
        self.position[1]+=self.deplacement[1]

class Porte :
    def __init__(self,p1,p2,d):
        self.extremite1=p1
        self.extremite2= p2
        self.milieu=[milieu(p1,p2)[0],milieu(p1,p2)[1]]
        self.debit=d
        self.debitEnCours=d
        self.couleur=cyan

    def dessinPorte(self):
        draw_fill_rectangle(self.extremite1,self.extremite2,self.couleur,f)

    def __str__(self):
        mes=""
        mes=mes+"extremite1 "+str(self.extremite1)
        mes=mes+" extremite2 "+str(self.extremite2)
        mes=mes+" milieu "+str(self.milieu)
        mes=mes+" debit "+str(self.debit)
        mes=mes+" debit en cours "+str(self.debitEnCours)
        return mes

class Poteau :
    def __init__(self,p):
        self.position=p
        self.rayon=30
        self.couleur=jaune

    def dessinPoteau(self):
        draw_fill_circle(self.position,self.rayon,self.couleur,f)

    def __str__(self):
        mes=""
        mes=mes+"position "+str(self.position[0])+str(self.position[1])
        mes=mes+" rayon "+str(self.rayon)
        return mes


class Salle :
    def __init__(self):
        self.listeVoyageurs=[]
        self.listePortes = []
        self.listePoteaux=[]

    def ajouterVoyageur(self,p,numPorte): #voyageur est un objet de la classe Voyageur
        voyageur = Voyageur(p,numPorte)
        voyageur.dessinVoyageur()
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
        self.listePoteaux.append(poteau)

    def effacePoteau(self,poteau):
        self.listeVoyageurs.remove(poteau)

    def vecteurDeplacement(self,voyageur):
        dest=milieu(self.listePortes[voyageur.porteDeSortie].extremite1,self.listePortes[voyageur.porteDeSortie].extremite2)
        #print("destination",dest[0]," ",dest[1])
        pos=voyageur.position
        v=voyageur.vitesse
        n=distance(pos,dest)
        #print("n=",n)
        dx=round(((dest[0]-pos[0])*v)/n)
        dy=round(((dest[1]-pos[1])*v)/n)
        return [dx,dy]

    def trouveDeplacement(self,numVoy):
        voyageur=self.listeVoyageurs[numVoy]
        pos=voyageur.position
        v=voyageur.vitesse
        #print("Voyageur ",numVoy)
        d=self.vecteurDeplacement(voyageur)
        #print(" vecteur deplacement ",d[0]," ",d[1])
        posDest=[pos[0]+d[0],pos[1]+d[1]]
        if(not self.estCollision(posDest,numVoy)):
            return d

        #version 1 en escargot
        for k in range(1,2*v):
            posAlt=[posDest[0]-k,posDest[1]-k]
            for j in range(-k,k):
                posAlt[1]=posDest[1]+j
                if(not self.estCollision(posAlt,numVoy)):
                    return [posAlt[0]-pos[0],posAlt[1]-pos[1]]
            for j in range(-k,k):
                posAlt[0]=posDest[0]+j
                if(not self.estCollision(posAlt,numVoy)):
                    return [posAlt[0]-pos[0],posAlt[1]-pos[1]]
            for j in range(k,-k):
                posAlt[1]=posDest[1]+j
                if(not self.estCollision(posAlt,numVoy)):
                    return [posAlt[0]-pos[0],posAlt[1]-pos[1]]
            for j in range(k,-k):
                posAlt[0]=posDest[0]+j
                if(not self.estCollision(posAlt,numVoy)):
                    return [posAlt[0]-pos[0],posAlt[1]-pos[1]]

        """ #version deux pas de coté
        #essai d'un coté à 90 degrés
        d1=[2*d[1],-2*d[0]]
        posDest=[pos[0]+d1[0],pos[1]+d1[1]]
        if(not self.estCollision(posDest,numVoy)):
            return d1
        #essai de l'autre coté à 90 degrés
        d2=[-2*d[1],2*d[0]]
        posDest=[pos[0]+d2[0],pos[1]+d2[1]]
        if(not self.estCollision(posDest,numVoy)):
            return d2"""

        #aucun deplacement possible
        #print("deplacement nul")
        return [0,0]


    def ajoutVoyageurPorte(self,numPorte):
        #print("Parametre Porte Libre numero",numPorte," : ",self.porteLibre(numPorte))
        if(self.porteLibre(numPorte)):
            max=len(self.listePortes)
            porteDestination=alea_int(0,max-1)
            while (porteDestination==numPorte):
                porteDestination=alea_int(0,max-1)
            self.ajouterVoyageur(self.listePortes[numPorte].milieu,porteDestination)

    def porteLibre(self,numPorte):
        collision=0
        if len(self.listeVoyageurs)>0:
            r=self.listeVoyageurs[0].rayon
        else:
            return True
        p=milieu(self.listePortes[numPorte].extremite1,self.listePortes[numPorte].extremite2)
        for v in self.listeVoyageurs:
            if distance(p,v.position)<=r*2:
                collision+=1
        return (collision==0)

    def estCollisionVoyageurs(self,p,numVoy):
        collision=0
        r=self.listeVoyageurs[numVoy].rayon
        for v in self.listeVoyageurs:
            if not (v is self.listeVoyageurs[numVoy]):
                if distance(p,v.position)<=r+v.rayon:
                    collision+=1
        return (collision>0)

    def estCollisionPoteaux(self,p,numVoy):
        collision=0
        r=self.listeVoyageurs[numVoy].rayon
        for pot in self.listePoteaux:
            if distance(p,pot.position)<=r+pot.rayon:
                collision+=1
        return (collision>0)

    def estCollision(self,p,numVoy):
        return (self.estCollisionVoyageurs(p,numVoy) or self.estCollisionPoteaux(p,numVoy))

    def dessinPoteaux(self):
        for pot in self.listePoteaux:
            pot.dessinPoteau()

    def desssinPortes(self):
        for porte in self.listePortes:
            porte.dessinPorte()

    def effaceVoyageurs(self):
        for v in self.listeVoyageurs:
            pos=v.position
            Dest=milieu(self.listePortes[v.porteDeSortie].extremite1,self.listePortes[v.porteDeSortie].extremite2)
            d=distance(pos,Dest)
            if (d<2*v.rayon):
                v.effaceVoyageur()
                self.effaceVoyageur(v)

#création de la salle
s=Salle()
affiche_auto_off()

#création des portes

e1=[0,200]
e2=[2,240]
s.ajouterPorte(e1,e2,50)

e1=[760,0]
e2=[799,2]
s.ajouterPorte(e1,e2,40)

e1=[400,598]
e2=[440,600]
s.ajouterPorte(e1,e2,70)

e1=[898,400]
e2=[900,440]
s.ajouterPorte(e1,e2,90)

#Création des poteaux
pos=[450,100]
s.ajouterPoteau(pos)

pos=[550,350]
s.ajouterPoteau(pos)

pos=[730,510]
s.ajouterPoteau(pos)

pos=[200,420]
s.ajouterPoteau(pos)

s.dessinPoteaux()
s.desssinPortes()

#on commence les tours des Voyageur( vont arriver
tour=0
while (tour<150):
    print("tour=",tour)
    for k in range(len(s.listePortes)):
        s.listePortes[k].debitEnCours-=1
        if s.listePortes[k].debitEnCours==0:
            s.ajoutVoyageurPorte(k)
            s.listePortes[k].debitEnCours=s.listePortes[k].debit
    k=0
    for k in range(len(s.listeVoyageurs)):
        voyageur=s.listeVoyageurs[k]
        #print("voyageur ",k,voyageur)
        voyageur.effaceVoyageur()
        d=s.trouveDeplacement(k)
        voyageur.deplacement=d
        voyageur.deplacementVoyageur()
        voyageur.dessinVoyageur()
        k+=1
    s.effaceVoyageurs()
    affiche_all()
    attendre(100)
    tour+=1

#attente pour terminer
wait_escape(f)

quit_graphics()
