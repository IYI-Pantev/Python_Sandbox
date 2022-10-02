n = int(input("Enter number: "))

binary_digit = int(input("Enter 1 or 0: "))

# Function to convert Decimal number
# to Binary number - returns as string with 0b prefix!
def decimalToBinary(num):
    return bin(num).replace("0b", "")

deciamal_number = decimalToBinary(n)

counted = deciamal_number.count(str(binary_digit))

if binary_digit == 0:
    print(f"We have {counted} zeroes")
else:
    print(f"We have {counted} ones")


