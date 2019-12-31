'''
check wheter a number is prime or not
'''

def is_prime(num):
    is_prime=True

    # prime number is always greater than 1
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                is_prime=False
                break     
    else:
        is_prime=False 
    
    return is_prime

num = int(input("enter a number: "))
#int(input("Enter any number: "))
res=is_prime(num)
print(res)
