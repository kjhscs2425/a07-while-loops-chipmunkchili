# write a factorial function, given n, you return n!

def factorial(n):
    if n==1:
        return 1
    else:
        answer = n * factorial(n-1)
    
    return answer
    
print(factorial(4))