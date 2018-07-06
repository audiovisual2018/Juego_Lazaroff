import pygame #Importo librería
pygame.init() #Iniciador de Pygame

window = pygame.display.set_mode((500,500)) #Configuro la ventana del jeugo

pygame.display.set_caption("Waluigi-dodgeball") #Le doy el nombre al ejecutable


#Sprites


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png')]
crouchr = pygame.image.load('CR.png')
crouchl = pygame.image.load('CL.png')
jumpRight = [pygame.image.load('JR1.png'), pygame.image.load('JR2.png'), pygame.image.load('JR3.png'), pygame.image.load('JR4.png'), pygame.image.load('JR5.png'), pygame.image.load('JR6.png'), pygame.image.load('JR7.png'), pygame.image.load('JR8.png')]
jumpLeft =  [pygame.image.load('JL1.png'), pygame.image.load('JL2.png'), pygame.image.load('JL3.png'), pygame.image.load('JL4.png'), pygame.image.load('JL5.png'), pygame.image.load('JL6.png'), pygame.image.load('JL7.png'), pygame.image.load('JL8.png')]
bg = pygame.image.load('bg.png')
youwon = pygame.image.load('youwon.png')
charr = pygame.image.load('IR.png')
charl = pygame.image.load('IL.png')
firer = [pygame.image.load('TR1.png'), pygame.image.load('TR2.png'), pygame.image.load('TR3.png'), pygame.image.load('TR4.png'), pygame.image.load('TR5.png'), pygame.image.load('TR6.png')]
firel = [pygame.image.load('TL1.png'), pygame.image.load('TL2.png'), pygame.image.load('TL3.png'), pygame.image.load('TL4.png'), pygame.image.load('TL5.png'), pygame.image.load('TL6.png')]
hitR = pygame.image.load('HR.png')
hitL = pygame.image.load('HL.png')
fbR = [pygame.image.load('FR1.png'), pygame.image.load('FR2.png'), pygame.image.load('FR3.png')]
fbL = [pygame.image.load('FL1.png'), pygame.image.load('FL2.png'), pygame.image.load('FL3.png')]

BwalkRight = [pygame.image.load('WR1.png'), pygame.image.load('WR2.png'), pygame.image.load('WR3.png'), pygame.image.load('WR4.png'), pygame.image.load('WR5.png'), pygame.image.load('WR6.png'), pygame.image.load('WR7.png'), pygame.image.load('WR8.png')]
BwalkLeft = [pygame.image.load('WL1.png'), pygame.image.load('WL2.png'), pygame.image.load('WL3.png'), pygame.image.load('WL4.png'), pygame.image.load('WL5.png'), pygame.image.load('WL6.png'), pygame.image.load('WL7.png'), pygame.image.load('WL8.png')]
Bcrouchr = pygame.image.load('WCR.png')
Bcrouchl = pygame.image.load('WCL.png')
BjumpRight = [pygame.image.load('WJR1.png'), pygame.image.load('WJR2.png'), pygame.image.load('WJR3.png'), pygame.image.load('WJR4.png'), pygame.image.load('WJR5.png'), pygame.image.load('WJR6.png'), pygame.image.load('WJR7.png'), pygame.image.load('WJR8.png')]
BjumpLeft =  [pygame.image.load('WJL1.png'), pygame.image.load('WJL2.png'), pygame.image.load('WJL3.png'), pygame.image.load('WJL4.png'), pygame.image.load('WJL5.png'), pygame.image.load('WJL6.png'), pygame.image.load('WJL7.png'), pygame.image.load('WJL8.png')]
Bcharr = pygame.image.load('WIR.png')
Bcharl = pygame.image.load('WIL.png')
Bfirer = [pygame.image.load('WTR1.png'), pygame.image.load('WTR2.png'), pygame.image.load('WTR3.png'), pygame.image.load('WTR4.png'), pygame.image.load('WTR5.png'), pygame.image.load('WTR6.png')]
Bfirel = [pygame.image.load('WTL1.png'), pygame.image.load('WTL2.png'), pygame.image.load('WTL3.png'), pygame.image.load('WTL4.png'), pygame.image.load('WTL5.png'), pygame.image.load('WTL6.png')]
BhitR = pygame.image.load('WHR.png')
BhitL = pygame.image.load('WHL.png')
BfbR = [pygame.image.load('WFR1.png'), pygame.image.load('WFR2.png'), pygame.image.load('WFR3.png')]
BfbL = [pygame.image.load('WFL1.png'), pygame.image.load('WFL2.png'), pygame.image.load('WFL3.png')]


#Creo un reloj

clock = pygame.time.Clock()

#Sonidos y música

fireballSound = pygame.mixer.Sound('ha.wav')
bfireballSound = pygame.mixer.Sound('ha.wav')
hitSound = pygame.mixer.Sound('ouch.wav')
bhitSound = pygame.mixer.Sound('ouch.wav')
winSound = pygame.mixer.Sound('win.wav')
bwinSound = pygame.mixer.Sound('win.wav')

music = pygame.mixer.music.load('dreamland64.mp3')
pygame.mixer.music.play(-1)

#Puntajes de P1 y P2

score = 0
bscore = 0


#Plataformas no implementadas
        
class stub(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, self.width, 20)

    def draw(self, window):
        pass
        #pygame.draw.rect(window, (255,0,0), self.hitbox, 2)


#Clase Jugador 1        

class player(object):
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.crouching = False
        self.crouchCount = 0
        self.rjumpCount = 0
        self.ljumpCount = 0
        self.standing = True
        self.facing = facing
        self.firing = False
        self.rfireCount = 0
        self.lfireCount = 0
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.hit = False


    #Método para dibujar cada animación

    def draw(self, window):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                if self.firing == True:
                    window.blit(firel[self.lfireCount//2], (self.x, self.y))
                    self.lfireCount += 1
                    if self.lfireCount >= 12:
                        self.firing = False
                else:
                    window.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                    
            elif self.right:
                if self.firing == True:
                    window.blit(firer[self.rfireCount//2], (self.x, self.y))
                    self.rfireCount += 1
                    if self.rfireCount >= 12:
                        self.firing = False
                else:
                    window.blit(walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1

        elif self.crouching:
            if self.facing == 1:
                window.blit(crouchr, (self.x,self.y))
                self.crouchCount += 1
            if self.facing == -1:
                window.blit(crouchl, (self.x,self.y))
                self.crouchCount += 1

        elif self.isJump:
             if self.facing == 1:
                if self.firing == True:
                    window.blit(firer[self.rfireCount//2], (self.x, self.y))
                    self.rfireCount += 1
                    if self.rfireCount >= 12:
                        self.firing = False
                else:
                    window.blit(jumpRight[self.rjumpCount//3], (self.x,self.y))
                    self.rjumpCount += 1

             elif self.facing == -1:
                 if self.firing == True:
                     window.blit(firel[self.lfireCount//2], (self.x, self.y))
                     self.lfireCount += 1
                     if self.lfireCount >= 12:
                        self.firing = False
                 else:
                    window.blit(jumpLeft[self.ljumpCount//3], (self.x, self.y))
                    self.ljumpCount += 1

               
        elif self.firing:
            if self.facing == 1:
                window.blit(firer[self.rfireCount//2], (self.x, self.y))
                self.rfireCount += 1
                if self.rfireCount >= 12:
                        self.firing = False
                    
            if self.facing == -1:
                window.blit(firel[self.lfireCount//2], (self.x, self.y))
                self.lfireCount += 1
                if self.lfireCount >= 12:
                        self.firing = False

        elif self.hit:
            if self.facing == 1:
                window.blit(hitR, (self.x, self.y))
                self.hit = False
            if self.facing == -1:
                window.blit(hitL, (self.x, self.y))
                self.hit = False
            
        else:
            if self.facing == 1:
                window.blit(charr, (self.x, self.y))
            if self.facing ==-1:
                window.blit(charl, (self.x, self.y))


        #Ajuste del tamaño de la Hitbox
        self.hitbox = (self.x + 20, self.y, 28, 60)
        #pygame.draw.rect(window, (255,0,0), self.hitbox, 2)



#Clase jugador 2:

class player2(object):
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.crouching = False
        self.crouchCount = 0
        self.rjumpCount = 0
        self.ljumpCount = 0
        self.standing = True
        self.facing = facing
        self.firing = False
        self.rfireCount = 0
        self.lfireCount = 0
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.hit = False

    #Método para dibujar cada animación de Jugador 2

    def draw(self, window):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                if self.firing == True:
                    window.blit(Bfirel[self.lfireCount//2], (self.x, self.y))
                    self.lfireCount += 1
                    if self.lfireCount >= 12:
                        self.firing = False
                else:
                    window.blit(BwalkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                    
            elif self.right:
                if self.firing == True:
                    window.blit(Bfirer[self.rfireCount//2], (self.x, self.y))
                    self.rfireCount += 1
                    if self.rfireCount >= 12:
                        self.firing = False
                else:
                    window.blit(BwalkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1

        elif self.crouching:
            if self.facing == 1:
                window.blit(Bcrouchr, (self.x,self.y))
                self.crouchCount += 1
                    
            if self.facing == -1:
                window.blit(Bcrouchl, (self.x,self.y))
                self.crouchCount += 1

        elif self.isJump:
             if self.facing == 1:
                if self.firing == True:
                    window.blit(Bfirer[self.rfireCount//2], (self.x, self.y))
                    self.rfireCount += 1
                    if self.rfireCount >= 12:
                        self.firing = False
                else:
                    window.blit(BjumpRight[self.rjumpCount//3], (self.x,self.y))
                    self.rjumpCount += 1
                    

             elif self.facing == -1:
                 if self.firing == True:
                     window.blit(Bfirel[self.lfireCount//2], (self.x, self.y))
                     self.lfireCount += 1
                     if self.lfireCount >= 12:
                        self.firing = False
                 else:
                    window.blit(BjumpLeft[self.ljumpCount//3], (self.x, self.y))
                    self.ljumpCount += 1

               
        elif self.firing:
            if self.facing == 1:
                window.blit(Bfirer[self.rfireCount//2], (self.x, self.y))
                self.rfireCount += 1
                if self.rfireCount >= 12:
                        self.firing = False
                    
            if self.facing == -1:
                window.blit(Bfirel[self.lfireCount//2], (self.x, self.y))
                self.lfireCount += 1
                if self.lfireCount >= 12:
                        self.firing = False

        elif self.hit:
            if self.facing == 1:
                window.blit(BhitR, (self.x, self.y))
                self.hit = False
            if self.facing == -1:
                window.blit(BhitL, (self.x, self.y))
                self.hit = False

        
        else:
            if self.facing == 1:
                window.blit(Bcharr, (self.x, self.y))
            if self.facing ==-1:
                window.blit(Bcharl, (self.x, self.y))

        #Hitbox jugador 2

        self.hitbox = (self.x + 20, self.y, 28, 60)
        #pygame.draw.rect(window, (255,0,0), self.hitbox, 2)



#Clase bola de fuego, proyectil del juego.

class fireball(object):
    def __init__(self, x,y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10 * facing
        self.fbCount = 0

    #Método para dibujar la bola de fuego.

    def draw(self, window):

        if self.facing > 0:
            window.blit(fbR[self.fbCount//1], (self.x, self.y))
            self.fbCount += 1
            if self.fbCount == 3:
                self.fbCount = 0

        if facing < 0:
            window.blit(fbL[self.fbCount//1], (self.x, self.y))
            self.fbCount += 1
            if self.fbCount == 3:
                self.fbCount = 0

        
            
#Función que actualiza todo lo que ocurre en pantalla, dibuja personajes, proyectiles, score, fondo, étc.
        

def redrawGameWindow():
    if bscore < 10 and score < 10:
        window.blit(bg, (0,0)) #Refresca la imagen de fondo durante cada movimiento
        text = font.render("Golpes: " + str(score), 1, (0,0,0))
        text2 = font.render("Golpes: " + str(bscore), 1, (0,0,0))
        window.blit(text, (300, 10))
        window.blit(text2, (70, 10))
        waluigi.draw(window)
        bwaluigi.draw(window)
        stub1.draw(window)
        stub2.draw(window)
        stub3.draw(window)
        for bullet in bullets:
            bullet.draw(window)

    #If´s que determinan el final del juego.
    
    if bscore == 10:
        waluigi.x = 225
        waluigi.y = 260
        window.blit(youwon, (0,0)) #Refresca la imagen de fondo durante cada movimiento
        waluigi.draw(window)
        winSound.play()
        
    if score == 10:
        bwaluigi.x = 225
        bwaluigi.y = 260
        window.blit(youwon, (0,0)) #Refresca la imagen de fondo durante cada movimiento
        bwaluigi.draw(window)
        bwinSound.play()
            


    pygame.display.update() #Hago que el display se actualice así pueden verse


#Creación de los jugadores, plataformas fallidas, letras de los scores, étc.

font = pygame.font.SysFont('verdana', 24, True)
stub1 = stub(64, 244, 95, 20)
stub2 = stub(347, 244, 95, 20)
stub3 = stub(195, 150, 115, 20)
waluigi = player(100,290,64,64,1)
bwaluigi = player2(370, 290, 64, 64, -1)
shootLoop = 0
bullets = []
run = True # Variable del programa que indica si funciona
while run:  # Main Loop, fundamental
    clock.tick(24) #cantidad de FPS del juego

    # If que evita el multi-tiro de bolas de fuego, para tiras dos quedan con un espaciamiento.
    
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 2:
        shootLoop = 0

    for event in pygame.event.get(): #Cualquier input del usuario
        if event.type == pygame.QUIT:
            run = False #Cierra el programa al tocar cruz roja

    # Relacionado con el proyectil

    for bullet in bullets:
        if bullet.y - bullet.radius < waluigi.hitbox[1] + waluigi.hitbox[3] and bullet.y + bullet.radius > waluigi.hitbox[1]:
            if bullet.x + bullet.radius > waluigi.hitbox[0] and bullet.x - bullet.radius < waluigi.hitbox[0] + waluigi.hitbox[2]:
                hitSound.play()
                bullets.pop(bullets.index(bullet))
                waluigi.hit = True
                score += 1
        if bullet.y - bullet.radius < bwaluigi.hitbox[1] + bwaluigi.hitbox[3] and bullet.y + bullet.radius > bwaluigi.hitbox[1]:
            if bullet.x + bullet.radius > bwaluigi.hitbox[0] and bullet.x - bullet.radius < bwaluigi.hitbox[0] + bwaluigi.hitbox[2]:
                bhitSound.play()
                bullets.pop(bullets.index(bullet))
                bwaluigi.hit = True
                bscore += 1
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    #Intento fallido de lograr las plataformas a tiempo

    if waluigi.hitbox[1] + waluigi.hitbox [3] < stub1.hitbox[1]:
        if waluigi.x+20 > stub1.hitbox[0] and waluigi.x+30 < stub1.hitbox[0] + stub1.hitbox[2]:
            pass
            

    keys = pygame.key.get_pressed() #Acumulo en una lista los comandos de las teclas para pygame


    #Inhabilito tirar bolas de fuego mientras está el jugador agachado y seteo las teclas para cada cosa.

    if not(waluigi.crouching):
         if keys[pygame.K_p] and shootLoop == 0 :
             
            if waluigi.facing == 1:
                waluigi.firing = True            
                facing = 1
                waluigi.rfireCount = 0
                if len(bullets) < 2:
                    bullets.append(fireball(round(waluigi.x + waluigi.width + 2), round(waluigi.y + waluigi.height//2), 10, (0,0,255), waluigi.facing))
                    fireballSound.play()
            
                            
            if waluigi.facing == -1:
                waluigi.firing = True
                facing = -1
                waluigi.lfireCount = 0
                if len(bullets) < 2:
                    bullets.append(fireball(round(waluigi.x - 2), round(waluigi.y + waluigi.height//2), 10, (0,0,255), waluigi.facing))
                    fireballSound.play()

            shootLoop = 1

    if keys[pygame.K_LEFT] and waluigi.x > waluigi.vel - 5:
        waluigi.x -= waluigi. vel
        waluigi.left = True
        waluigi.right = False
        waluigi.crouching = False
        waluigi.standing = False
        waluigi.facing = -1
    
    elif keys[pygame.K_RIGHT] and waluigi.x < 500 - waluigi.width - waluigi.vel:
        waluigi.x += waluigi.vel
        waluigi.left = False
        waluigi.right = True
        waluigi.crouching = False
        waluigi.standing = False
        waluigi.facing = 1
    else:
        waluigi.standing = True
        waluigi.crouching = False
        waluigi.walkCount = 0
    if not(waluigi.isJump):
        if keys[pygame.K_UP] and waluigi.y > waluigi.vel - 5:
            if waluigi.right:
                waluigi.isJump = True
                waluigi.rjump = True
                waluigi.ljump = False
                waluigi.right = False
                waluigi.left = False
                waluigi.crouching = False
                waluigi.walkCount = 0
                waluigi.rjumpCount = 0
                waluigi.ljumpCount = 0
                waluigi.standing= False
                waluigi.facing = 1
            elif waluigi.left:
                waluigi.isJump = True
                waluigi.rjump = False
                waluigi.ljump = True
                waluigi.right = False
                waluigi.left = False
                waluigi.crouching = False
                waluigi.walkCount = 0
                waluigi.rjumpCount = 0
                waluigi.ljumpCount = 0
                waluigi.standing= False
                waluigi.facing = -1
            else:
                if waluigi.facing == 1: 
                    waluigi.isJump = True
                    waluigi.rjump = True
                    waluigi.ljump = False
                    waluigi.right = False
                    waluigi.left = False
                    waluigi.crouching = False
                    waluigi.walkCount = 0
                    waluigi.rjumpCount = 0
                    waluigi.ljumpCount = 0
                    waluigi.standing= False
                elif waluigi.facing == -1:
                    waluigi.isJump = True
                    waluigi.rjump = False
                    waluigi.ljump = True
                    waluigi.right = False
                    waluigi.left = False
                    waluigi.crouching = False
                    waluigi.walkCount = 0
                    waluigi.rjumpCount = 0
                    waluigi.ljumpCount = 0
                    waluigi.standing= False

        if keys[pygame.K_DOWN]:
            waluigi.isJump = False
            waluigi.right = False
            waluigi.left = False
            waluigi.crouching = True
            waluigi.walkCount = 0
            waluigi.crouchCount = 0

    if (waluigi.isJump):
        if waluigi.jumpCount >= -10:
            neg = 1
            if waluigi.jumpCount < 0:
                neg = -1
            waluigi.y -= (waluigi.jumpCount ** 2) * 0.3 * neg
            waluigi.jumpCount -= 1

        else:
            waluigi.isJump= False
            waluigi.jumpCount = 10


    if not(bwaluigi.crouching):
         if keys[pygame.K_LCTRL] and shootLoop == 0 :
             
            if bwaluigi.facing == 1:
                bwaluigi.firing = True            
                facing = 1
                bwaluigi.rfireCount = 0
                if len(bullets) < 2:
                    bullets.append(fireball(round(bwaluigi.x + bwaluigi.width + 2), round(bwaluigi.y + bwaluigi.height//2), 10, (0,0,255), waluigi.facing))
                    fireballSound.play()
            
                            
            if bwaluigi.facing == -1:
                bwaluigi.firing = True
                facing = -1
                bwaluigi.lfireCount = 0
                if len(bullets) < 2:
                    bullets.append(fireball(round(bwaluigi.x - 2), round(bwaluigi.y + bwaluigi.height//2), 10, (0,0,255), bwaluigi.facing))
                    fireballSound.play()

            shootLoop = 1


    if keys[pygame.K_a] and bwaluigi.x > bwaluigi.vel - 5:
        bwaluigi.x -= bwaluigi.vel
        bwaluigi.left = True
        bwaluigi.right = False
        bwaluigi.crouching = False
        bwaluigi.standing = False
        bwaluigi.facing = -1

    elif keys[pygame.K_d] and bwaluigi.x < 500 - bwaluigi.width - bwaluigi.vel:
        bwaluigi.x += waluigi.vel
        bwaluigi.left = False
        bwaluigi.right = True
        bwaluigi.crouching = False
        bwaluigi.standing = False
        bwaluigi.facing = 1

    else:
        bwaluigi.standing = True
        bwaluigi.crouching = False
        bwaluigi.walkCount = 0

    if not(bwaluigi.isJump):
        if keys[pygame.K_w] and bwaluigi.y > bwaluigi.vel - 5:
            if bwaluigi.right:
                bwaluigi.isJump = True
                bwaluigi.rjump = True
                bwaluigi.ljump = False
                bwaluigi.right = False
                bwaluigi.left = False
                bwaluigi.crouching = False
                bwaluigi.walkCount = 0
                bwaluigi.rjumpCount = 0
                bwaluigi.ljumpCount = 0
                bwaluigi.standing= False
                bwaluigi.facing = 1
            elif bwaluigi.left:
                bwaluigi.isJump = True
                bwaluigi.rjump = False
                bwaluigi.ljump = True
                bwaluigi.right = False
                bwaluigi.left = False
                bwaluigi.crouching = False
                bwaluigi.walkCount = 0
                bwaluigi.rjumpCount = 0
                bwaluigi.ljumpCount = 0
                bwaluigi.standing= False
                bwaluigi.facing = -1
            else:
                if bwaluigi.facing == 1: 
                    bwaluigi.isJump = True
                    bwaluigi.rjump = True
                    bwaluigi.ljump = False
                    bwaluigi.right = False
                    bwaluigi.left = False
                    bwaluigi.crouching = False
                    bwaluigi.walkCount = 0
                    bwaluigi.rjumpCount = 0
                    bwaluigi.ljumpCount = 0
                    bwaluigi.standing= False
                elif bwaluigi.facing == -1:
                    bwaluigi.isJump = True
                    bwaluigi.rjump = False
                    bwaluigi.ljump = True
                    bwaluigi.right = False
                    bwaluigi.left = False
                    bwaluigi.crouching = False
                    bwaluigi.walkCount = 0
                    bwaluigi.rjumpCount = 0
                    bwaluigi.ljumpCount = 0
                    bwaluigi.standing= False

        if keys[pygame.K_s]:
            bwaluigi.isJump = False
            bwaluigi.right = False
            bwaluigi.left = False
            bwaluigi.crouching = True
            bwaluigi.walkCount = 0
            bwaluigi.crouchCount = 0
        
        
                        
    if (bwaluigi.isJump):
        if bwaluigi.jumpCount >= -10:
            neg = 1
            if bwaluigi.jumpCount < 0:
                neg = -1
            bwaluigi.y -= (bwaluigi.jumpCount ** 2) * 0.3 * neg
            bwaluigi.jumpCount -= 1

        else:
            bwaluigi.isJump= False
            bwaluigi.jumpCount = 10

            


#Ejecuto la función redrawGameWindow para poder actualizar los movimientos en la pantalla.

    redrawGameWindow()

    
pygame.quit()


