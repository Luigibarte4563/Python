# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input().strip()

result = ""

for ch in s:
    if ch not in result:
        result += ch
        
print "No Duplicates:", result