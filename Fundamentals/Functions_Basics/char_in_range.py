def get_char_in_range(start_char, end_char):
    start_int = ord(start_char)
    end_int = ord(end_char)

    chars = []

    for num in range(start_int + 1, end_int):
        chars.append(chr(num))

    return chars


char1 = input()
char2= input()

result = get_char_in_range(char1, char2)


print(" ".join(result))
