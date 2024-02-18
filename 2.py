x = 1
if x == 2:
    print("x is 2")
my_name = input("Enter your name: ")
if my_name == "Gilad":
    print("Good!")

a = 4
b= 14
if a < b:
    print("a is lower")

fname = "Gilad"
lname = "Ouzan"

full_name = fname + "" + lname
another_full_name = "%s %s" % (fname, lname)
another_full_name2 = f"{fname} {lname}"
another_full_name3 = "{} {}".format(fname, lname)
print(my_full_description)
print(another_full_name3)