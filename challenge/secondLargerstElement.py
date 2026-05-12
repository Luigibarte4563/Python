numbers = list(map(int, raw_input().split()))
numbers = list(set(numbers))

if len(numbers) < 2:
    print("No second largest")
else:
    numbers.sort()
    print(numbers[-2])