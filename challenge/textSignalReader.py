# Enter your code here. Read input from STDIN. Print output to STDOUT
text = raw_input().strip()

upper = 0
lower = 0
number = 0
symbol = 0


for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        number += 1
    else:
        symbol += 1

print upper, lower, number, symbol
    