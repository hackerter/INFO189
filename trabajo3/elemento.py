#!/usr/bin/python
# -*- coding: utf-8 -*- 

import numpy as np

def incializarMatriz(c,valorFrontera):
    z=np.zeros((5,5))
    z[0][0]=c[0]
    z[0][1]=c[1]
    z[0][2]=c[2]
    z[0][3]=c[3]
    z[0][4]=c[4]

    z[1][0]=c[5]
    z[1][1]=c[6]
    z[1][2]=c[7]
    z[1][3]=c[8]
    z[1][4]=c[9]

    z[2][0]=c[5]
    z[2][1]=c[6]
    z[2][2]=c[7]
    z[2][3]=c[8]
    z[2][4]=c[9]

    z[3][0]=c[10]
    z[3][1]=c[11]
    z[3][2]=c[12]
    z[3][3]=c[13]
    z[3][4]=c[14]



    z[3][0]=c[15]
    z[3][1]=c[16]
    z[3][2]=c[17]

    z[3][3]=valorFrontera
    z[3][4]=valorFrontera


    z[4][0]=c[18]
    z[4][1]=c[19]
    z[4][2]=c[20]

    z[4][3]=valorFrontera
    z[4][4]=valorFrontera
    return(z)

def calculaMatrizEntera(c,frontera):
    z=incializarMatriz(c,frontera)

    d1=z
    d1Flip=np.flip(d1,1)

    numerosDeLaChimenea=list()
    for a in range(5):
        fila=(np.append(d1[a],d1Flip[a]) )
        numerosDeLaChimenea.append(fila )


    chimeneaMitad=(np.asarray(numerosDeLaChimenea))
    chimeneaMitad=np.flip(chimeneaMitad,0)


    for a in range(5):
        numerosDeLaChimenea.append(chimeneaMitad[a])
    chimeneaMitad=(np.asarray(numerosDeLaChimenea))
    chimeneaMitad=(np.delete(chimeneaMitad, 5, 1))
    chimeneaMitad=(np.delete(chimeneaMitad, 5, 0))

    chimeneaEntera=chimeneaMitad
    return(chimeneaEntera)



def recta1(x,y):
    Xr=7.5
    Yr=-7.5
    if(x>7.5):
        x=x-7.5
    if(y>7.5):
        y=y-7.5
    valor=Xr*x + Yr*y

    if(valor<=0):
        return True
    else:
        return False


#condiciones térmicas
kx = 0.8
area = float((7.5*7.5)/2)
Tf1 = 150   #interior
Tf2 = 10    #exterior
h1 = 2.0      #interior
h2 = 0.3    #exterior

#matrices borde elementoCuadrado
mij= np.array([[2,1,0,0],[1,2,0,0],[0,0,0,0],[0,0,0,0]])
mjk= np.array([[0,0,0,0],[0,2,1,0],[0,1,2,0],[0,0,0,0]])
mkm= np.array([[0,0,0,0],[0,0,0,0],[0,0,2,1],[0,0,1,2]])
mmi= np.array([[2,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,2]])

#matrices borde elementoTriangular
tij= np.array([[2,1,0],[1,2,0],[0,0,0]])
tjk= np.array([[0,0,0],[0,2,1],[0,1,2]])
tki= np.array([[2,0,1],[0,0,0],[1,0,2]])

#matrices factores elementoCuadrado
nx = np.array([[2, -2, -1, 1],[-2, 2, 1, -1],[-1, 1, 2, -2],[1, -1, -2, 2]])
ny = np.array([[2, 1, -1, -2],[1, 2, -2, -1],[-1, -2, 2, 1],[-2, -1, 1, 2]])

#ingreso coordenadas e5 y e6 triangulares superior e inferior
t1 = np.array([[0,0],[7.5,0],[7.5,7.5]])
t2 = np.array([[0,0],[7.5,0],[7.5,7.5]])
t5 = np.array([[0,0],[7.5,0],[7.5,7.5]])
t6 = np.array([[0,0],[7.5,0],[7.5,7.5]])

t3 = np.array([[0,0],[7.5,7.5],[0,7.5]])
t4 = np.array([[0,0],[7.5,7.5],[0,7.5]])
t7 = np.array([[0,0],[7.5,7.5],[0,7.5]])
t8 = np.array([[0,0],[7.5,7.5],[0,7.5]])


#matrices factores para triangulo respectivamente
trX1=[]
trY1=[]

trX2=[]
trY2=[]

trX5=[]
trY5=[]

trX6=[]
trY6=[]

trX3=[]
trY3=[]

trX4=[]
trY4=[]

trX7=[]
trY7=[]

trX8=[]
trY8=[]

#calculo factores triangulo
def elementoTriangular(b):
    tb = []
    tbb = []
    tc = []
    tcc = []
    bi = b[1][1] - b[2][1]
    bj = b[2][1] - b[0][1]
    bk = b[0][1] - b[1][1]
    
    ci = b[2][0] - b[1][0]
    cj = b[0][0] - b[2][0]
    ck = b[1][0] - b[0][0]
    
    tb.append([bi*bi,bi*bj,bi*bk])
    tb.append([bj*bi,bj*bj,bj*bk])
    tb.append([bk*bi,bk*bj,bk*bk])
    tbb = np.array(tb)
    
    
    tc.append([ci*ci,ci*cj,ci*ck])
    tc.append([cj*ci,cj*cj,cj*ck])
    tc.append([ck*ci,ck*cj,ck*ck])
    tcc = np.array(tc)
    return tbb,tcc


#retorna matrixes X e Y de cada elemento triangular
[trX1, trY1] = elementoTriangular(t1)
[trX2, trY2] = elementoTriangular(t2)
[trX5, trY5] = elementoTriangular(t5)
[trX6, trY6] = elementoTriangular(t6)

[trX3, trY3] = elementoTriangular(t3)
[trX4, trY4] = elementoTriangular(t4)
[trX7, trY7] = elementoTriangular(t7)
[trX8, trY8] = elementoTriangular(t8)





#matrices de conduccion x elemento
kd9 = ((0.08*nx) + ((2.0/9)*ny))
e9 = np.array([3,4,9,8])

kd10 = ((0.08*nx) + ((2.0/9)*ny))
e10 = np.array([4,5,10,9])

kd11 = ((0.08*nx) + ((2.0/9)*ny))
e11 = np.array([8,9,14,13])

kd12 = ((0.08*nx) + ((2.0/9)*ny))
e12 = np.array([9,10,15,14])

kd13 = (((14.0/45)*nx) + ((2.0/35)*ny))
e13 = np.array([11,12,17,16])

kd14 = (((14.0/45)*nx) + ((2.0/35)*ny))
e14 = np.array([12,13,18,17])

kd15 = (((14.0/45)*nx) + ((2.0/35)*ny))
e15 = np.array([16,17,20,19])

kd16 = (((14.0/45)*nx) + ((2.0/35)*ny))
e16 = np.array([17,18,21,20])

kd1 = (kx/(area*4))*(trX1+trY1)
e1 = np.array([1,2,7])

kd2 = (kx/(area*4))*(trX2+trY2)
e2 = np.array([2,3,8])

kd3 = (kx/(area*4))*(trX3+trY3)
e3 = np.array([1,7,6])

kd4 = (kx/(area*4))*(trX4+trY4)
e4 = np.array([2,8,7])

kd5 = (kx/(area*4))*(trX5+trY5)
e5 = np.array([6,7,12])

kd6 = (kx/(area*4))*(trX6+trY6)
e6 = np.array([7,8,13])

kd7 = (kx/(area*4))*(trX7+trY7)
e7 = np.array([6,12,11])

kd8 = (kx/(area*4))*(trX8+trY8)
e8 = np.array([7,13,12])


#matrices de convectividad x elemento
kc9 = ((h2*12.5)/6)*mij
kc10 = ((h2*12.5)/6)*mij

kc11 = ((h2*12.5)/6)*mkm
kc12 = ((h2*12.5)/6)*mkm


kc13 = ((h2*17.5)/6)*mmi
kc15 = ((h2*17.5)/6)*mmi

kc14 = ((h2*17.5)/6)*mjk
kc16 = ((h2*17.5)/6)*mjk


kc1 = ((h2*7.5)/6)*tij
kc2 = ((h2*7.5)/6)*tij

kc3 = ((h2*7.5)/6)*tki
kc7 = ((h2*7.5)/6)*tki



#vectores de termicidad x elemento
f11 = (150)*np.array([0,0,1,0])
f12 = (150)*np.array([0,0,1,0])
f14 = (150)*np.array([0,0,1,0])
f16 = (150)*np.array([0,0,1,0])

f1 = ((h2*Tf2*7.5)/2)*np.array([1,1,0])
f2 = ((h2*Tf2*7.5)/2)*np.array([1,1,0])
f3 = ((h2*Tf2*7.5)/2)*np.array([1,0,1])
f7 = ((h2*Tf2*7.5)/2)*np.array([1,0,1])

f6 = (150)*np.array([0,0,1])

f9 = ((h2*Tf2*12.5)/2)*np.array([1,1,0,0])
f10 = ((h2*Tf2*12.5)/2)*np.array([1,1,0,0])
f13 = ((h2*Tf2*17.5)/2)*np.array([1,0,0,1])
f15 = ((h2*Tf2*17.5)/2)*np.array([1,0,0,1])



#Matriz ensamble de elementos K
MT = np.zeros((21,21))

#Matriz k general de triángulo
for i in range(0,len(kd1)):#fila
    for j in range(0,len(kd5)):#columna
         MT[e1[i]-1][e1[j]-1]+=kd1[i][j]+kc1[i][j]
         MT[e2[i]-1][e2[j]-1]+=kd2[i][j]+kc2[i][j]    
         MT[e3[i]-1][e3[j]-1]+=kd3[i][j]+kc3[i][j]    
         MT[e4[i]-1][e4[j]-1]+=kd4[i][j]
         
         MT[e5[i]-1][e5[j]-1]+=kd5[i][j]
         MT[e6[i]-1][e6[j]-1]+=kd6[i][j]
         MT[e7[i]-1][e7[j]-1]+=kd7[i][j]+kc7[i][j]    
         MT[e8[i]-1][e8[j]-1]+=kd8[i][j]
         

#Matriz k general de cuadrado
for i in range(0, len(kd9)):#fila
    for j in range(0, len(kd9)):#columna
        MT[e9[i]-1][e9[j]-1]+=kd9[i][j]+kc9[i][j]
        MT[e11[i]-1][e11[j]-1]+=kd11[i][j]+kc11[i][j]
        MT[e12[i]-1][e12[j]-1]+=kd12[i][j]+kc13[i][j]
        MT[e10[i]-1][e10[j]-1]+=kd10[i][j]+kc10[i][j]

        MT[e13[i]-1][e13[j]-1]+=kd13[i][j]+kc13[i][j]
        MT[e14[i]-1][e14[j]-1]+=kd14[i][j]+kc14[i][j]
        MT[e16[i]-1][e16[j]-1]+=kd16[i][j]+kc16[i][j]
        MT[e15[i]-1][e15[j]-1]+=kd15[i][j]+kc15[i][j]

F = np.zeros(21)        

#Vector de termincidad F triángulo
for i in range(0,len(e1)):
    F[e1[i]-1]+=f1[i]
    F[e2[i]-1]+=f2[i]
    F[e3[i]-1]+=f3[i]
    F[e7[i]-1]+=f7[i]
    F[e6[i]-1]+=f6[i]

#Vector de termincidad F cuadrado
for i in range(0,len(e11)):
    F[e11[i]-1]+=f11[i]
    F[e12[i]-1]+=f12[i]
    F[e14[i]-1]+=f14[i]
    F[e16[i]-1]+=f16[i]
    F[e9[i]-1]+=f9[i]
    F[e10[i]-1]+=f10[i]
    F[e13[i]-1]+=f13[i]
    F[e15[i]-1]+=f15[i]


#Setea las condiciones iniciales en la matriz de ensamble
for i in range(0,21):
        MT[14][i]=0.0
        MT[13][i]=0.0
        MT[12][i]=0.0
        MT[20][i]=0.0
        MT[17][i]=0.0
MT[14][14]=1.0
MT[13][13]=1.0
MT[12][12]=1.0    
MT[20][20]=1.0
MT[17][17]=1.0




c = np.linalg.solve(MT, F)



with (open("sol.txt",'w')) as a:		#exporta los polinomios en archivo de texto
  for i in c:
    a.write(str(i)+"\n")
    
def buscarnodo(x1,y1):
    x1=int(x1)
    y1=int(y1)
    x=0
    y=0
    if x1>=0 and x1>40 and x1<=80:
        x=80-x1
    else:
        x=x1
    if y1>=0 and y1>50 and y1<=100:
        y=100-y1
    else:
        y=y1
    cx=0
    cy=0
    while True:
        if x<=7.5:
            cx=0
            break
        if x<=15:
            cx=1
            break
        if x<=25:
            cx=2
            break
        if x<=40:
            cx=3
            break
    while True:
        if y<=7.5:
            cy=0
            break
        if y<=15:
            cy=1
            break
        if y<=32.5:
            cy=2
            break
        if y<=50:
            cy=3
            break

    MNodos = [[0 for x in range(4)] for x in range(4)]
    MNodos[0][0]=e1
    MNodos[0][1]=e5
    MNodos[0][2]=e13
    MNodos[0][3]=e15
    MNodos[1][0]=e2
    MNodos[1][1]=e6
    MNodos[1][2]=e14
    MNodos[1][3]=e16
    MNodos[2][0]=e9
    MNodos[2][1]=e11
    MNodos[3][0]=e10
    MNodos[3][1]=e12

    largoM = len(MNodos[cx][cy])

    if(largoM==3):
        if(MNodos[cx][cy][0] == 1 and MNodos[cx][cy][1] == 2 and MNodos[cx][cy][2] == 7):
            if(recta1(x,y)):
                print(e3)
                return e3

        if(MNodos[cx][cy][0] == 2 and MNodos[cx][cy][1] == 3 and MNodos[cx][cy][2] == 8):
            if(recta1(x,y)):
                print(e4)
                return e4

        if(MNodos[cx][cy][0] == 6 and MNodos[cx][cy][1] == 7 and MNodos[cx][cy][2] == 12):
            if(recta1(x,y)):
                print(e7)
                return e7
        if(MNodos[cx][cy][0] == 7 and MNodos[cx][cy][1] == 8 and MNodos[cx][cy][2] == 13):
            if(recta1(x,y)):
                print(e8)
                return e8




    return MNodos[cx][cy]

tt = np.zeros((22,2))
tt[1] =[0,0]
tt[2] =[7.5,0]
tt[3] =[15.0,0]
tt[6] =[0,7.5]
tt[7] =[7.5,7.5]
tt[8] =[15.0,7.5]
tt[11] =[0,15.0]
tt[12] =[7.5,15.0]
tt[13] =[15.0,15.0]


def revisaCuadrado(elementoCuadrado,x,y):
    criterio=0
   
    for nodo in elementoCuadrado:
        if(nodo<=15):
            criterio=criterio+1
    if(criterio==4):
        b=12.5
        a=7.5
        print(elemCuadrado(elementoCuadrado,a,b,x,y))
        return "a"
    b=7.5
    a=17.5
    print(elemCuadrado(elementoCuadrado,a,b,x,y))
    return [b,a]



def elemCuadrado(nn,b,a,x,y):   #nm = vector nodos, b=largo cuadrado, a=alto cuadrado, x=coordenada, y=coordenada

    ni = (1-(float(x)/b) ) *(1-(float(y)/a)) 
 
    nj = (float(x)/b)*((1-(float(y)/a)))
 
    nk = (float(x)/b)*(float(y)/a)
 
    nm = (1-(float(x)/b))*((float(y)/a))
    

    rst = c[nn[0]-1]*ni   +   c[nn[1]-1]*nj +   c[nn[2]-1]*nk +   c[nn[3]-1]*nm

    
    return rst



def elemTriangulo(cc,x,y):
    
    
    ni = (1.0/(2*area))*((tt[cc[0]][0]*tt[cc[2]][1]-tt[cc[2]][0]*tt[cc[1]][1])+ (tt[cc[1]][1]-tt[cc[2]][1])*x + (tt[cc[2]][0]-tt[cc[1]][0])*y )
    
    
    nj = (1.0/(2*area))*( (tt[cc[2]][0]*tt[cc[0]][1]-tt[cc[0]][0]*tt[cc[2]][1]) +(tt[cc[2]][1]-tt[cc[0]][1])*x + (tt[cc[0]][0]-tt[cc[2]][0])*y )
    
    nk = (1.0/(2*area))*( (tt[cc[0]][0]*tt[cc[1]][1]-tt[cc[1]][0]*tt[cc[0]][1]) + (tt[cc[0]][1]-tt[cc[1]][1])*x + (tt[cc[2]][0]-tt[cc[0]][0])*y )
    
    rst = ni*c[cc[0]-1] + nj*c[cc[1]-1] + nk*c[cc[2]-1]
    return rst


matrizEntera=calculaMatrizEntera(c,Tf1)




from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np







### Distancia entre puntos, no deberia ser necesario cambiarlo
x = np.array([[0   ,7.5   ,15   ,27.5   ,40   ,52.5   ,65    ,72.5    ,80     ]])

y = np.array([[0,7.5,15,32.5,50,67.5,85,92.5,100]])



fig = plt.figure()
ax = fig.gca(projection='3d')


#Creacion del mesh entre los puntos
x, y = np.meshgrid(x, y)


#Funcion para graficar
surf = ax.plot_surface(x, y, matrizEntera, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# eje z delmitador, Tf1 , es el maximo
ax.set_zlim(0, Tf1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Barra de color del eje z
fig.colorbar(surf, shrink=0.51, aspect=5)

plt.show()



fig, ax = plt.subplots()
heatmap = ax.pcolor(matrizEntera, cmap=plt.cm.coolwarm)
plt.show()




x = input("Ingrese valor de X: ")
y = input ("Ingrese valor de Y: ")

q = buscarnodo(x,y)


if(len(q)==4):
    print(revisaCuadrado(q,x,y))
if(len(q)==3):
	print(elemTriangulo(q,x,y))