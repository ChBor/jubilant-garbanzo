import random
#1
def Sum(n):
    if n > 0:
        return Sum(n // 10) + n % 10
    else:
        return 0
n=int(input("Enter digit:"))
print(Sum(n), "\n")




#2
def fib(n):
    if n <=1:
        return n
    return fib(n - 1) + fib(n - 2)
n=int(input("Enter digit:"))
print(fib(n), "\n")




#3
def list_mul(n):
    if len(n) == 0:
        return True
    else:
        return list_mul(n[:-1])*n[-1]
n=[]
for i in range(5):
    n.append(random.randint(1, 5))
print(n)
print(list_mul(n), "\n")




#4
def Power(n):
    n = n/2
    if n == 2:
        return True
    elif n > 2:
        return Power(n)
    else:
        return False
n=int(input("Enter digit:"))
if Power(n):
    print("YES", "\n")
else:
    print("NO", "\n")
Power(n)




#5
def main_func(a, b):
    def sec_func():
        global total
        total=a+b
        return total
    print(sec_func())
    fin=total+5
    return fin
a=int(input("Num1:"))
b=int(input("Num2:"))
print(main_func(a, b))