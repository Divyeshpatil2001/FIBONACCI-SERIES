def fibonacci_series(n):
    fibonacci_sequence = [0,1]
    
    for i in range(2,n):
        next_number = fibonacci_sequence[-1]+fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

n = int(input("enter your nth number for fibonacci series"))
result = fibonacci_series(n)
print(result)