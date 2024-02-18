#dictionary examples


detelis = ["Gilad", "Ouzan", 24, True]
detelis_dict = {"fname": "Gilad",
                "lname": "Ouzan",
                "age": 34,
                "is_married": False}

my_class = [
    {"fname": "Gilad", "lname": "Ouzan"},
    {"fname": "Asaf", "lname": "cohen"}
]

for student in my_class:
    print(student["fname"] + " " + student["lname"])

print(detelis_dict.keys())
print(detelis_dict.values())

