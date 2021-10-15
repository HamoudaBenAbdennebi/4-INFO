import math
def saisirN():
    while True:
        N = int(input("donner N = "))
        if N in range(3,101):
            return N

def remp(N):
    T=list()
    for i in range(N):
        x=dict()
        x['nom']=input('nom = ')
        x['abs']=int(input('abscisse = '))
        x['ord']=int(input('ordonné = '))
        T.append(x)
    return T

def mat(N,T):
    M = [[0] * (N) for p in range(N)]
    for i in range(N):
        for j in range(N):
            M[i][j] = math.sqrt(((T[i]["abs"] - T[j]["abs"])**2)+((T[i]["ord"] - T[j]["ord"])**2))

    return M
def afficher(M,N):
    for i in range(N):
        for j in range(N):
            print(M[i][j],end=' ')
        print()
def finder(T,N):
    name = input('name = ')
    finded = False
    for i in range(N):
        if T[i]['nom'] == name:
            finded = True
            print(i+1)
            break
    
N = saisirN()
T= remp(N)
M = mat(N,T)
afficher(M,N)
finder(T,N)