s = input().strip()

freq = {}

for ch in s:
    freq[ch] = ch.get(ch, 0) + 1    

found = False

for ch in s:
    if freq[ch] == 1:
        print(ch)
        found = True
        break

if not found:
    print("None")