# Créé par Aurélie, le 12/06/2019 en Python 3.4

from random import*
# Je suppose que notre image tient dans un rectangle de longeur(x) longueur et de largeur(y) largeur
xmax=int(input("veuillez donner la longueur du cadre"))
ymax=int(input("veuillez donner la largeur du cadre"))

tableauPoteaux =[[xmax/4,ymax/2],[2*xmax/4,2*ymax/3],[3*xmax/4,ymax/3]] # 3 poteaux dont j'ai fixé les coordonnées du centre
tableauPortes = [[xmax/2,0],[xmax,ymax/3],[2*xmax/3,ymax],[0,3*ymax/4]] # j'ai fixé les coordonnées du centre des 4 portes
tableauVoyageurs =[]

class Voyageur:
    def __init__(self,px,py,pNumeroPorteSortie): # px et py sont des réels ; pNumeroPorteSortie est un entier pour stocker la porte de sortie
        self.abscisse=px
        self.ordonnee=py
        self.numeroPorteSortie = pNumeroPorteSortie

    def deplacerUnVoyageur(self):
        if pasDePoteaux() and pasDeVoyageurs():
            self.abscisse, self.ordonnee= nouvelleCoordonnees(self.abscisse,self.ordonnee,tableauPortes[self.numeroPorteSortie][0],tableauPortes[self.numeroPorteSortie][1])
        elif pasDeVoyageurs(): # le problème vient donc du poteau
            # j essaie de voir pour dévier la trajectoire linéaire
            self.abscisse, self.ordonnee= nouvelleCoordonnees1(self.abscisse,self.ordonnee,tableauPortes[self.numeroPorteSortie][0],tableauPortes[self.numeroPorteSortie][1])
        else : # le problème vient donc d'un voyageur
            # j essaie de voir
            self.abscisse, self.ordonnee= nouvelleCoordonnees2(self.abscisse,self.ordonnee,tableauPortes[self.numeroPorteSortie][0],tableauPortes[self.numeroPorteSortie][1])




def pasDePoteaux(pVoyageur) : # en paramètre, il faut une instance de la classe Voyageur
    for i in range(0,len(tableauPoteaux)):
        distancePoteau = sqrt((pVoyageur.abscisse-tableauPoteaux[i][0])**2+(pVoyageur.ordonnee-tableauPoteaux[i][1])**2)
        if distancePoteau < 18: # je suppose que la personne est de largeur 5 et avance de 3 et le poteau est de rayon 10
            return false
    return true

def pasDeVoyageurs(pVoyageur): #en paramètre, il me faut une instance de la classe Voyageur
    # n'ayant pas fait de tri dans le tableau qui stocke les voyageurs, je dois balayer tout le tableau
    for i in range(0,len(tableauVoyageurs)):
        # on teste si la distance entre mon voyageur et les autres voyageurs est plus petite que 3
        ## il faut modifier le code de sorte qu'en plus, si voyageur gene, il est bien devant et non derriere nous. En effet, cela va poser un probleme au démarrage si je ne fais pas cela.
        if(((pVoyageur.abscisse-tableauVoyageurs[i].abscisse)**2+(pVoyageur.ordonnee-tableauVoyageurs[i].ordonnee)**2)<9):
            return false
    return true

def nouvelleCoordonnee(pXancien,pYancien,pXvise,pYvise):
    # je cherche les nouvelles coordonnées quand il n y a pas de risque de collision
    coefficientDirecteur = (pYvise-pYancien)/(pXvise-pXancien) # formule de seconde pour le coeff directeur d'une droite
    discriminant = 4(1+coefficientDirecteur**2)*(9-(coefficientDirecteur*pXancien)**2) # après résolution d'une equation, je suis tombée sur ce discriminant
    premierX=(2*pXancien*(1+coefficientDirecteur**2)-sqrt(discriminant))/(2*(1+coefficientDirecteur**2)) #premiere solution de mon equation
    deuxiemeX=(2*pXancien*(1+coefficientDirecteur**2)+sqrt(discriminant))/(2*(1+coefficientDirecteur**2)) # deuxieme solution de mon equation
    if ((pXancien<premierX and premierX<pXvise) or (pXancien>premierX and premierX>pXvise)) : # il y a deux points distants de 3, il faut prendre celui qui nous fait avancer
        y=coefficientDirecteur*premierX+(pYancien-discriminant*pXancien) # l'equation de la droite
        return premierX,y
    else:
        y=coefficientDirecteur*deuxiemeX+(pYancien-discriminant*pXancien) # l'equation de la droite
        return premierX,y

def nouvelleCoordonnee1(pXancien,pYancien,pXvise,pYvise): # qd le problème vient du poteau
    xSiPasProbleme,ySiPasProbleme=nouvelleCoordonnee(pXancien,pYancien,pXvise,pYvise)
    ## à travailler demain : il faut que je connaisse le poteau qui pose problème pour pouvoir le contourner

def nouvelleCoordonnee2(pXancien,pYancien,pXvise,pYvise): # qd le problème vient d'un voyageur
    xSiPasProbleme,ySiPasProbleme=nouvelleCoordonnee(pXancien,pYancien,pXvise,pYvise)
    ## à travailler demain : il faut que je connaisse le voyageur qui pose problème pour pouvoir le contourner

def main() :
    compteur = 0
    while compteur < 5000:
        compteur =compteur+1
        # dans cette partie, je créée un nombre aléatoire de voyageurs, ils ont une porte d'entrée et une porte de sortie aléatoirement
        nbVoyageurs=randrange(1,20,1)
        for i in range(0,nbVoyageurs) :
            numeroPorteEntree = randrange(0,3,1)
            numeroPorteSortie = randrange(0,3,1)
            while numeroPorteEntree == numeroPorteSortie:  # cette boucle sert à ce que la porte de sortie ne soit pas la meme que la porte d'entrée
                numeroPorteSortie=randrange(0,3,1)
            unVoyageur =Voyageur(tableauPortes[numeroPorteEntree][0],tableauPortes[numeroPorteEntree][0],numeroPorteSortie)
            tableauVoyageurs.append(unVoyageur) # je stocke dans un tableau tous mes voyageurs
        # Dans cette partie, je me ballade dans le tableau tableauVoyageurs pour faire bouger tous les voyageurs
        for i in range(0,len(tableauVoyageurs)):
            deplacerUnVoyageur(tableauVoyageurs[i])



main()




