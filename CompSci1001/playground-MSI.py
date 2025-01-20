
def recursiveFactorization(x,arr=[]):

    until = int( x*(1/2) ) + 1

    for i in range(2 , until):
        if x % i == 0:
            arr.append(i)
            break
        if i == until:
            return sorted(arr)
    else:                  
        arr.append(int(x))  
        print(arr)          
        return sorted(arr)
    
    recursiveFactorization(x/i, arr)

if __name__=='__main__':
    print(recursiveFactorization(33))

