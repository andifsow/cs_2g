from cmu_graphics import * 
wall = Group(Rect(0,0,10,400,fill='gray'),
             Rect(390,0,20,400,fill='gray'))

app.stepPerSecond = 30

ground = Group()


###playercharacter
player = Group()
player.add(Rect(20,360,20,40,fill='midnightBlue'))
player.isOnStart = True
###platforms 


floor = Rect(0,400,400,10,fill='black')
platform1 = Rect(0,200,120,20)
platform2 = Rect(280,80,120,20)


###ground 
ground.add(floor,platform1,platform2)


player.isOnStart = True
###player
player.dy = 0
player.dx = 0
player.jump = -15
player.gravity = 1

###enemycharacters 
#enemy1 = 

Enemys = Group()











###Wall border
def onStep():
    
    if(player.left < 10):
        player.left = 10
        
    if(player.right > 390):
        player.right = 390
        
    if(player.bottom > 400):
        player.centerY = 360
    
    if(player.)
    


     
###gravity     
    player.centerY += player.dy
    if player.hitsShape(ground) != True:
            player.dy += player.gravity



###platform stuff






    for platform in ground.children:
        if player.hitsShape(platform) and player.bottom < platform.top + (player.dy+7):
            player.bottom = platform.top
            player.dy = 0
        
        if player.hitsShape(platform) and player.bottom > platform.top + (player.dy+7):
            player.top = platform.bottom
            player.dy = 2
        
        
            
 ###function

 

###Player Movementqa


def onKeyPress(keys):
        if keys == 'space' and player.hitsShape(ground):
            player.dy = player.jump
      
        if keys == 'space' and player.hitsShape(wall):
            player.dy = player.jump 
            app.stepPerSecond = 12
        
            
def onKeyHold(keys):
        if('d' in keys):
            player.centerX += 10
            
        if('a' in keys):
            player.centerX -= 10
        

            





cmu_graphics.run()
