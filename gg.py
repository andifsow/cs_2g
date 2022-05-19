from cmu_graphics import * 

app.background = 'darkGray'
app.stepsPerSecond = 30

###Wall
wall = Group(Rect(0,0,10,400,fill='gray'),
             Rect(390,0,20,400,fill='gray'))
###platforms 


floor = Rect(1,400,400,10,fill='black')
platform1 = Rect(10,270,200,20)
platform2 = Rect(200,170,200,20)

###movibel platforms

moplat1 = Rect(275,370,50,30)

moveplat = Group(moplat1)
###ground 
ground = Group(floor,
moveplat,
platform1,
platform2)

###



###gun 

gunhand = Rect(30,370,30,10)
gun = Group(gunhand,visible=False)

###playercharacter
player = Group()
player.add(Rect(20,360,20,40,fill='midnightBlue'))



###Wall border
def onStep():
    if(player.left < 10):
        player.left = 10
    elif(player.right > 390):
        player.right = 390
    
###gravity     
    player.centerY += player.dy
    if player.hitsShape(ground) != True:
            player.dy += player.gravity

    for platform in ground.children:
        if player.hitsShape(platform) and player.bottom < platform.top + (player.dy+7):
            player.bottom = platform.top
            player.dy = 0
        
        #if(player.hitsShape(platform.bottom) == True):
            #player.centerY = platform.centerY+10
        
        
        


###player
player.dy = 0
player.dx = 0
player.speed = 6
player.gravity = 1
player.jump = -11




###Player Movementqa


def onKeyPress(keys):
        if keys == 'space' and player.hitsShape(ground):
            player.dy = player.jump
        if(keys == 'q'):
            gun.centerX = player.centerX
            gun.centerY = player.centerY
            player.add(gun)
       
        
            
def onKeyHold(keys):
        if('d' in keys):
            player.centerX += 10
            
        elif('a' in keys):
            player.centerX -= 10
            
###Gunshot

    

















    

cmu_graphics.run()
