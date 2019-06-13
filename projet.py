# Créé par Aurélie, le 12/06/2019 en Python 3.4
from graphics import *

#Définition de la taille de la fenêtre
LARGEUR=900
HAUTEUR=600
f=init_graphics(LARGEUR,HAUTEUR)



class Voyageur:
    def __init__(self,p,d,numPorte):
        self.position=p
        self.rayon=5
        self.deplacement=d
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
        self.milieu=[(p1[0]+p2[0])//2,(p1[1]+p2[1])//2]
        self.debit=d
        self.debitEnCours=d
        self.couleur=cyan

    def dessinPorte(self):
        draw_fill_rectangle(self.extremite1,self.extremite2,self.couleur,f)

class Poteau :
    def __init__(self,p):
        self.position=p
        self.rayon=30
        self.couleur=jaune

    def dessinPoteau(self):
        draw_fill_circle(self.position,self.rayon,self.couleur,f)

class Salle :
    def __init__(self):
        self.listeVoyageurs=[]
        self.listePortes = []
        self.listePoteaux=[]

    def ajouterVoyageur(self,p,v,numPorte): #voyageur est un objet de la classe Voyageur
        voyageur = Voyageur(p,v,numPorte)
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

    def vecteurDeplacement(self,pos,numPorte,v):
        dest=self.listePortes[numPorte].milieu
        n=distance(pos,dest)
        dx=round((dest[0]-pos[0])*v/n)
        dy=round((dest[1]-pos[1])*v/n)
        return [dx,dy]
        
    def trouveDeplacement(self,numVoy):
        voyageur=self.listeVoyageurs[numVoy]
        pos=voyageur.position
        v=voyageur.vitesse
        porteDest=voyageur.porteDeSortie
        d=self.vecteurDeplacement(pos,porteDest,v)
        posDest=[pos[0]+d[0],pos[1]+d[1]]
        if(not self.estCollision(posDest,numVoy)):
            return d
        for k in range(v):
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
        print("deplacement nul")
        return [0,0]
    
    
    def ajoutVoyageurPorte(self,numPorte):
        if(self.porteLibre(numPorte)):
            max=len(self.listePortes)
            porteDestination=alea_int(0,max-1)
            while (porteDestination==numPorte):
                porteDestination=alea_int(0,max-1)
            v=self.vecteurDeplacement(self.listePortes[numPorte].milieu,porteDestination,5)
            self.ajouterVoyageur(self.listePortes[numPorte].milieu,v,porteDestination)

    def porteLibre(self,numPorte):
        collision=0
        if len(self.listeVoyageurs)>0:
            r=self.listeVoyageurs[0].rayon
        else:
            return True
        p=self.listePortes[numPorte].milieu
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
            

#création de la salle
s=Salle()

#création des portes

e1=[0,200]
e2=[2,240]
s.ajouterPorte(e1,e2,5)

e1=[860,0]
e2=[899,2]
s.ajouterPorte(e1,e2,10)

e1=[400,598]
e2=[440,600]
s.ajouterPorte(e1,e2,15)

e1=[898,400]
e2=[900,440]
s.ajouterPorte(e1,e2,22)

#Création des poteaux
pos=[500,220]
s.ajouterPoteau(pos)

pos=[700,400]
s.ajouterPoteau(pos)

pos=[200,510]
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
    for k in range(len(s.listeVoyageurs)):
        s.listeVoyageurs[k].effaceVoyageur()
        #d=s.trouveDeplacement(k)
        s.listeVoyageurs[k].deplacement=s.vecteurDeplacement(s.listeVoyageurs[k].position,s.listeVoyageurs[k].porteDeSortie,s.listeVoyageurs[k].vitesse)
        s.listeVoyageurs[k].deplacementVoyageur()
        s.listeVoyageurs[k].dessinVoyageur()
    attendre(500)    
    tour+=1    
            
#attente pour terminer
wait_escape(f)

quit_graphics()
             