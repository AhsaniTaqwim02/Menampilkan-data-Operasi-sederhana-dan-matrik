from math import sqrt
#Cara menampilkan hasil

m = 10
print(m)
print("hasil m+m",m+m)
print("hasil m x m",m*m)

print('-------------')

#menampilkan karakter
kar_1 = 'kalau orang lain bisa'
kar_2 = 'kenapa harus aku'
print(kar_1+' '+kar_2)
print(kar_1[0:12])
karakter = 'kalau oranglain bisa kenapa harus aku'
print(karakter.split())

print('------------------')
from math import sqrt
#operasi perhitungan sederhana
a = 10
b = -4.5
c = 5.0
d = 5/2

print(a+b)
print("bentuk bilangan integer = ", int(b))
print("bentuk bilangan float = ", float(a))
print("perkalian c x d", c*d)
print("--------------------")
print("contoh soal = tentukan keccepatan v(w(usaha) = 20 ; s(jarak) = -10 t(waktu) = 2")
w = 20
s = -10
t = 2
#v = s/t
kecepatan = s/t
print(kecepatan,"m/s")
print("--------------")

from math import sqrt
print("soal 1 = tentukan energi dalam j dari m = 9,31 x 10^-31; c = 3x10^8")
m = 9.31*10**-31
c = 3*10**8
#energi : E = m x c^2
E = m * c**2
print (E)

print("-------------------")
print("soal 2 = tentukan periode dalam s (l = 0,5 m ; g = 9,8 m/s^2")
l = 0.5
g = 9.8
#periode = 2 * pi * sqrt (l/g)
periode = 2*pi*sqrt(l/g)
print(periode)

print('------------------------')
from numpy import *
#menampilkan matrik
M = [[0 ,1 ,1 ,0], [2,3,2,1]]
print(M)

a= zeros((3,3), int)
print(a)
print("  ")
a[0] = [1,4,2]
a[1,1] = 9
a[2,0:2] = [9]
print(a)

from numpy import array
print('  ')
A =  array([[2,3,4],[2,3,4]])
print(A)

print('-----------------------')
import matplotlib.pyplot as plt
from  numpy import arange,sin,cos

x = arange(0.0,6.0,0.1)
plt.plot(x,sin(x),'o-',x,cos(x),'s-')
plt.title('grafik sinusoidal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(('sinus','cosinus'),loc = 0)
plt.grid(True)
plt.show()
