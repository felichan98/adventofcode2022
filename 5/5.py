id_exercise = 2

f = open('input.txt', 'r')

content = f.read()

## Estraendo roba...

boxes = []
moves = []

boxes_raw, moves_raw = (content.split("\n\n"))

moves= moves_raw.split('\n')
boxes_raw = boxes_raw.split('\n')
boxes_raw.reverse()
boxes_raw.remove(boxes_raw[0])

for index, riga in enumerate(boxes_raw):
    #per impilarli senza danno nel prossimo ciclo (?)
    boxes_raw[index] = riga.replace("    ", ' *')
    
    boxes_raw[index] = boxes_raw[index].split(' ')
    

list_of_stacks = [[] for _ in range(9)]



for stack_index, row in enumerate(boxes_raw):
    for i, element in enumerate(row):
        if(element is not '*'): list_of_stacks[i].append(element)
    
    
#### decoding moves

num_of_boxes = 0
start_point = 0
end_point = 0

for j,row in enumerate(moves):  
    moves[j] = [int(i) for i in row.split() if i.isdigit()]

if id_exercise==1:

    for instruction in moves:
        num_of_boxes= instruction[0]
        start_point = instruction[1] -1
        end_point = instruction[2] -1
        for _ in range(num_of_boxes):
            list_of_stacks[end_point].append(list_of_stacks[start_point].pop()) 
            
else:
    for instruction in moves:
        num_of_boxes= instruction[0] 
        start_point = instruction[1] -1
        end_point = instruction[2] -1
        
        
    
        list_of_stacks[end_point].extend(list_of_stacks[start_point][-num_of_boxes:]) 
        del list_of_stacks[start_point][-num_of_boxes:]
        
        
pass