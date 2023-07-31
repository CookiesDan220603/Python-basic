"My sample game!"

from stuff import*

#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
#   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #
   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #   #



size = (800,600)
screen = pygame.display.set_mode(size, 32)

ship = Ship(size)
shot_L = []
explosion_L = []
enemy_L  = []
enemyshot_L  = []
star_L = []

boom_s = pygame.mixer.Sound("boom.wav")
shot_s = pygame.mixer.Sound("shot.wav")
highscore_s = pygame.mixer.Sound("highscore.wav")


wait = 0
time=0

gameover = pygame.image.load("gameover.gif")

gameover_r = gameover.get_rect()
gameover_r = gameover_r.move([size[0]/2-gameover_r.width/2, size[1]/2-gameover_r.height/2])

score = 0

pygame.mouse.set_visible(False)

song = pygame.mixer.Sound("technotris.wav")
song.play(-1)

for star in xrange(100):
    star_L.append(Star(size))


################## START #################

while 1:
    time+=1
    keys = pygame.key.get_pressed()

    #restarts when you die and then press enter
    if ship==None and keys[K_RETURN]:
        song.play(-1)
        score=0
        ship=Ship(size)
        wait = 0
        time=1
        shot_L = []
        explosion_L = []
        enemy_L  = []


    #checks if the ship should be shooting
    if keys[K_SPACE] and not wait and ship!=None:
        shot_L.append(Shot(ship.rect.center, 'right'))
        shot_s.play()
        wait=True
        
    if not keys[K_SPACE]: wait = False


    #creates a new alien 
    if time%(1000000/(score+1)+1)==0:
        if random.randint(0,1)==0: enemy_L.append(Enemy2(list((size[0]+100,random.randint(50,size[1]-50))), enemyshot_L))
        elif random.randint(0,1)==0: enemy_L.append(Enemy3(list((size[0]+100,random.randint(50,size[1]-50)))))
        else:  enemy_L.append(Enemy1([size[0]+100,random.randint(50,size[1]-50)]))
    if time%100==0: enemy_L.append(Enemy1([size[0]+100,random.randint(50,size[1]-50)]))

    
    #updates the shots
    for shot in shot_L:
        shot.update(screen)
        if shot.rect[0]>size[0]:
            shot_L.remove(shot)

    #updates the explosions
    for boom in explosion_L:
        boom.update(screen)
        if boom.life<=0:
            explosion_L.remove(boom)

    #updates the enemys
    for enemy in enemy_L:
        
        enemy.update(screen, time, ship)

        #blows up the ship if it runs into a alien
        if ship!=None and enemy.rect.colliderect(ship.rect) :
            pygame.time.wait(50)
            screen.fill([255,0,0])

            info = open("highscore.spacegame","r")
            highscore = int(info.readline())

            if score-1>highscore:
                highscore_s.play()
                info = open("highscore.spacegame","w")
                info.write(str(score))
            
            explosion_L.append(Explosion(ship_pos))
            ship = None
            enemy_L.remove(enemy)
            boom_s.play()
            
        # deletes an enemy once it's left the screen
        if enemy.rect.left<-50:
            enemy_L.remove(enemy)
            if ship!=None: score-=25
            
        #checks if the alien has been shot
        for shot in shot_L:
            if shot.rect.colliderect(enemy.rect):
                explosion_L.append(Explosion(enemy.rect.center))
                boom_s.play()
                try:
                    enemy_L.remove(enemy)
                except:
                    pass
                shot_L.remove(shot)
                
                if ship!=None: score+=100

    #decides if the ship has been blow up, then updates
    if ship !=None:
        ship.update(screen,keys,size)
        ship_pos = ship.rect.topleft
    else:
        screen.blit(gameover, gameover_r)
        song.stop()

    #updates stars
    for star in star_L:
        star.update(screen)

    #updates enemy's shots, checks if it hit the ship
    for shot in enemyshot_L:
        shot.update(screen)
        if ship!= None and shot.rect.colliderect(ship.rect):
            enemyshot_L.remove(shot)
            explosion_L.append(Explosion(ship_pos))
            ship = None
            boom_s.play()
    

    #scoring system
    score = max(0, score)

    score_t = pygame.font.SysFont("arial", 20).render('score - '+str(score), False, (255,255,255))
    score_t_r = score_t.get_rect()
    score_t_r = score_t_r.move([size[0]/2-score_t_r.width/2, size[1]-size[1]/10])

    screen.blit(score_t, score_t_r)

    #updates the screen
    pygame.display.flip()
    screen.fill([0,0,0])


    # === ANTI-CRASH ===
    for event in pygame.event.get():
        if event.type == QUIT or keys[K_ESCAPE]:
            pygame.quit(); sys.exit()

        
