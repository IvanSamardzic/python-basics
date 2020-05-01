#import random and curses libs
import random 
import curses

s = curses.initscr() #initialize the screen
curses.curs_set(0) #set the cursor to zero
sh, sw = s.getmaxyx() #get the widht and height 
w = cursrs.newwin(sh, sw, 0, 0) #create new window
w.keypad(1) 
w.timeout(100) 

snk_x = sw / 4 #initial snake position
snk_y = sh / 2
#initila snake body parts, 3 parts
snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
]
#inital food position
food = [sh / 2, sw / 2]
#add the food to the screen
w.addch[food[0], food[1], curses.ACS_PI]
#snake is initially going to the right
key = curses.KEY_RIGHT

#monitor forever
while True:
    next_key = w.getch() #see what is the next key
        key = key if next_key == -1 else next_key 
        
    #set the rules for losing the game
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    
    #determine the new head
    new_head = [snake[0][0], snake[0][1]]
    
    #monitor what key is pressed
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
        
     snake.insert(0, new_head)
    
    #determine id snake eun into the food
    if snake[0] == food:
        food = None
        while food is None  
            #then create new food
            nf = [
                random.randint(1,sh - 1),
                random.randint(1,sw - 1)
            ]
            food = nf if nf not in snake else None
        #add the food to the screen
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        #erase the tail
        tail = snake.pop()
        #place ' ' where the tail earlier was
        w.addch(tail[0], tail[1], ' ')
    #add the snake head to the screen    
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)