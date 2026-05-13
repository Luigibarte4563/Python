n = int(raw_input())
numbers = list(map(int, raw_input().split()))

for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
    if swapped:
        print "Pass: {}".format(numbers)
    else:
        break
            