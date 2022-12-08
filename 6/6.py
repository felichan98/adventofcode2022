
id_exercise = 2

f = open('input.txt', 'r')

content = f.read()

total_len = len(content)

if(id_exercise ==1):
	buffer = [None] * 4

	start_of_seq = 0
	i=0
	while(i<total_len):
		
		buffer[0] = buffer[1]
		buffer[1] = buffer[2]
		buffer[2] = buffer[3]
		buffer[3] = content[i]
		if i>2 and len(buffer) == len(set(buffer)):
				#marker trovato
			start_of_seq = i+1
			break
		i+=1
    

buffer = [None] * 14

start_of_seq = 0
i=0
while(i<total_len):
    
    #spostamento
    index = 0
    while(index<13):
        buffer[index] = buffer[index+1]
        index += 1
    buffer[13] = content[i]
    
    if i>13 and len(buffer) == len(set(buffer)):
            start_of_seq = i+1
            break
        
    i+=1

pass