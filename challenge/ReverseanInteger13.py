n = int(raw_input())

negative = False

if n < 0:
    negative = True
    n = -n
    
reverse = 0

while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
    
if negative:
    reverse = -reverse
    
print reverse
