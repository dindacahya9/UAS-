#Dinda Cahya Macharani
#UAS Prak FisKom
import numpy as p
import matplotlib.pyplot as plt

def func(x):
    return (x**2)*p.exp(-2*x)
a = float(input('Batas bawah(a) = '))   
b = float(input('Batas atas (b) = '))   
n = int (input('Jumlah grid (n) = '))   

#reiman
x = p.linspace(a,b,n)
dx = (x[-1]-x[0])/(n-1)

hasil = 0

for i in range (n-1):
    hasil += dx*func(x[i])
print('Hasil = ', hasil)

xp = p.linspace(a,b)
plt.plot(xp,func(xp))
for i in range(n-1):
    plt.bar(x[i],func(x[i]), align = 'edge',width=dx, color='green',edgecolor='red')
plt.show()
