a = 50
b = 10
my_name = "Gilad"

if a < 10:
    print("You are Gilad")
elif my_name == "Gilad":
    print("Found your name")
elif b > 5:
    print("B is good")
else:
    print("Halbala")
my_list = ["or", "shahar", "adam"]
my_other_name = "or"

# I can use only IN operator for solving problem without loops
if my_other_name in my_list:
    print("I found you")

# IS, an operator that checking the same "ID" and return True or False
tt = 50
rr = 50
print(tt is rr)