
text = 'HelloOo!'
dic = {}
for i in text:
    if i.lower() in dic:
        dic[i.lower()]+=1
    else:
        dic[i.lower()] =1
my_list = list(dic.items())
for mx in range(len(my_list)-1, -1, -1):
    swapped = False
    for i in range(mx):
        if my_list[i][1] < my_list[i+1][1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            swapped = True
    if not swapped:
        break
go = 1
while(go):
    holy = 0
    for i in text:
        if dic[i.lower()] == 0:
            continue
        for j in my_list:
            if dic[j[0]] == 0:
                continue
            if j[1] > dic[i.lower()]:
                break
            else:
                dic[i.lower()] = 0
                print(i.lower(),j[1])
                holy = 1
                break
        if holy == 1:
            holy = 0
            break
    go = 0
    for k in text:
        if(dic[k.lower()])>0:
            go = 1
