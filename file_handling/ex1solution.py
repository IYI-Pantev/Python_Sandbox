symbols = {"-", ",", ".", "!", "?"}

with open('text.txt', 'r') as file:
    idx = 0
    while True:
        line = file.readline().strip()
        if not line:
            break

        if idx % 2 != 0:
            idx += 1
            continue
        for symbol in symbols:
            line = line.replace(symbol, '@')
        reversed_line = ' '.join(line.split()[::-1])
        print(f"{idx} {reversed_line}")
        idx += 1
