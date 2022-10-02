print(bin(125).replace("0b", ""))

# bit at position formula

n = 125
p = 5 # position which we wanna check

bit = (n >> p) & 1

print(bit)