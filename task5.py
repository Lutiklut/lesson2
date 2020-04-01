#Вывести цифры числа на каждой строчке.
a=input("введите число")
c=0
b=0
n=len(a)
# перепишем число в обратном порядке
for i in range(len(a)):
    a=int(a)
    b=a%10
    a=a//10
    c=c*10+b
print(c)
# вывод цифр числа
for i in range(n):
    d=c%10
    c=c//10
    print(d)