from os import remove
import random
import time







# def dead_state(width,height):
#     board = [[0 for i in range(width)] for j in range(height)]
#     return board

# def random_state(width,height):
#     state = dead_state(width,height)

#     for i in range(len(state)):
#         for j in range(len(state[i])):
#             # randomizing the values of state dead or alive 
#             random_number = random.random()
#             if(random_number>=0.5):
#                 cell_state = 0
#             else:
#                 cell_state = 1
#             # assigning random value 0 or 1 to state 
#             state[i][j] = cell_state

#     next_state(state)
#     # for i in range(len(state)):
#     #     print(state[i])


def render(function):     
    # to print call this function
    # b_state = random_state(width,height)
    b_state = [row[:] for row in function]
    for i in range(len(b_state)):
        for j in range(len(b_state[i])):
            if(b_state[i][j]):
                b_state[i][j] = " "
            else:
                b_state[i][j] = "#"
    # print("initially")
    # printing the board             
    print("-"*(len(b_state)+2))
    for i in range(len(b_state)):
        # print(*b_state[i],sep='')
        print('|',end='')
        for j in range(len(b_state[i])):
            print(b_state[i][j],end='')
        print('',end=''),print('|')      
    print("-"*(len(b_state)+2))    

    # next_state(width,height)
        



# for the cells within boundaries 
# i will range from 1 to len(state)-1
# j in range from 1 to len(state[i])-1
# then for every state[i][j]: 
# if the cell is alive that is 1:
#   count the no. of alive neighbours
#   if count<=1 then change state[i][j]=0
#   elif 2<= count <=3 then state[i][j]=1 or continue
#   elif count>=3 then change state[i][j]=0
#
# else the cell is dead that is 0:
#   count the no. of alive neighbours
#   if count=3 then state[i][j]=1
#   

def next_state(function):
    previous = [row[:] for row in function]
    # previous = random_state(len(function[0]),len(function))  #(width,height)
    
    # copying the previous to make the next board        
    new_state = [row[:] for row in previous]
    # to check the next state of a cell
    for i in range(1,len(previous)-1):
        for j in range(1,len(previous[i])-1):
            # when previous[i][j]==1 
            if(previous[i][j]):
                count=-1                            
                for l in range(i-1,i+2):
                    for m in range(j-1,j+2):
                        if(previous[l][m]==1):
                            count+=1

                # checking conditins apllied and changing values
                if(count<=1):
                    new_state[i][j]=0
                elif(count>=2 and count<=3):
                    new_state[i][j]=1
                elif(count>3):
                    new_state[i][j]=0 

            # when previous[i][j]=0
            else:
                count=0
                
                for l in range(i-1,i+2):
                    for m in range(j-1,j+2):
                        if(previous[l][m]==1):
                            count+=1

                if(count==3):
                    new_state[i][j]=1 

    
    # we can consider the corners seperately and deal with boundary rows and columns too seperately

    # TOP LEFT CORNER
    if(previous[0][0]==1):
        count_c = 0
        if(previous[0][1]==1):
            count_c+=1
        if(previous[1][0]==1):
            count_c+=1
        if(previous[1][1]==1):
            count_c+=1

        if(count_c<=1):
            new_state[0][0]=0
        elif(count_c>=2 and count<=3):
            new_state[0][0]=1

        # print("TOP LEFT COUNT: ",count_c)    
    else:
        count_c = 0
        if(previous[0][1]==1):
            count_c+=1
        if(previous[1][0]==1):
            count_c+=1
        if(previous[1][1]==1):
            count_c+=1

        if(count_c==3):
            new_state[0][0]=1 

        # print("TOP LEFT COUNT: ",count_c) 

    # TOP RIGHT CORNER
    if(previous[0][len(previous[0])-1]==1):
        count_c = 0
        if(previous[0][len(previous[0])-2]==1):
            count_c+=1
        if(previous[1][len(previous[1])-1]==1):
            count_c+=1
        if(previous[1][len(previous[1])-2]==1):
            count_c+=1

        if(count_c<=1):
            new_state[0][len(previous[0])-1]=0
        elif(count_c>=2 and count<=3):
            new_state[0][len(previous[0])-1]=1

        # print("TOP RIGHT COUNT: ",count_c) 

    else:
        count_c = 0
        if(previous[0][len(previous[0])-2]==1):
            count_c+=1
        if(previous[1][len(previous[1])-1]==1):
            count_c+=1
        if(previous[1][len(previous[1])-2]==1):
            count_c+=1

        if(count_c==3):
            new_state[0][len(previous[0])-1]=1
    
        # print("TOP RIGHT COUNT: ",count_c) 

    # BOTTOM LEFT CORNER
    if(previous[len(previous)-1][0]==1):
        count_c = 0
        if(previous[len(previous)-2][0]==1):
            count_c+=1
        if(previous[len(previous)-1][1]==1):
            count_c+=1
        if(previous[len(previous)-2][1]==1):
            count_c+=1

        if(count_c<=1):
            new_state[len(previous)-1][0]=0
        elif(count_c>=2 and count<=3):
            new_state[len(previous)-1][0]=1

        # print("BOTTOM LEFT COUNT: ",count_c) 

    else:
        count_c = 0
        if(previous[len(previous)-2][0]==1):
            count_c+=1
        if(previous[len(previous)-1][1]==1):
            count_c+=1
        if(previous[len(previous)-2][1]==1):
            count_c+=1

        if(count_c==3):
            new_state[len(previous)-1][0]=1
    
        # print("BOTTOM LEFT COUNT: ",count_c) 


    # BOTTOM RIGHT CORNER

    if(previous[len(previous)-1][len(previous[0])-1]==1):
        count_c = 0
        if(previous[len(previous)-2][len(previous[0])-1]==1):
            count_c+=1
        if(previous[len(previous)-1][len(previous[0])-2]==1):
            count_c+=1
        if(previous[len(previous)-2][len(previous[0])-2]==1):
            count_c+=1

        if(count_c<=1):
            new_state[len(previous)-1][len(previous[0])-1]=0
        elif(count_c>=2 and count<=3):
            new_state[len(previous)-1][len(previous[0])-1]=1

        # print("BOTTOM RIGHT COUNT: ",count_c) 

    else:
        count_c = 0
        if(previous[len(previous)-2][len(previous[0])-1]==1):
            count_c+=1
        if(previous[len(previous)-1][len(previous[0])-2]==1):
            count_c+=1
        if(previous[len(previous)-2][len(previous[0])-2]==1):
            count_c+=1

        if(count_c==3):
            new_state[len(previous)-1][len(previous[0])-1]=1
    
        # print("BOTTOM RIGHT COUNT: ",count_c)    

    # ROW WITH ZERO INDEX
    for i in range(1,len(previous[0])-1):
        if(previous[0][i]):
            count_r = -1
            for l in range(0,2):
                for m in range(i-1,i+2):
                    if(previous[l][m]==1):
                        count_r+=1

            if(count_r<=1):
                new_state[0][i]=0
            elif(count_r>=2 and count_r<=3):
                new_state[0][i]=1
            elif(count_r>3):
                new_state[0][i]=0

        else:
            count_r = 0
            for l in range(0,2):
                for m in range(i-1,i+2):
                    if(previous[l][m]==1):
                        count_r+=1

            if(count_r==3):
                new_state[0][i]=1                    

    # ROW with INDEX len(previous)-1

    for i in range(1,len(previous[0])-1):
        if(previous[len(previous)-1][i]):
            count_r = -1
            for l in range(len(previous)-2,len(previous)):
                for m in range(i-1,i+2):
                    if(previous[l][m]==1):
                        count_r+=1

            if(count_r<=1):
                new_state[len(previous)-1][i]=0
            elif(count_r>=2 and count_r<=3):
                new_state[len(previous)-1][i]=1
            elif(count_r>3):
                new_state[len(previous)-1][i]=0

        else:
            count_r = 0
            for l in range(len(previous)-2,len(previous)):
                for m in range(i-1,i+2):
                    if(previous[l][m]==1):
                        count_r+=1

            if(count_r==3):
                new_state[len(previous)-1][i]=1

    # LEFT MOST COLUMN
    for i in range(1,len(previous)-1):
        if(previous[i][0]):
            count_r=-1
            for l in range(0,2):
                for m in range(i-1,i+2):
                    if(previous[m][l]==1):
                        count_r+=1
        
            if(count_r<=1):
                new_state[i][0]=0
            elif(count_r>=2 and count_r<=3):
                new_state[i][0]=1
            elif(count_r>3):
                new_state[i][0]=0
        else:
            count_r=0
            for l in range(0,2):
                for m in range(i-1,i+2):
                    if(previous[m][l]==1):
                        count_r+=1

            if(count_r==3):
                new_state[i][0]=1


    # Right Most column
    for i in range(1,len(previous)-1):
        if(previous[i][len(previous)-1]):
            count_r=-1
            for l in range(len(previous)-2,len(previous)):
                for m in range(i-1,i+2):
                    if(previous[m][l]==1):
                        count_r+=1
        
            if(count_r<=1):
                new_state[i][len(previous)-1]=0
            elif(count_r>=2 and count_r<=3):
                new_state[i][len(previous)-1]=1
            elif(count_r>3):
                new_state[i][len(previous)-1]=0
        else:
            count_r=0
            for l in range(len(previous)-2,len(previous)):
                for m in range(i-1,i+2):
                    if(previous[m][l]==1):
                        count_r+=1
        
            if(count_r==3):
                new_state[i][len(previous)-1]=1                           
 



    render(previous)
    time.sleep(0.1)
    render(new_state)
    time.sleep(0.1)
    next_state(new_state)
    




# random_state(90,90)
handle = open("toad.txt")
words = list()

for line in handle:
    for digit in range(len(line)):
        if (line[digit:digit+1]=="\n"):
            continue
        words.append(int(line[digit:digit+1]))
for ele in words:        
    if(ele=="\n"):
        words.remove(ele)

print(words)
print(len(words))
array = [words[r*6:(r+1)*6] for r in range(0,6)]
print(array)
next_state(array)

