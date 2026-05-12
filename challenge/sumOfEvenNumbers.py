# Enter your code here. Read input from STDIN. Print output to STDOUT
n = list(map(int, raw_input().split()))

sum_even = 0

for i in n:
    if i % 2 == 0:
        sum_even += i
        
        
print(sum_even)
        