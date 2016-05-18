#1
L = ["python","poo",999,666]

L[2] = 900
L[3] = 600

#2
L2 = [9,99,999,9999]

L2.remove(9)
L2.remove(99)

#3
L3 = [4,43,432,4321]

L3[0] = 432
L3[1] = "info2016"
L3[2] = 'mod1'

#4
a=["python","java", "php","c++"]
b=len(a)
print (a)
print (b)

#5
a=["no se nada"]
print (a*3)

#6
a=["Resistencia","Corrientes","Posadas", "Parana"];
b=a[1]
print (b)

#7
a= ["Resistencia", "Corrientes", "Posadas", "Parana"]
print a
print a.pop(3)
print a

#8
a= [1990,1993,1987,1990,1988,1993,2004,2014,2014,2014,2000,2016,2016]
print a
x= a[1] - a[0]
print x

#9
a=[1990,1993,1987,1990,1988,1993,2004,2014,2014,2014,2000,2016,2016]
print a
a[0]=1987
a[1]=1988
a[2]=1990
a[4]= 1993
a[6]=2000
a[7]=2004
a[10]=2014
print a

#10
a=[1990,1993,1987,1990]
print (a)
a.remove(1990)
a.remove(1990)
print (a)

#11
a=["INFO 2013", "INFO 2014"]

print (a)

a.append("INFO 2014")
a.append("INFO 2015")
print (a)

#12
a= ["A", 1, "B", 2,"C",3]
print a
a.remove("A")
a.remove(2)
a.remove("C")
a.remove(3)
print a

#13
a=["A",1,"B",2,"C",3]
print a
print a
a.remove("A")
print a
print a

#14
a=['A', 1, 'B',2,'C',3]

print (a)
a.reverse()

print (a)

#15
L15 = ["F", 1, "G", 2, "H", 3]
L15.reverse()

print(L15)

#16
L16 = ["F", 4, "G", 5, "H", 6]

len(L16)
L16[2] = "Hijo" 

print(L16)

#17
a= ["A","B", "C"]
print a
i= len(a)
for x in range (0,i-1):
	a.remove(a[x])

#18
a=["Unalista"]
b=["OtraLista"]
c=a+b

print (a)
print (b)
print (c)