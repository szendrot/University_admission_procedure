nr_app, nr_acc = 5, 3
app_list = []

n =  'Cole Collins 3.68'
app_list.append(n.split())
n = 'Dolores Baldwin 3.40'
app_list.append(n.split())
n = 'Brett Boyer 2.45'
app_list.append(n.split())
n = 'Nora Alston 3.71'
app_list.append(n.split())
n = 'Jessy Moore 3.14'
app_list.append(n.split())

sort_app_list = sorted(app_list, key=lambda x: (-float(x[2]), x[0], x[1]))
print('Successful applicants:')
for i in range(len(sort_app_list)):
    if i < nr_acc:
        print(sort_app_list[i][0] + ' ' + sort_app_list[i][1])

