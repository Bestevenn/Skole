import math
import pygame
from random import randint


pygame.init
pygame.font.init()


pygame.display.set_caption("Bilspill")
x_vin, y_vin = (1280), (720)
backgrunn = (30, 30, 30)
farge_ball = (138, 180, 248)
fps = 120
vindu = pygame.display.set_mode((x_vin, y_vin))
clock = pygame.time.Clock()
green = (0, 255, 0)
blue = (0, 0, 128)
kant = 50



Bilde = pygame.image.load("Bilspill/BIlder til bilspill/racecar.png")
bane = pygame.image.load("Bilspill/BIlder til bilspill/track3.jpg")
rent_bilde = pygame.image.load("Bilspill/BIlder til bilspill/track2.png")




start_x = 110 
start_y = 400
radius = 50
dx_aks = 1.0
R = 2.5
grader = 180
x_kod_ball = start_x
y_kod_ball = start_y
fart = 0.001

# gjør det mulig å stoppe aks
aks_opp = True
aks_ned = True

mål = False

# teller og tekst
Antall_treff = 0
poeng_verdi_system = 0
font = pygame.font.SysFont('arial', 32)
x_font = 600
y_font = 400
y_font2 = 400 + 100
def vis_poeng(x,y):
    poeng = font.render("Antall treff: " + str(Antall_treff),True,(255,255,255))
    vindu.blit(poeng,(x, y))


# klokke
stoppeklokke_minutter = 0
stoppeklokke_sek = 0
stoppeklokke_millisekk = 0
start_stoppeklokke = False


# klokke tegner 
def timer(x,y):
    if mål == False:
        poeng = font.render(f"0{stoppeklokke_minutter}:{stoppeklokke_sek}:{stoppeklokke_millisekk}",True,(255,255, 255))
        vindu.blit(poeng,(x, y))
    if mål == True:
        poeng = font.render("",True,(255,255, 255))
        vindu.blit(poeng,(x, y))




def vis_checkpoint(x,y):
    global mål
    if mål == False:
        poeng = font.render("Du er på checkpoint: " + str(status_checkpoint),True,(checkpoint_farge))
        vindu.blit(poeng,(x, y))
    if mål == True:
        poeng = font.render(f" Mål! din tid: 0{stoppeklokke_minutter}:{stoppeklokke_sek}:{stoppeklokke_millisekk}",True,(255,255, 255))
        vindu.blit(poeng,(x, y))







# bil tegner med rotasjon
def tegnfigur(vindu1, fig, punkt, vinkel):
    rotertbilde = pygame.transform.rotate(fig, vinkel)
    x = punkt[0]
    y = punkt[1]
    vindu1.blit(rotertbilde, rotertbilde.get_rect(
        center=fig.get_rect(center=(x, y)).center).topleft)



#checkpoints

checkpoint_nr1,checkpoint_nr1_kod_x,checkpoint_nr1_kod_y,checkpoint_nr1_grader = (234,125,69),(250),(100),(90)
checkpoint_nr2, checkpoint_nr2_kod_x, checkpoint_nr2_kod_y,checkpoint_nr2_grader = (125,70,234),(881),(169),(144)
checkpoint_nr3, checkpoint_nr3_kod_x, checkpoint_nr3_kod_y, checkpoint_nr3_grader = (70,179,235),(1099),(582),(-44)
checkpoint_nr4,checkpoint_nr4_kod_x, checkpoint_nr4_kod_y, checkpoint_nr4_grader = (225,70,236),(577),(650),(-90)
checkpoint_mål,checkpoint_mål_kod_x, checkpoint_mål_kod_y, checkpoint_mål_grader = (255,250,0),(110),(398),(90)
status_checkpoint = 0
checkpoint_farge = (0, 0, 0)

# Funksjon som sender deg tilbake til checkpointet
def start_nytt(pros_x, pros_y,antall_grader):
    global x_kod_ball
    global y_kod_ball
    global fart
    global Antall_treff
    global grader
    x_kod_ball = pros_x
    y_kod_ball = pros_y
    fart = 0.001
    Antall_treff = 0 
    grader = antall_grader

# lar meg svslutte
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    
    # bakgrunn
    vindu.fill(backgrunn)
    vindu.blit(bane,(0,0))
    
    # Mekanikken til bilen
    key = pygame.key.get_pressed()
    # Test for pil ned
    if key[pygame.K_LEFT]:
        grader += 3
        # Test for pil opp
    elif key[pygame.K_RIGHT]:
        grader -= 3
    elif key[pygame.K_ESCAPE]:
        pygame.quit()
    elif key[pygame.K_UP]:
        if aks_opp == True:
            fart += 0.08
            start_stoppeklokke = True
    elif key[pygame.K_DOWN]:
        if aks_ned == True:
            if stoppeklokke_sek > 2:
                fart -= 0.08
    elif key[pygame.K_TAB]:
        # sender deg tilbake til daværende checkpoint
        if status_checkpoint == 1:
            x_kod_ball , y_kod_ball, grader = checkpoint_nr1_kod_x, checkpoint_nr1_kod_y ,checkpoint_nr1_grader
            fart = 0.001
        elif status_checkpoint == 2:
            x_kod_ball , y_kod_ball, grader = checkpoint_nr2_kod_x, checkpoint_nr2_kod_y, checkpoint_nr2_grader
            fart = 0.001
        elif status_checkpoint == 3:
            x_kod_ball , y_kod_ball, grader = checkpoint_nr3_kod_x, checkpoint_nr3_kod_y, checkpoint_nr3_grader
            fart = 0.001
        elif status_checkpoint == 4:
            x_kod_ball , y_kod_ball, grader = checkpoint_nr4_kod_x, checkpoint_nr4_kod_y , checkpoint_nr4_grader
            fart = 0.001

    elif key[pygame.K_SPACE]: 
        start_nytt(start_x, start_y,180)
        checkpoint_farge = (69,235,125)
        start_stoppeklokke = False
        stoppeklokke_minutter = 0
        stoppeklokke_sek = 0 
        stoppeklokke_millisekk = 0
        status_checkpoint = 0 
        checkpoint_farge = (0,0,0)
        aks_opp = True
        aks_ned = True
        mål = False

    x_kod_ball += fart*math.sin(grader*math.pi/180)
    y_kod_ball += fart*math.cos(grader*math.pi/180)

    # stoppekloppe
    if start_stoppeklokke == True:
        stoppeklokke_millisekk += 1
        if stoppeklokke_millisekk == 60:
            stoppeklokke_sek += 1
            stoppeklokke_millisekk = 0
            if stoppeklokke_sek == 60:
                stoppeklokke_minutter += 1
                stoppeklokke_sek = 0

    # Gjør det umulig å kjøre utenfor kartet
    if x_kod_ball > x_vin - radius - kant:
        x_kod_ball = x_vin - radius - kant
    if x_kod_ball < 0 - radius + kant:
        x_kod_ball = 0 - radius + kant
    if y_kod_ball > y_vin - radius: 
        y_kod_ball = y_vin - radius 
    if y_kod_ball < 0 - radius + kant:
        y_kod_ball = 0 - radius + kant
    
    # fargegjennkjennig ti bilen
    farge_bil = bane.get_at((int(x_kod_ball), int(y_kod_ball)))
    
    # checkpointsystem i verdensklasse :)
    if farge_bil == checkpoint_nr1:
        status_checkpoint = 1
        checkpoint_farge = checkpoint_nr1
    elif farge_bil == checkpoint_nr2:
        status_checkpoint = 2
        checkpoint_farge = (255,250,0)
    elif farge_bil == checkpoint_nr3:
        status_checkpoint = 3
        checkpoint_farge = checkpoint_nr3
    elif farge_bil == checkpoint_nr4:
        status_checkpoint = 4
        checkpoint_farge = checkpoint_nr4
    elif farge_bil == checkpoint_mål:
        if stoppeklokke_sek > 2:
            start_stoppeklokke = False
            aks_opp = False
            aks_ned = False
            fart =  0
            mål = True



    # Poengsystem med tregere oppdatring
    if farge_bil == (69,235,125) or farge_bil == (50,124,11):
        if Antall_treff == 0:
            Antall_treff = 1
        poeng_verdi_system += 1
        if poeng_verdi_system == 50:
            Antall_treff += 1
            poeng_verdi_system = 0
        if Antall_treff >= 1:
            fart /= 1.1112
    
        # sender deg tilbake til checkpointet ditt dersom du får treff = 10
        if Antall_treff == 1000:
            if status_checkpoint == 0:
                start_nytt(start_x, start_y,180)        
            elif status_checkpoint == 1:
                start_nytt(checkpoint_nr1_kod_x, checkpoint_nr1_kod_y,checkpoint_nr1_grader)
            elif status_checkpoint == 2:
                start_nytt(checkpoint_nr2_kod_x,checkpoint_nr2_kod_y,checkpoint_nr2_grader)
            elif status_checkpoint == 3:
                start_nytt(checkpoint_nr3_kod_x,checkpoint_nr3_kod_y,checkpoint_nr3_grader)
            elif status_checkpoint == 4:
                start_nytt(checkpoint_nr4_kod_x,checkpoint_nr4_kod_y,checkpoint_nr4_grader)
            elif status_checkpoint == 5:
                print
        
    print(x_kod_ball, y_kod_ball)
    vindu.blit(rent_bilde,(0,0))
    timer(220, 221)
    vis_poeng(904, 247)
    vis_checkpoint(510, 438)
    tegnfigur(vindu, Bilde, (x_kod_ball, y_kod_ball), grader)
    clock.tick(fps)
    pygame.display.flip()
    pygame.display.update()


