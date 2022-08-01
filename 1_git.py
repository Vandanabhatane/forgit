s='anbcvvghcccnj'
char_count= {}
for c in s:
    if c in char_count:
        char_count[c] += 1
    else:
        char_count[c] = 1

print(char_count)
