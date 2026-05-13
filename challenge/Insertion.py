n = int(raw_input())
numbers = list(map(int, raw_input().split()))

for i in range(1, n):
    key = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key

    print "Pass:", numbers