num=109481562932
prime=[]
dino=2

while dino<=num:
    # highest prime of a number can only be itself
    while num%dino==0:
        #if remaider is zero, then divisible
        x,y=divmod(num,dino)
        if y==0:
            # if the quotient is also divisible by the same
            prime.append(dino)
            num=x
            # to proceed till the quotients remains divisible by the same prime number
    else:
        dino+=1
        # looking for the next divisible prime number
print(prime)
