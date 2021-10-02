import pyglet
from pyglet import image
from pyglet.window import mouse, Window, key

window=Window(496, 526, resizable=True, caption='Eight Queens')
board = pyglet.resource.image('resources/board.gif')
qimage=image.load('resources/queen.png')          #Image for the queen
boximage=image.load('resources/black box.png')    #image which bolds each box
errorimage=image.load('resources/red.jpg')        #error detection of queen
previmage=image.load('resources/green.jpg')        #highlight theprevious position until new one is placed
win = image.load('resources/win.jpeg')                   #Image for winning window
winning = Window(450, 296, resizable=False, caption='You Win!!')   #winning window
winning.set_visible(False)
lose = image.load('resources/lose.jpeg')         #image for losing window
losing = Window(458,377, resizable=False, caption='You Lose!!')       #losing window
losing.set_visible(False)
close=image.load('resources/close.png')     #Load image for close button
clear=image.load('resources/clear.png')     #Load image for clear button
hellp=image.load('resources/help.png')      #Load image for help button
music=image.load('resources/play.jpg')      #Load image for music button
pause=image.load('resources/pause.jpg')     #Load image for music when paused 
rekt=image.load('resources/option.png')     #Load image for button highlight over close and clear
smol_rekt=image.load('resources/choose.png')        #Load image for button highlight over instructions and help
instructions=image.load('resources/instruction.jpeg')   #Load the instructions image
ins=pyglet.sprite.Sprite(instructions,270,200)  #Converting instructions loaded image to sprite
ins.visible=False #keeping image invisible for now
smol1=pyglet.sprite.Sprite(smol_rekt,209,498)   #Converting button highlight loaded image to sprite
smol1.visible=False #keeping image invisible for now
smol2=pyglet.sprite.Sprite(smol_rekt,261,498)
smol2.visible=False #keeping image invisible for now
rekt1=pyglet.sprite.Sprite(rekt,341,500)
rekt1.visible=False #keeping image invisible for now
rekt2=pyglet.sprite.Sprite(rekt,93,500)
rekt2.visible=False #keeping image invisible for now
close=pyglet.sprite.Sprite(close,341,500)
close.visible=True  #image visible because button in game
clear=pyglet.sprite.Sprite(clear,93,500)
clear.visible=True  #image visible because button in game
hellp=pyglet.sprite.Sprite(hellp,261,498)
hellp.visible=True  #image visible because button in game
music=pyglet.sprite.Sprite(music,209,498)
music.visible=True  #image visible because button in game
pause=pyglet.sprite.Sprite(pause,209,498)
pause.visible=False     #keeping image invisible for now
#Music play for the whole game
game_music = pyglet.media.load('resources/Music.mp3')
# keep playing for as long as the app is running by creating a looper
looper = pyglet.media.SourceGroup(game_music.audio_format, None)
looper.loop = True
looper.queue(game_music)
# create a player and queue the song
player = pyglet.media.Player()
player.queue(looper)
player.play()


# Get an instance of current platform
platform = pyglet.window.get_platform()
# Get an instance of current display
display = platform.get_default_display()
# Get an instance of current screen
screen = display.get_default_screen()
# Make sure that game approximately is placed as center of screen
# This will adjust for different resolution. Relative positioning
# Using resolution to center game window
#Game window
window.set_location(screen.width // 2 - 250, screen.height // 2 - 240)
myicon = pyglet.image.load('resources/board.gif')  # image for icon of game window
window.set_icon(myicon)  # Setting icon for game window
#Winning window
winning.set_location(screen.width // 2 - 225, screen.height // 2 - 145)
myicon = pyglet.image.load('resources/win.jpeg')
winning.set_icon(myicon)
#Losing window
losing.set_location(screen.width // 2 - 225, screen.height // 2 - 175)
myicon = pyglet.image.load('resources/lose.jpeg')
losing.set_icon(myicon)

#all queens, boxes indicating something are represented in a form of matrix
#the last list of the matrix is the top most row, and the leftmost column is the first element of each row
qsprite=[[0 for m in range(8)] for n in range(8)]
kalay_dabbay=[[0 for m in range(8)] for n in range(8)]
checker=[[0 for m in range(8)] for n in range(8)]  
masla=[[0 for m in range(8)] for n in range(8)]
wrongPlacement = [[0 for m in range(8)] for n in range(8)]
prev_pos=[[0 for m in range(8)] for n in range(8)]
prev_mat=[[0 for m in range(8)] for n in range(8)]

#placing the queens and boxes
for i in range(8):
    for j in range(8):
        qsprite[i][j]=pyglet.sprite.Sprite(qimage,j*62,i*62)
        qsprite[i][j].visible=False
        kalay_dabbay[i][j]=pyglet.sprite.Sprite(boximage,(j*62)-26,(i*62)-28)
        kalay_dabbay[i][j].visible=False
        masla[i][j]=pyglet.sprite.Sprite(errorimage,j*62,i*62)
        masla[i][j].visible=False
        prev_pos[i][j]=pyglet.sprite.Sprite(previmage,j*62,i*62)
        prev_pos[i][j].visible=False

#a variable to make sure only 8 queens are placedsrif8=0
srif8 = 0
      
@window.event
def on_draw():  #This is a built-in pyglet function that draws everything on the window but we could choose for items to be kept visible or invisible
    window.clear()
    clear.draw()
    close.draw()
    hellp.draw()
    music.draw()
    pause.draw()
    rekt1.draw()
    rekt2.draw()
    smol1.draw()
    smol2.draw()
    board.blit(0,0)
    ins.draw()
    for i in range(8):
        for j in range(8):
            masla[i][j].draw()
            prev_pos[i][j].draw()
            qsprite[i][j].draw()
            kalay_dabbay[i][j].draw()
@winning.event   #when all queens are placed in correct positions
def on_draw():
    winning.clear()
    win.blit(0,0)
@losing.event   #when all queens are placed in correct positions except last one
def on_draw():
    losing.clear()
    lose.blit(0,0)

@window.event
def on_mouse_release(x, y, button, modifiers):  #This is a built-in pyglet function that takes input from the touchpad or mouse buttons and functions according to the code afterwards
    global srif8
    if button==mouse.LEFT:  #if the button on mouse pressed is the left one
        if (x<=119 and x>=93) and y>=500 and y<=526: #if the music button is pressed to turn music off
            player.pause()
        if (x<=235 and x>=209) and y>=498 and y<=525:   #if the music button is prssed turn the button green so user knows the music is paused
            if pause.visible==True:
                pause.visible=False
                player.play()    #play the music
            else:
                pause.visible=True
                player.pause()          #pause the music

        #clears the screen when clear button is pressed            
        if (x<=156 and x>=93) and (y>=500 and y<=525):     
            srif8=0
            for i in range(8):
                for j in range(8):
                    qsprite[i][j].visible=False
                    wrongPlacement[i][j] = 0 
                    masla[i][j].visible = False
                    checker[i][j] = 0
                    prev_pos[i][j].visible = False
        if (x<=404 and x>=341) and y>=500 and y<=525: #if close button clicked
            window.close()
            player.pause()
        elif (x<=287 and x>=261) and (y>=498 and y<=524): #if ins button clicked
            if ins.visible==True:
                ins.visible=False
            else:
                ins.visible=True
                    
        # looping over matrics that contain the queens, error boxes, previous position boxes and displaying the desire changes        
        for i in range(8):
            for j in range(8):
                if (x>=j*62 and x<=(j*62)+62) and (y>=i*62 and y<=(i*62)+62):
                       #if the queen was previously visible then do the following
                        if qsprite[i][j].visible==True:
                            srif8-=1    
                            qsprite[i][j].visible=False
                            wrongPlacement[i][j] = 0       #a matric that has ones in places where queens are placed and 0 where no queens
                            checker[i][j] = 0
                            prev_pos[i][j].visible = True      #making that place green where the queen was previously placed so as to not forget the position
                            prev_mat[i][j] = 1
                        else:
                        #if queen is not placed yet or is invisible, do the following
                            ins.visible=False
                            if srif8<8:
                                srif8+=1
                                qsprite[i][j].visible=True
                                checker[i][j] = 1
                                wrongPlacement[i][j] = 1
                                #where ever there is a one in the prev_mat matric meaning thats the previous position, now that the queen has been placed player doesnt need to remeber that position
                                for i in range(8):
                                    for j in range(8):
                                        if prev_mat[i][j]==1:
                                            prev_pos[i][j].visible = False
                                            prev_mat[i][j] = 0
                                #if more than one queen is placed, checking if theyhave any problem or not
                                if srif8 > 1:
                                    checkMasla(wrongPlacement)
                                #when 8 queens have been placed telling whether you won or not
                                if srif8 == 8:
                                    checkWin(checker)
                #removing the error sign and then checking to see if its any more problems with the other queens
                masla[i][j].visible=False
                checkMasla(wrongPlacement)
                    
@window.event
def on_mouse_motion(x, y, dx, dy):
    if (x<=404 and x>=341) and y>=500 and y<=525:  #close
        rekt1.visible=True
    elif (x<=156 and x>=93) and y>=500 and y<=525: #clear
        rekt2.visible=True
    elif (x<=235 and x>=209) and y>=498 and y<=524: #highlighter over music button
        smol1.visible=True
    elif (x<=287 and x>=261) and y>=498 and y<=524: #highlighter over instruction button
        smol2.visible=True    
    else:
        rekt1.visible=False     #keeping all other  highlighters invisible
        rekt2.visible=False
        smol1.visible=False
        smol2.visible=False
    #when you move the cursor, black boxes tell you where the you'll place the queen
    for i in range(8):
        for j in range(8):
            if ins.visible==False:
                if (x>=j*62 and x<=(j*62)+62) and (y>=i*62 and y<=(i*62)+62):
                    kalay_dabbay[i][j].visible=True
                else:
                    kalay_dabbay[i][j].visible=False

#the function that checks if any queens placed attack each other or not and make them red accordingly               
def checkMasla(matrix):
    #checking for queens in the same row
    for i in matrix:
        if i.count(1)>1:
            for j in range(8):
                if i[j] == 1:
                    masla[matrix.index(i)][j].visible = True
    #queens in the same column
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 1:
                for k in range(i+1, 8):
                    if matrix[k][j] == 1:
                        masla[k][j].visible = True
                        masla[i][j].visible = True
    #queens in the diagonal
    pos = [["70", "71", "72", "73", "74", "75", "76", "77"],
           ["60", "61", "62", "63", "64", "65", "66", "67"],
           ["50", "51", "52", "53", "54", "55", "56", "57"],
           ["40", "41", "42", "43", "44", "45", "46", "47"],
           ["30", "31", "32", "33", "34", "35", "36", "37"],
           ["20", "21", "22", "23", "24", "25", "26", "27"],
           ["10", "11", "12", "13", "14", '15', "16", "17"],
           ["00", "01", "02", "03", "04", "05", "06", "07"]]    #positions of queens in reverse order
    pos.reverse()
    max_col = len(matrix)
    max_row = len(matrix[0])
    fdiag = [[] for i in range(max_col + max_row - 1)]                  #front diagonal
    bdiag = [[] for i in range(len(fdiag))]                                        #back diagonal 
    posfdiag = [[] for i in range(len(fdiag))]                          #diagonals of position
    posbdiag = [[] for i in range(len(fdiag))]
    posmin_bdiag = -max_col +1
    min_bdiag = -max_col + 1
    #finding all possible diagonals 
    for y in range(max_col):
        for x in range(max_row):
            fdiag[x+y].append(matrix[y][x])
            posfdiag[x+y].append(pos[y][x])
            bdiag[-min_bdiag+x-y].append(matrix[y][x])
            posbdiag[-min_bdiag+x-y].append(pos[y][x])
    #checking if more than one 1 in a diagonal, else they'd attack each other
    for x in fdiag:
        if x.count(1)>1:
            for y in range(len(x)):
                if x[y] == 1:
                    temp = posfdiag[fdiag.index(x)][y]
                    masla[int(temp[0])][int(temp[1])].visible = True
    for x in bdiag:
        if x.count(1)>1:
            for y in range(len(x)):
                if x[y] == 1:
                    temp = posbdiag[bdiag.index(x)][y]
                    masla[int(temp[0])][int(temp[1])].visible = True

#same conditions as the above function, just a difference in what they do if condition is fullfiled
def checkWin(matrix):
    #queens in the same row
    for i in matrix:
        if i.count(1)>1:
            losing.set_visible(True)
            window.set_visible(False)
            return
    #queens in the same column
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 1:
                for k in range(8):
                    if k!=i and matrix[k][j] == 1:
                        losing.set_visible(True)
                        window.set_visible(False)
                        return
    #queens in the diagonal
    max_col = len(matrix)
    max_row = len(matrix[0])
    fdiag = [[] for i in range(max_col + max_row - 1)]
    bdiag = [[] for i in range(len(fdiag))]
    min_bdiag = -max_col + 1
    for y in range(max_col):
        for x in range(max_row):
            fdiag[x+y].append(matrix[y][x])
            bdiag[-min_bdiag+x-y].append(matrix[y][x])
    for x in fdiag:
        if x.count(1)>1:
            losing.set_visible(True)
            player.pause()  #stops music 
            window.set_visible(False)
            return
    for x in bdiag:
        if x.count(1)>1:
            losing.set_visible(True)
            player.pause()  #stops music 
            window.set_visible(False)
            return

    winning.set_visible(True)   
    window.set_visible(False)
    player.pause()  #stops music 
    winmusic = pyglet.media.load('resources/win.wav')   #win music play when user wins
    winmusic.play()
    return
def update(dt):
    on_draw()
#window.push_handlers(pyglet.window.event.WindowEventLogger())      #will give all events running in the background
pyglet.app.run()
