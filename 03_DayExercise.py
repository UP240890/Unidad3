#exercise1#
edad = 19
alt = 1.71
#exercise4#
print('--area del triangulo--')
base = int (input('cual es tu base? '))
Alt = int (input('cual es tu altura? '))
a= base*Alt/2
print('area', a)
#exercise5#
print('--perimetro del triangulo--')
la=int (input('lado1:'))
lb=int (input('lado2:'))
lc=int (input('lado3:'))
p=la+lb+lc
print('perimetro del triangulo',p) 
#exercise6#
print('--area y perimetro del rectangulo--')
large=float(input('largo:'))
width=float(input('ancho:'))
ar= large*width
per=2*(large+width)
print('area:',ar) 
print('perimetro: ',per) 
#exercise7#
print('--area y circunferencia--')
r=float(input('radio:'))
pi=3.14
area=pi*r**2
c=2*pi*r
print('area',area)
print('circuferencia',c)
#exercise8#
print('--interceccion Y--')
x=float(input('x:'))
y=(2*x)-2
print('y:',y)
#exercise9#
print('--pendiente--')
x1=float(input('x1:'))
x2=float(input('x2:'))
y1=float(input('y1:'))
y2=float(input('y2:'))
m=(y2-y1)/(x2-x1)
print('pendiente:',m)
#exercise10#
print('pendiente mayor:', y2<=m)
print('pendiente menor:', m<=y2)
print('pendiente igual:', y2==m)