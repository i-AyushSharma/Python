def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

#Fibonacci Sequence
def fibonaccisequence(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonaccisequence(n-1)+fibonaccisequence(n-2)
    
for i in range(20):
    print(fibonaccisequence(i))