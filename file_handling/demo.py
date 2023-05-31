file = open('x.py', 'r')
print(file.read())
file.close()

file = open('sample_x.py', 'w')
file.write('# some demonstration')
file.close()