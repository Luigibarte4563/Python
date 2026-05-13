n = int(raw_input())
numbers = list(map(int, raw_input().split()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    print "Pass: {}".format(numbers[j]) 