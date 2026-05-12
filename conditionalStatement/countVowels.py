s = raw_input().strip().lower()

vowels = 0

for i in s:
    if i in "aeiou":
        vowels += 1

print(vowels)