#Найти произведение цифр числа.
a=input("введите число")
c=0
b=1
n=len(a)
for i in range(len(a)):
    a=int(a)
    b=a%10*b
    a=a//10

print(b)