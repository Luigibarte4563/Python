# Enter your code here. Read input from STDIN. Print output to STDOUT

text = raw_input().strip()

if text == text[::-1]:
    print("YES")
else:
    print("NO")