s = input()
symmetrical_symbols = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
mirror_symbols = {'E': '3', 'J': 'L', 'S': '2', 'Z': '5'}
mirror_symbols2 = {'3': 'E', 'L': 'J', '2': 'S', '5': 'Z'}
s2 = s[::-1]
regular_pol = False
symmetrical_pol = False
mirror_pol = False

all_symmetrical = True
for el in s2:
    if el not in symmetrical_symbols:
        all_symmetrical = False
        break

mirror_or_symmetrical = True
for el in s2:
    if el not in symmetrical_symbols and el not in mirror_symbols and el not in mirror_symbols2:
        mirror_or_symmetrical = False
        break

if s == s2 and all_symmetrical:
    symmetrical_pol = True
elif s == s2:
    regular_pol = True
elif mirror_or_symmetrical:
    s3 = ''
    for el in s2:
        if el in mirror_symbols:
            s3 += mirror_symbols[el]
        elif el in mirror_symbols2:
            s3 += mirror_symbols2[el]
        else:
            s3 += el
    print(s3)
    if s == s3:
        mirror_pol = True
if symmetrical_pol:
    print(f"{s} is a mirrored palindrome.")
elif mirror_pol:
    print(f"{s} is a mirrored string.")
elif regular_pol:
    print(f"{s} is a regular palindrome.")
else:
    print(f"{s} is not a palindrome.")

