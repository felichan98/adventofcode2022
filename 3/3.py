import string
#Mapping priorities through ascii

dict_priorities = {}

common_characters = []
sum_priorities = 0

lowercase_letters = [x for x in string.ascii_lowercase] 
uppercase_letters = [x for x in string.ascii_uppercase] 

for index, letter in enumerate(lowercase_letters):
    dict_priorities[letter] = [index+1]

for index, letter in  enumerate(uppercase_letters):
    dict_priorities[letter] = [index+27]
    

f = open('input.txt', 'r')

content = f.read()

list_cosi = []

list_cosi= (content.split("\n"))

for i in list_cosi:
    first_half  = i[:len(i)//2]
    second_half = i[len(i)//2:]
    
    common_characters.append(set(first_half).intersection(second_half).pop())
    
# assigning priorities

for x in common_characters:
    sum_priorities += dict_priorities[x][0]
    
    
    
#second part

#select each 3-element group from input and find the common letters

common_badges = []

gruppi =  [list_cosi[i:i + 3] for i in range(0, len(list_cosi), 3)]

for gruppo in gruppi:
    
	common_badges.append(set(gruppo[0]) & set(gruppo[1]) & set(gruppo[2]))

sum_priorities_2=0

for x in common_badges:
    sum_priorities_2 += dict_priorities[x.pop()][0]
    
pass