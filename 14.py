def add3names():
    names = []
    for i in range(3):
        name = input(f"Enter  name {i + 1}:")
        names.append(f"{name} \n")

    # Write the names to a file
    my_file = open("names.txt", "a+")
    my_file.writelines(names)
    my_file.close()

def printnames():
    my_names = open("names.txt", "r")
    for name in my_names.readlines():
        print(f"hello {name}", end='')

add3names()
printnames()

