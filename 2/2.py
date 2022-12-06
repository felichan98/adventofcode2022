#A SASSO	#X PERDITA
#B CARTA	#Y PAREGGIO
#C FORBICI	#Z VITTORIA

#punteggio = 
#6 VITTORIA #3 PAREGGIO #0 PERDITA 
	#+
#1 A, #2B, #3C


#Vittoria if r1 - r1 = 0
#Perdita 


f = open('input.txt', 'r')

content = f.read()

#print(content)

list = []

list= (content.split("\n"))
new_list = []

for i in list:
    players = i.split(' ')
    
    if(players[0]=='A' and players[1]=='X'):
        i = i.replace('X', 'C')
    if(players[0]=='A' and players[1]=='Y'):
        i = i.replace('Y', 'A')
    if(players[0]=='A' and players[1]=='Z'):
        i = i.replace('Z', 'B')
        
        
        
    if(players[0]=='B' and players[1]=='X'):
        i = i.replace('X', 'A')
    if(players[0]=='B' and players[1]=='Y'):
        i = i.replace('Y', 'B')
    if(players[0]=='B' and players[1]=='Z'):
        i = i.replace('Z', 'C')
        
        
    if(players[0]=='C' and players[1]=='X'):
        i = i.replace('X','B')
    if(players[0]=='C' and players[1]=='Y'):
        i = i.replace('Y','C')
    if(players[0]=='C' and players[1]=='Z'):
        i = i.replace('Z','A')
        
    if(i!=''):
    	new_list.append(i)

    

n_pareggi =0
n_vittorie = 0
n_sconfitte = 0

score_choices = 0

for i in new_list:
    players = i.split(' ')
    
    if(players[1] == 'A'): score_choices +=1
    if(players[1] == 'B'): score_choices +=2
    if(players[1] == 'C'): score_choices +=3
    
    
    if(players[0] == players[1]): n_pareggi += 1
    
    if(players[0]=='A' and players[1]=='B'): n_vittorie +=1
    if(players[0]=='B' and players[1]=='C'): n_vittorie +=1
    if(players[0]=='C' and players[1]=='A'): n_vittorie +=1
    
    if(players[0]=='A' and players[1]=='C'): n_sconfitte +=1
    if(players[0]=='B' and players[1]=='A'): n_sconfitte +=1
    if(players[0]=='C' and players[1]=='B'): n_sconfitte +=1
    
    
#calcolo punteggio

punteggio = score_choices + (n_vittorie*6) + n_pareggi*3


    
pass