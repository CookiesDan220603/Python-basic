from imports import*
class Shot(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.Surface([6,6])
        pygame.draw.circle(self.image, [255,255,255],[3,3],3)
        self.image.set_colorkey([0,0,0])

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos)

        self.direction = direction

    def update(self, screen):
        if self.direction=='right': self.rect = self.rect.move(5,0)
        else:self.rect = self.rect.move(-5,0)
        screen.blit(self.image, self.rect)



class Ship(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("ship.gif")
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(size[0]/8,size[1]/2)

        self.speed = 4

    def update(self, screen, keys, size):
        
        #move
        if keys[K_UP]:
            self.rect = self.rect.move(0,-self.speed)
        if keys[K_DOWN]:
            self.rect = self.rect.move(0,self.speed)
        if keys[K_LEFT]:
            self.rect = self.rect.move(-self.speed,0)
        if keys[K_RIGHT]:
            self.rect = self.rect.move(self.speed,0)

        #bounce
        if self.rect.top<0:
            self.rect = self.rect.move(0,self.speed)
        if self.rect.bottom>size[1]:
            self.rect = self.rect.move(0,-self.speed)
        if self.rect.left<0:
            self.rect = self.rect.move(self.speed,0)
        if self.rect.right>size[0]:
            self.rect = self.rect.move(-self.speed,0)

        #render
        screen.blit(self.image, self.rect)



class Enemy1(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("enemy1.gif")
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(pos)

        self.speed = random.randint(-2,-1)

    def update(self, screen, time, ship):

        self.rect = self.rect.move([self.speed,0])
        screen.blit(self.image, self.rect)

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, pos, shot_list):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("enemy2.gif")
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(pos)

        self.speed = random.randint(-2,-1)

        self.shot_list = shot_list

    def update(self, screen, time, ship):
        if ship != None:

            if  abs(ship.rect.center[1]-self.rect.center[1])<10 and time%20==0:
                self.shot_list.append(Shot(self.rect.center, 'left'))

            if time%2:
                if ship.rect.center[1]-self.rect.center[1]<0:
                    self.rect = self.rect.move(0,-1*-self.speed)
                if ship.rect.center[1]-self.rect.center[1]>0:
                    self.rect = self.rect.move(0,1*-self.speed)

        self.rect = self.rect.move([self.speed,0])
        screen.blit(self.image, self.rect)



class Enemy3(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("enemy3.gif")
        
        ####
        self.image.set_colorkey([255,255,255])
        ####
        
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(pos)

        self.speed = -6

    def update(self, screen, time, ship):
        if ship != None:
            if time%2:
                if ship.rect.center[1]-self.rect.center[1]<0:
                    self.rect = self.rect.move(0,-1*-self.speed)
                if ship.rect.center[1]-self.rect.center[1]>0:
                    self.rect = self.rect.move(0,1*-self.speed)

        self.rect = self.rect.move([self.speed,0])
        screen.blit(self.image, self.rect)

class Partical(pygame.sprite.Sprite):
    def __init__(self, pos, life):
        self.image = pygame.Surface([3,3])
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos)

        self.life = life
        self.maxlife = life

        self.v_pos = [float(self.rect.center[0]),float(self.rect.center[1])]

        self.direction = [random.randint(1.0,50.0)*(random.randint(0,1)*2-1),random.randint(1.0,50.0)*(random.randint(0,1)*2-1)]
        self.magnitude = math.sqrt( self.direction[0]**2  +  self.direction[1]**2 )
        self.speed = random.randint(1,100)/33.333

        self.direction[0] = self.direction[0]/self.magnitude*self.speed
        self.direction[1] = self.direction[1]/self.magnitude*self.speed
    def update(self, screen):
        self.life-=1
        self.dim = int(255*(float(self.life)/self.maxlife))
        
        self.v_pos = [self.v_pos[0] + self.direction[0], self.v_pos[1] + self.direction[1]]

        self.rect = self.rect.move(int(self.v_pos[0])-self.rect.center[0],int(self.v_pos[1])-self.rect.center[1])
                
        self.color = random.randint(0,3)
        if self.color==0:
            self.image.fill([self.dim,self.dim,self.dim])
        elif self.color==1:
            self.image.fill([self.dim,0,0])
        elif self.color==2:
            self.image.fill([0,self.dim,0])
        else:
            self.image.fill([0,0,self.dim])

        screen.blit(self.image, self.rect)



class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.life=100

        self.particals = []
        for a in xrange(50):
            self.particals.append(Partical(pos, self.life))


    def update(self, screen):

        for partical in self.particals:
            partical.update(screen)
        
        self.life-=1

class Star(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.Surface([1,1])
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move([random.randint(0,size[0]),random.randint(0,size[1])])

        self.size = size

        self.move = random.randint(5,25)
        self.current = self.move


    def update(self, screen):
        self.current-=1
        if self.current==0:
            self.current = self.move
            self.rect = self.rect.move(-1,0)
        
        self.brightness = random.randint(100-self.move*4,255-self.move*4)
        self.image.fill([self.brightness,self.brightness,self.brightness])
        
        
        if self.rect.right<0:
            self.rect = self.rect.move(self.size[0],0)

        screen.blit(self.image, self.rect)
