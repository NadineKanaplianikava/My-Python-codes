#Given a natural number n(n≤9). Write a program that prints an additional table for all numbers from 1 to n.
n = int(input())
for i in range(1, n+1):
    for j in range(1,10):
        print(f'{i} + {j} = {i + j}')
    print()
