my_file = open("names.txt")
print(type(my_file))
for name in my_file.readlines():
    print(f"hello {name}", end='')


