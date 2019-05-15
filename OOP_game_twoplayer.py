'''
Created on 29. nov. 2018

@author: silas
'''
'''
Created on 5. dec. 2018

@author: silas
'''
'''
Created on 29. nov. 2018

@author: silas
'''
#importing pygame and calling __init__() for pygame and fonts to make them work
import pygame
pygame.init()
pygame.font.init()

#creating the font type and size and making game over text from it
myfont = pygame.font.SysFont('Comic Sans MS', 60)
gameover_text = myfont.render('Game over', False, (255, 255, 255))
restartfont = pygame.font.SysFont('Comic Sans MS', 20)
restart_text = restartfont.render("PRESS 'SPACE' TO RESTART", False, (255, 255, 255))

#creating clock variable to call it in the mainloop more easily
clock = pygame.time.Clock()

#setting up the screen
def screen_setup():
    global screen_x
    screen_x = 1000
    global screen_y
    screen_y = 500
    global win    
    win = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption('Chase Game')
screen_setup()

#making a class for the player, enemies and enemy-objects
class objecttemplate():
    def __init__(self,width,height,x,y,vel,color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vel = vel
        self.color = color
        
#making the player
def makeplayer():
    global player
    player = objecttemplate(height=20,width=20,x=500,y=250,vel=8,color=(0,204,0))


#making the enemy and enemy-objects
def makeenemies():
    global enemy
    enemy = objecttemplate(height=60,width=60,x=50,y=250,vel=6,color=(255,0,0))
    global object1
    object1 = objecttemplate(height=10,width=400,x=0-200,y=230,vel=4,color=(255,0,0))
    global object2
    object2 = objecttemplate(height=400,width=10,x=480,y=0-200,vel=2,color=(255,0,0))
    global object3
    object3 = objecttemplate(height=10,width=400,x=screen_x,y=310,vel=4,color=(255,0,0))
    global object4
    object4 = objecttemplate(height=400,width=10,x=560,y=screen_y,vel=2,color=(255,0,0))

#this draws the enemies and turns them into rects
def drawenemies():
    enemy.rect = pygame.draw.rect(win, enemy.color, (enemy.x,enemy.y,enemy.width,enemy.height))
    object1.rect = pygame.draw.rect(win, object1.color, (object1.x,object1.y,object1.width,object1.height))
    object2.rect = pygame.draw.rect(win, object2.color, (object2.x,object2.y,object2.width,object2.height))
    object3.rect = pygame.draw.rect(win, object3.color, (object3.x,object3.y,object3.width,object3.height))
    object4.rect = pygame.draw.rect(win, object4.color, (object4.x,object4.y,object4.width,object4.height))

#this draws the player and turns him into a rect
def drawplayer():
    player.rect = pygame.draw.rect(win, player.color, (player.x,player.y,player.width,player.height))

#function that decides how the enemies will move
def enemymovement():
    #object to top to bottom
    if object2.y > screen_y:
        object2.y = 0-220
        object2.x = player.x-20
    object2.y += (object2.vel * 1)
    #object1 left to right
    if object1.x > screen_x:
        object1.x = 0-object1.width-20
        object1.y = player.y-20
    object1.x += (object1.vel * 1)
    #object3 right to left    
    if object3.x < 0-object3.width:
        object3.x = screen_x+20
        object3.y = player.y+player.height+10
    object3.x -= (object3.vel * 1)
    #object4 bottom to top
    if object4.y < 0-object4.height:
        object4.y = screen_y+20
        object4.x = player.x+player.width+10
    object4.y -= (object4.vel * 1)
    #the chasing enemy
#     if enemy.x <= player.x+(player.width/2)-(enemy.width/2):
#         enemy.x += enemy.vel
#     if enemy.x > screen_x:
#         enemy.x = 0-100
#     if enemy.x > player.x+(player.width/2)-(enemy.width/2):
#         enemy.x -= enemy.vel
#     if enemy.y < player.y+(player.height/2)-(enemy.height/2):
#         enemy.y += enemy.vel
#     if enemy.y > player.y+(player.height/2)-(enemy.height/2):
#         enemy.y -= enemy.vel
        
#this decides how the player moves     
def playermovement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player.vel
    if keys[pygame.K_RIGHT] and player.x < (screen_x-player.width):
        player.x += player.vel
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= player.vel
    if keys[pygame.K_DOWN] and player.y < (screen_y-player.height):
        player.y += player.vel
        
    if keys[pygame.K_a] and enemy.x > 0:
        enemy.x -= enemy.vel
    if keys[pygame.K_d] and enemy.x < (screen_x-enemy.width):
        enemy.x += enemy.vel
    if keys[pygame.K_w] and enemy.y > 0:
        enemy.y -= enemy.vel
    if keys[pygame.K_s] and enemy.y < (screen_y-enemy.height):
        enemy.y += enemy.vel

#this detecs if the player collides with any other rects in the game
def collision_detection():
    if player.rect.colliderect(enemy.rect) or player.rect.colliderect(object1.rect) or player.rect.colliderect(object2.rect) or player.rect.colliderect(object3.rect) or player.rect.colliderect(object4.rect):
        return True

#draws on the surface aka. window and updates it everytime it's called
def drawwindow(score_text):
    win.fill((0,0,0))
    drawenemies()
    drawplayer()
    win.blit(score_text,(900,0))
    pygame.display.update()

#main function that starts the game and sets up important stuff
def main():
    #loading and start playing the game tune
    pygame.mixer.music.load('Humble [8 Bit Tribute to Kendrick Lamar] - 8 Bit Universe.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(loops=-1, start=0_0)
    humbleplaying = True
    #creating a user event to update the score and setting a timer for it
    score_event = pygame.USEREVENT + 1
    pygame.time.set_timer(score_event, 1000)
    
    #setting/resetting the score to 0 and creating/recreating the score_text for it
    score = 0
    score_text = myfont.render(str(score), False, (255, 255, 255))
    
    #calling some functions so you're able to restart the game
    makeplayer()
    makeenemies()
    drawwindow(score_text)
    
    #MAINLOOP
    running = True
    while running:
        clock.tick(55)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            if event.type == score_event:
                score += 1
                score_text = myfont.render(str(score), False, (255, 255, 255))
        #This is where everything will run--
        playermovement()
        enemymovement()
        
        #if this is true then game over screen will appear
        if collision_detection():
            if humbleplaying == True:
                pygame.mixer.music.fadeout(500)
            win.blit(gameover_text,(350,200))
            pygame.display.update()
            #starts game over tune and displays some text
            if humbleplaying == True:
                pygame.time.wait(1000)
                pygame.mixer.music.load('Falling Down [8 Bit Tribute to Lil Peep & XXXTENTACION] - 8 Bit Universe.mp3')
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(loops=-1, start=0_0)
                humbleplaying = False
                win.blit(restart_text,(355,450))
            #lets you restart the game by pressing space
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                main()
        #calls drawwindow if no collision was detected 
        else:
            drawwindow(score_text)   
    pygame.quit()
main()