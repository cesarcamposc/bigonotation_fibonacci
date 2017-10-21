'''
Created on 20/10/2017

@author: Admin
'''
def fibonacci1(n):
    if n < 0:
        print("N can not be less than zero")
    if n <= 2:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)

nterms = int(input("Enter n : "))

for i in range(0,nterms+1):
            print(fibonacci1(i))
        