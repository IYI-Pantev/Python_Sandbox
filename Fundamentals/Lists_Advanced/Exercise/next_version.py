# You will be given a version as in this example: "1.3.4".
# You have to find the next version and print it ("1.3.5" from the example).

num = int(input().replace('.', '')) # string.replace(oldvalue, newvalue, count)

new_version = num + 1

print('.'.join(list(str(new_version)))) # list(iterabe)