#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    fibonacci_sequence = [0]  # Start with the first Fibonacci number
    if length > 1:
        fibonacci_sequence.append(1)  # Add the second Fibonacci number
    
    for i in range(2, length):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)
    
    print(fibonacci_sequence)