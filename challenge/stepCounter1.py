# Enter your code here. Read input from STDIN. Print output to STDOUT
numbers = list(map(int, raw_input().strip().split()))

count = 0

for i in range(len(numbers) - 1):
    if numbers[i + 1] > numbers[i]:
        count += 1

print(count)
    
        