xwert = (10)
schrittgroesse = 2
groessex = 1
groessey = 1
hintergrundbild = loadImage("Hintergrund.jpg")

koord_liste = [50,100,150,200,250,300,350]
radius_liste = []


def setup():
    size(800, 500)
    
    #hintergrundbild = loadImage("Hintergrund.jpg")
    #image (hintergrundbild,0,0,800,500)
    
    swat = loadImage("SWAT.png")
    image (swat,10,380,138,86)
    
    
def wachsender_kreis(radius_liste):
    print(radius_liste)
    global hintergrundbild
    #r = 1
    noFill();
    strokeWeight(4);
    stroke(255,0,0);
    #for i in range (1,20):
        #image (hintergrundbild,0,0,800,500)
    background(240,240,240)
    for e in range (0,len(radius_liste)):
        x=koord_liste[e]
        ellipse(x,380,radius_liste[e],radius_liste[e])
    #r = i*15
   

def draw ():
    global swat
    global xwert
    global schrittgroesse
    global groessex
    global groessey
    global koord_liste
    

        
    hintergrundbild = loadImage("Hintergrund.jpg")
    image (hintergrundbild,0,0,800,500)
    swat = loadImage("SWAT.png")
    image(swat,xwert,380,117,75)     
    xwert = xwert + schrittgroesse
    #print(xwert)
    
    if xwert in koord_liste:
       radius_liste.append(1)
       
    if len(radius_liste) >= 1:
        for f in range(1,len(radius_liste)):
            radius_liste[f] = radius_liste[f] + 10
        wachsender_kreis(radius_liste)
    
    #for i in range(1,len(radius_liste)):
     #   wachsender_kreis(radius_liste[i])
    













    #wachsender_kreis(10)

       # for i in range(1,len(koord_liste)):
        #    if xwert in koord_liste:
         #       wachsender_kreis(xwert,10)
            
            
            
    #      noFill();
    #      strokeWeight(4);
    #      stroke(255,0,0);
    #      ellipse(koord_liste[i],380,groessex,groessey)
    #     groessex = groessex + 15
        #    groessey = groessey + 15
            #if xwert == 50 or 100 or 150 or 200 or 250 or 300:
                #koord_liste = append(int(xwert))

#1. Funktion, welche wächst
#2. Schleife, mit Intervall
        
        
        
    return ellipse
    return swat
    
