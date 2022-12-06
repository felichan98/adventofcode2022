
id_exercise = 2

f = open('input.txt', 'r')

content = f.read()

list_pairs = []

list_pairs= (content.split("\n"))

## foreach [n1-n2] in a pair, fill the missing numbers and intersect to check the condition

intestections_count = 0

for i in list_pairs:
    first_elfo, second_elfo = i.split(',')
    # making them integers!!
    first_elfo= list(map(int, first_elfo.split('-')))
    second_elfo= list(map(int, second_elfo.split('-')))
    
    #unsqueeeezing
    
    for j in range(first_elfo[0], first_elfo[1] + 1):
        if(j==first_elfo[0]): first_elfo.clear()
        first_elfo.append(j)
        
    for j in range(second_elfo[0], second_elfo[1] + 1):
        if(j==second_elfo[0]): second_elfo.clear()
        second_elfo.append(j)
        
    intersect = list(set(first_elfo) & set(second_elfo))
    intersect.sort()
    
    #FIRST PART: one fully inside all the other one
    if(id_exercise==1):    
        if((intersect == first_elfo) or (intersect == second_elfo)): intestections_count += 1
        
    #SECOND PART: all kind of intersections
    if(id_exercise==2):    
        if(len(intersect) != 0): intestections_count += 1

print(intestections_count)



    
    
