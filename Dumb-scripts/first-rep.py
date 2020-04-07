a=[2, 1, 3, 5, 3, 2]

def firstDuplicate(a):
    lista=[]
    yatengo=[]
    for i in range(len(a)):
        if a[i] in yatengo :
            lista.append(a[i])

        yatengo.append(a[i])
    
    for l in lista:
        print(l)
        
    if lista == []:
        return -1
    else:
        return(lista[0])

firstDuplicate(a)