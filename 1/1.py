f = open('input.txt', 'r')

content = f.read()

#print(content)

list = []

list= (content.split("\n\n")) #241 clusters

new_list = []
for i in list:
	new_list.append(i.replace('\n', ' '))
    


sum_results = []

for i in new_list:
    int_elements_list = []
    element_list = i.split(" ")
    for j in element_list:
        if j != '':
            int_elements_list.append(int(j))
        
        
    summ = sum(int_elements_list)
    sum_results.append(summ)
    
sorted_results = sum_results.sort()

max_three = sum_results[240]+ sum_results[239] + sum_results[238]
pass