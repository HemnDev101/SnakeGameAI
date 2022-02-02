import pygame
import time
import random
from pygame.math import Vector2

pygame.init() # Initialize all pygame modules

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

grass_color = (167,209,61)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height)) 
#A method that initialize surface witch is a pygameobject for representing images

pygame.display.set_caption('Snake Game') # Setting caption for the frame

clock = pygame.time.Clock() #This function is used to create a clock object which can be used to keep track of time

snake_block = 10
snake_speed = 15
score_font = pygame.font.SysFont("comicsansms", 25)


game_over = False
Max_score = dis_width*dis_height/25
x1=120
y1=80
x2=10
y2=0

arry = [0, 0,'right']
snake_List = [Vector2(110,80),Vector2(100,80),Vector2(90,80),Vector2(80,80)]
Length_of_snake = 4

foodx = round(random.randrange( 10, dis_width - snake_block-10) /10 ) * 10.0 #Generate position for the food (x,y)
foody = round(random.randrange(10, dis_height - snake_block-10) /10 ) * 10.0


apple = pygame.image.load_basic('apple.bmp')
head_up = pygame.image.load_basic('head_up.bmp')
head_down = pygame.image.load_basic('head_down.bmp')
head_left = pygame.image.load_basic('head_left.bmp')
head_right = pygame.image.load_basic('head_right.bmp')

tail_up = pygame.image.load_basic('tail_up.bmp')
tail_down = pygame.image.load_basic('tail_down.bmp')
tail_left = pygame.image.load_basic('tail_left.bmp')
tail_right = pygame.image.load_basic('tail_right.bmp')

body_bl = pygame.image.load_basic('body_bl.bmp')
body_br = pygame.image.load_basic('body_br.bmp')
body_tl = pygame.image.load_basic('body_tl.bmp')
body_tr = pygame.image.load_basic('body_tr.bmp')

body_horizontal = pygame.image.load_basic('body_horizontal.bmp')
body_vertical = pygame.image.load_basic('body_vertical.bmp')

background=pygame.image.load_basic('background.bmp')
def our_snake(snake_block, snake_list):
    
    snake_tail = update_tail_graphics(snake_list)
    snake_head = update_head_graphics(snake_list)
    
    
    for index in range(len(snake_list)):
        x_pos = int(snake_list[index].x)
        y_pos = int(snake_list[index].y)
        block_rect = pygame.Rect(x_pos, y_pos, snake_block, snake_block)
        
        if index == 0:
            dis.blit(snake_head, block_rect)
            
        elif index == len(snake_list)-1:
            dis.blit(snake_tail, block_rect)
        

        
        else:
        
            previous_block = snake_list[index - 1] - snake_list[index]
            previous_block2 = snake_list[index - 2] - snake_list[index]
          # next_block2 = snake_list[index + 2] - snake_list[index]
            next_block = snake_list[index + 1] - snake_list[index]
            
            
            if previous_block2.x == next_block.x:
                if index == 1:
                    continue
       
                dis.blit(body_vertical,block_rect)
            elif previous_block2.y == next_block.y:
                if index == 1:
                    continue
               
                
                dis.blit(body_horizontal,block_rect)
            else:
               
                if previous_block.x == -10 and next_block.y == -10 or previous_block.y == -10 and next_block.x == -10:
                    dis.blit(body_tl,block_rect)
                elif previous_block.x == -10 and next_block.y == 10 or previous_block.y == 10 and next_block.x == -10:
                    dis.blit(body_bl,block_rect)
                elif previous_block.x == 10 and next_block.y == -10 or previous_block.y == -10 and next_block.x == 10:
                    dis.blit(body_tr,block_rect)
                elif previous_block.x == 10 and next_block.y == 10 or previous_block.y == 10 and next_block.x == 10:
                    dis.blit(body_br,block_rect)

                    
def update_head_graphics(snake_list):
    global snake_head
    head_relation = snake_list[1] - snake_list[0]
    if head_relation == Vector2(10,0): snake_head = head_left
    elif head_relation == Vector2(-10,0): snake_head = head_right
    elif head_relation == Vector2(0,10): snake_head = head_up
    else: snake_head = head_down
    #head_relation == Vector2(0,-10)
    return snake_head

def update_tail_graphics(snake_list):
    global snake_tail
    tail_relation = snake_list[-2] - snake_list[-1]
    if tail_relation == Vector2(10,0): snake_tail = tail_left
    elif tail_relation == Vector2(-10,0): snake_tail = tail_right
    elif tail_relation == Vector2(0,10): snake_tail = tail_up
    else: snake_tail = tail_down
    #tail_relation == Vector2(0,-10)
    return snake_tail

def Your_score(score): # Displaying the score
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [10, 560])



def draw_grass(dis):
		for row in range(dis_width):
			if row % 2 == 0: 
				for col in range(dis_height):
					if col % 2 == 0:
						grass_rect = pygame.Rect(col * snake_block,row * snake_block,snake_block,snake_block)
						pygame.draw.rect(dis,grass_color,grass_rect)
			else:
				for col in range(dis_height):
					if col % 2 != 0:
						grass_rect = pygame.Rect(col * snake_block,row * snake_block,snake_block,snake_block)
						pygame.draw.rect(dis,grass_color,grass_rect)




def calculate(x, y, fx, fy, directions): 
    #Moving the snake toward the food
    
    global arr
    
    if x < fx:
        if directions == 'left':
            arr = [0, 10,'up']
        elif directions == 'right':
            arr = [10, 0,'right']
        elif directions == 'up':
            arr = [10, 0,'right']
        elif directions == 'down':
            arr = [10, 0,'right']
        return arr

    if x > fx:
        if directions == 'left':
            arr = [-10, 0,'left']
        elif directions == 'right':
            arr = [0, 10,'up']
        elif directions == 'up':
            arr = [-10, 0,'left']
        elif directions == 'down':
            arr = [-10, 0,'left']
        return arr

    if y < fy:
        if directions == 'left':
            arr = [0, 10,'up']
        elif directions == 'right':
            arr = [0, 10,'up']
        elif directions == 'up':
            arr = [0, 10,'up']
        elif directions == 'down':
            arr = [10, 0,'right']
        return arr

    if y > fy:
        if directions == 'left':
            arr = [0, -10,'down']
        elif directions == 'right':
            arr = [0, -10,'down']
        elif directions == 'up':
            arr = [10, 0,'right']
        elif directions == 'down':
            arr = [0, -10,'down']
        return arr

def message(msg, color):
    mesg = score_font.render(msg, True, color)
    dis.blit(mesg, [100, 50])
game_close=True
Ai_play=False
User_play=True
while not game_over: #Main loop
                                        
    
    while game_close == True:
        dis.blit(background,(0,0))
        message("Enter 1 for the user to play or 2 to let the Ai play", white)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    game_close=True
                    game_over = True
                if event.key == pygame.K_1:
                    Ai_play=False
                    User_play=True
                    game_close = False
                if event.key == pygame.K_2:
                        Ai_play = True
                        User_play=False
                        game_close = False
            
                
     
     
         
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    #Cllaing an event handler to see if wanna close the window
            game_over = True
        if User_play == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x2 = -10
                    y2 = 0
                elif event.key == pygame.K_RIGHT:
                    x2 = 10
                    y2 = 0
                elif event.key == pygame.K_UP:
                    y2 = -10
                    x2 = 0
                elif event.key == pygame.K_DOWN:
                    y2 = 10
                    x2 = 0
    
    
            

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True #Making boundries for the snake
    
    if User_play==True:
        x1+=x2
        y1+=y2

    if Ai_play == True:
        arry = calculate(x1, y1, foodx,foody,arry[2])
        x1 += arry[0]
        y1 += arry[1]

    dis.fill(green)     #Coloring the frame
    
    #draw_grass(dis)     #Drawing grass for our game
    
    dis.blit(apple, [foodx-5, foody-5]) #Drwing the food
    snake_Head = Vector2(x1,y1)
          
    snake_List.insert( 0 ,snake_Head) #Adding the new position point to the list


    if len(snake_List) > Length_of_snake:
            del snake_List[-1]
            
    for x in snake_List[1:]: #Ending the game if the snake cross it's body
        if x == snake_Head:
            game_over = True

       
    Your_score(Length_of_snake - 1)  
    our_snake(snake_block, snake_List)
    
    pygame.display.update() #updating the entire frame(Rendering)
    
    
            
    if x1 == foodx and y1 == foody: #Check if the snake reaches the food
        
        Length_of_snake += 1 #Increamente the length
        
        foodx = round(random.randrange(   #Generate new food position
            10, dis_width - snake_block-10) / 10.0) * 10.0
        foody = round(random.randrange(
            10, dis_height - snake_block-10) / 10.0) * 10.0
    
    if Length_of_snake==Max_score:
        game_over = True
        
    clock.tick(snake_speed)  #Limiting the games runtime speed to 10 fps whiches same as snake speed


pygame.quit() # Uninitialize all pygame modules
quit()        #Used to exit a python program