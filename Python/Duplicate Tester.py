s1 = input("Enter a string: ")
count = 0
has_dup = 'False'
char = ''
for s in s1:
    if s not in char:
        char += s
    else:
        count += 1
        has_dup = 'True'
print('duplicates: ', count)
