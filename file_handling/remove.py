import os

if os.path.exists('my_first_file.txt'):
    os.remove("my_first_file.txt")
    print("file removed")
else:
    print("Path not found")

print(os.listdir("."))  # shows whats in the current directory
