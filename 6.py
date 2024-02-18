# For loops - basic syntax: just write for operator,
# add any variable, add in and the "Range" or the "List", etc

#For loop - by each
for i in range(5):
    print("Hello " + str(i))
else:
     print("Finished")

class_mate = ["Maksim", "Yoni", "Gilad", "Oren"]
for name in class_mate:
    if name == "Yoni":
        name = "Amir"
    print(name)

for i in range(len(class_mate)):
    print(class_mate[i])

#While loop
your_name = input("Enter your name: ")
while your_name != "Aviel":
    print("You are not Aviel")
    if your_name == "Haim":
        print("Oh my god")
        break
    if your_name == "David":
        print("Wow")
        continue
    your_name = input("Enter your name: ")