# практична 6 завадння 6.1
text = "Hello!"

for char in text:
    kod = ord(char)

    if 48 <= kod <= 57:
        print(f"Символ {char}  це цифра")
    elif (65 <= kod <= 90) or (97 <= kod <= 122):
        print(f"Символ {char}  це латинська літера")
    elif kod == 32:
        print(f"Це звичайний пробіл")
    else:
        print(f"Символ {char}  інший знак")
print("\n")

#6.2
text = "Level"

lowered = ""
for char in text:
    code = ord(char)
    if 65 <= code <= 90:
        code = code + 32        # різниця між великою і малою літерою = 32
    lowered = lowered + chr(code)

# Порівнюємо символи з двох кінців
left = 0
right = len(lowered) - 1
is_palindrome = True

while left < right:
    if lowered[left] != lowered[right]:
        is_palindrome = False
    left = left + 1
    right = right - 1

print("Рядок:", text)
print("Після зведення до малих:", lowered)
print("Паліндром", is_palindrome)




