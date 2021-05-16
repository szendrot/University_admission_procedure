#import os
#os.getcwd()

max_nr = 10  #int(input())

dep_dict = {'Biotech': 3, 'Chemistry': 3, 'Engineering': 5, 'Mathematics': 4, 'Physics': 2}
list_appl_1 = []
list_appl_2 = []
list_appl_3 = []

file = open('applicants_5.txt.', 'r')
for i in file:
    list_appl_1.append(i.replace('\n','').split())
file = open('applicants_5.txt.', 'r')
for i in file:
    list_appl_2.append(i.replace('\n','').split())
file = open('applicants_5.txt.', 'r')
for i in file:
    list_appl_3.append(i.replace('\n','').split())
    
dep_list_2 = []
for dep in dep_dict.keys():
    lista = []
    dep_lista = []
    for i in range(len(list_appl_1)):
        if list_appl_1[i][6] == dep:
            lista.append(list_appl_1[i])
    lista = sorted(lista, key=lambda x: (-float(x[dep_dict[dep]]), x[0], x[1]))
    for i in range(len(lista)):
        if i < max_nr:
            dep_lista.append([lista[i][0], lista[i][1], lista[i][dep_dict[dep]]])
            list_appl_2.remove(lista[i])
            list_appl_3.remove(lista[i])
    dep_list_2.append(dep_lista)

for n in range(len(dep_dict)):
    lista = []
    for i in range(len(list_appl_2)):
        if list_appl_2[i][7] == list(dep_dict.keys())[n]:
            lista.append(list_appl_2[i])
    lista = sorted(lista, key=lambda x:(-float(x[dep_dict[list(dep_dict.keys())[n]]]), x[0], x[1]))
    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - nr:
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][dep_dict[list(dep_dict.keys())[n]]]])
                list_appl_3.remove(lista[i])
         
for n in range(len(dep_dict)):
    lista = []
    for i in range(len(list_appl_3)):
        if list_appl_3[i][8] == list(dep_dict.keys())[n]:
            lista.append(list_appl_3[i])
    lista = sorted(lista, key=lambda x:(-float(x[dep_dict[list(dep_dict.keys())[n]]]), x[0], x[1]))
    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - len(dep_list_2[n]):
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][dep_dict[list(dep_dict.keys())[n]]]]) 

dep_list_3 = []
for n in range(len(dep_dict)):
    lista = sorted(dep_list_2[n], key=lambda x:(-float(x[2]), x[0], x[1]))
    dep_list_3.append(lista)

for n in range(len(dep_dict)):
    print(list(dep_dict.keys())[n])
    for i in dep_list_3[n]:
        print(f'{i[0]} {i[1]} {i[2]}')
    print('')



 
