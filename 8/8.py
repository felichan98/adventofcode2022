import numpy as np

f = open('input.txt', 'r')

content = f.read()

content = content.split('\n')

for index,i in enumerate(content):
    content[index] = list(map(int,i))
    

alberi = np.array(content)

num_visible = 0

num_visible += alberi.shape[0]*2 + alberi.shape[0]*2 -4

#alberi = alberi[1:alberi.shape[0]-1, 1:alberi.shape[1]-1]

for i in range(1,alberi.shape[0]-1):
    for j in range(1,alberi.shape[1]-1):
        updated = False
        guess_left = alberi[i,j] > alberi[i,:j]
        guess_right = alberi[i,j] > alberi[i,j+1:]
        if(guess_left.all() == True or guess_right.all() == True): 
            num_visible +=1
            updated =True
                
        guess_up = alberi[i,j] > alberi[:i,j]
        guess_down = alberi[i,j] > alberi[i+1:,j]
        if(updated == False):
            if(guess_up.all() == True or guess_down.all() == True): 
                num_visible +=1

        
    
print(num_visible)


#scenic score


pass