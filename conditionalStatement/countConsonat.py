s = raw_input().strip().lower()

consonant = 0

for ch in s:
    if ch.isalpha() and ch not in "aeiou":
        consonant += 1

print(consonant)