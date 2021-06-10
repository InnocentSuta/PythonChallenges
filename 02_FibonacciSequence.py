''' The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, 
    starting with 0, and 1. The Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
    Written as a rule, the expression is: Xn = X(n-1) + X(n-2)
    
    This program finds the nth term in the fibonacci sequence.
  '''
def fibonnaci(n):
    
    if n < 0:
        print("Enter Valid Input")
        
    elif n == 0:
        return 0
    
    elif n in range( 1 , 2):
        return 1
    
    else:
        return fibonnaci(n - 1) + fibonnaci( n - 2)
    
print(fibonnaci(10))

'''
By Innocent Suta 

'''