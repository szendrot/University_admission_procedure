#import os
#os.getcwd()

max_nr = 10  #int(input())

dep_list = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']
list_appl_1 = []
list_appl_2 = []
list_appl_3 = []

file = open('applicants_4.txt.', 'r')
for i in file:
    list_appl_1.append(i.replace('\n','').split())
file = open('applicants_4.txt.', 'r')
for i in file:
    list_appl_2.append(i.replace('\n','').split())
file = open('applicants_4.txt.', 'r')
for i in file:
    list_appl_3.append(i.replace('\n','').split())
    
dep_list_2 = []
for dep in dep_list:
    lista = []
    dep_lista = []
    for i in range(len(list_appl_1)):
        if list_appl_1[i][3] == dep:
            lista.append(list_appl_1[i])
    lista = sorted(lista, key=lambda x: (-float(x[2]), x[0], x[1]))
    for i in range(len(lista)):
        if i < max_nr:
            dep_lista.append([lista[i][0], lista[i][1], lista[i][2], lista[i][3]])
            list_appl_2.remove(lista[i])
            list_appl_3.remove(lista[i])
    dep_list_2.append(dep_lista)

for n in range(len(dep_list)):
    lista = []
    for i in range(len(list_appl_2)):
        if list_appl_2[i][4] == dep_list[n]:
            lista.append(list_appl_2[i])
    lista = sorted(lista, key=lambda x:(-float(x[2]), x[0], x[1]))
    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - nr:
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][2], lista[i][4]])
                list_appl_3.remove(lista[i])
              
for n in range(len(dep_list)):
    lista = []
    for i in range(len(list_appl_3)):
        if list_appl_3[i][5] == dep_list[n]:
            lista.append(list_appl_3[i])
    lista = sorted(lista, key=lambda x:(-float(x[2]), x[0], x[1]))
    if lista != []:
        nr = len(dep_list_2[n])
        for i in range(len(lista)):
            if i < max_nr - len(dep_list_2[n]):
                dep_list_2[n].append([lista[i][0], lista[i][1], lista[i][2], lista[i][5]]) 

dep_list_3 = []
for n in range(len(dep_list)):
    lista = sorted(dep_list_2[n], key=lambda x:(-float(x[2]), x[0], x[1]))
    dep_list_3.append(lista)

for n in range(len(dep_list)):
    print(dep_list[n])
    for i in dep_list_3[n]:
        print(f'{i[0]} {i[1]} {i[2]}')
    print('')



 
