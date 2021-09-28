'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
      if n==0 or n==1:
        return False
    if n<0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n=int(input("n="))
print(is_prime(n))
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
    p=1
    for i in lst:
        p=p*i
    return p
lst=[1,2,3,4]
print(get_product(lst))
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
    if (y == 0):
            return x
    else:
        return get_cmmdc_v1(y, x % y)
x = int(input("x= "))
y = int(input("y= "))
print("CMMDC:", get_cmmdc_v1(x,y))
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    if x==0:
        return y
    if y==0:
        return x
    while x != y:
        if x>y:
            x=x-y
        else:
            y=y-x
    return x
n=input("dati primul nr:")
a=int(n)
n=input("dati al doilea nr:")
b=int(n)
print(get_cmmdc_v2(a,b))
  
  
def main():
  # interfata de tip consola aici

if __name__ == '__main__':
  main()
