def left():
    ''' For Left Operation'''
    c=0
    while(c<2):
        c=c+1
        for i in range(4):
            for j in range(3):
                if(box[i,j] == box[i,j+1] or box[i,j] == 0):
                    box[i,j] = box[i,j] + box[i,j+1]
                    for k in range(j+1,3):
                        box[i,k] = box[i,k+1]
                    box[i,3] = 0
    #print(box)

def right():
    '''For Right operation'''
    c=0
    while(c < 2):
        c = c+1
        for i in range(3,-1,-1):
            for j in range(3,0,-1):
                if(box[i,j] == box[i,j-1] or box[i,j] == 0):
                    box[i,j] = box[i,j] + box[i,j-1]
                    for k in range(j-1,0,-1):
                        box[i,k] = box[i,k-1]
                    box[i,0] = 0
    #print(box)

def up():
    '''For Up operation'''
    c=0
    while(c<2):
        c=c+1
        for i in range(3):
            for j in range(4):
                if(box[i,j] == box[i+1,j] or box[i,j]==0):
                    box[i,j] = box[i,j] + box[i+1,j]
                    for k in range(i+1,3):
                        box[k,j] = box[k+1,j]
                    box[3,j] = 0
   # print(box)

def down():
    '''For down operation'''
    c=0
    while(c < 2):
        c = c+1
        for i in range(3,0,-1):
            for j in range(3,-1,-1):
                if(box[i,j] == box[i-1,j] or box[i,j] == 0):
                    box[i,j] = box[i,j] + box[i-1,j]
                    for k in range(i-1,0,-1):
                        box[k,j] = box[k-1,j]
                    box[0,j] = 0
   # print(box)

def new_num():
    '''returns 2 or 4 randomly'''
    import random
    return random.choices([2,4], weights =(.7,.3), k=1)[0]

def cell():
    '''Selects an empty cell'''
    import random
    while(1):
        m = random.randint(0,3)
        n = random.randint(0,3)
        if(box[m,n] == 0):
            box[m,n]=new_num()
            break
    #print(box)

def clear():
    import os
    from time import sleep
    _ = os.system('cls')

import numpy as np
from IPython.display import clear_output
  
box=np.matrix([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
cell()
print(box)

c=1
while(True):
    c = int(input('Enter your operation:\n2: Down; 4: Left; 6: Right; 8: Up\n0: To End The Game'))
    while(not(c in [0,2,4,6,8])):
        print("Please Enter valid operation")
        c = int(input(''))
    
    
    clear_output(wait=True)
    
    
    if(c==0):
        print('Your Score is: ',np.max(box))
        break
    if(c==2):
        down()
        cell()
    if(c==4):
        left()
        cell()
    if(c==6):
        right()
        cell()
    if(c==8):
        up()
        cell()
    print(box)
