text = " hello"
shift = 3
result = ""
for char in text:
    code = ord(char)

    if 65 <= code <= 90 or 97 <= code <= 122:
        new_code = 97 + (code - 97 + shift) % 26
        result += chr(new_code)
    else:
        result += char

print("Початкове слово ", text )
print("Зашифроване слово", result)

