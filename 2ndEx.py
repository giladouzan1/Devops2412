#Second Class - Exercise

#A
x = int(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))
if x > y:
    print("BIG")
elif x < y:
    print("Small")
else:
    print("X and Y are equal")

#B
for num in range(0,5):
    print(num)

#C
seasons = input("Enter a number between 1-4: ")
if int(seasons) == 1:
    print("Summer")
elif int(seasons) == 2:
    print("Winter")
elif int(seasons) == 3:
    print("fall")
elif int(seasons) == 4:
    print("Spring")
else:
    print("The number that you entered isn't between 1-4: ")

#D
# 10 times and 10 will be printed

#E
age = 24
fletter = "o"
currency = 3.60
flew_abroad = True
apartment_num = 41

print(age)
print(fletter)
print(currency)
print(flew_abroad)
print(apartment_num)
print(currency+age)

#F
phone_number = input("Please enter your phone number: ")
print("Phone Number:" + str(phone_number))

#G
def printHello():
    print("Hello")

def calculate():
    sum = 5+3.2
    print(sum)

#H
def receiveName(name):
    name = input("Please enter your name: ")
    print(name)

def divideBy2(number):
    number = input("Please enter a number: ")
    print(number/ 2)
#I
def sum(number1, number2):
     print(number1 + number2)

def twoStrings(string1, string2):
    print(string1 + " "+ string2)

#Challenges
def pyramid(rows):
    for row in range(1, rows + 1):
        for n in range(1, row + 1):
            if row == n:
                print("#" * n, end="")
        print("")


num_rows = int(input("Enter the number of rows for the pyramid: "))
pyramid(num_rows)


width = 7
length = 7

def xshape(width,length):
# Nested for loop to create X shape
    for i in range(length):
        for j in range(width):
            if i == j or i + j == width - 1:
                print("X", end="")
            else:
                print(" ", end="")
        print()

def ConvertRadiansIntoDegrees(radians):
    import math
    # Accessing the Pi constant from the math module
    pi_value = math.pi

    degrees = radians / (pi_value / 180)
    return degrees

print(ConvertRadiansIntoDegrees(1))


def SortAList(my_list,parameter):
    if parameter == "asc":
        sorted_list = sorted(my_list)
        return sorted_list
    elif parameter == "desc":
        descending_sorted_list = sorted(my_list, reverse=True)
        return descending_sorted_list
    elif parameter == "none":
        return my_list
    else:
        print("The parameter that you enter isn't correct, please enter a new one!")
        parameter = input("Please enter a list and a parameter(asc, desc, and none): ")

my_list = [1, 55, 34, 87, 2, 45, 66, 32, 34]
parameter = "desc"

print(SortAList(my_list, parameter))

def decimal_to_binary(decimal_number):
    # Check if the input is within the valid range
    if not (0 <= decimal_number < 1024):
        return "Error: Input must be a decimal number between 0 and 1023."

    # Convert decimal to binary using the bin() function and remove the '0b' prefix
    binary_representation = bin(decimal_number)[2:]
    return binary_representation

print(decimal_to_binary(13))

def countVowels(word):
    vowelsList = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in range(len(word)):
        if vowelsList[i] in word.lower():
            count += 1
    return count

print(countVowels("Gilad"))

def hideCreditCard(creditCardNum):
    resultNumbers = creditCardNum[-4:]
    return int(resultNumbers)

def XsEqualtoOs(word):
    countO = 0
    countX = 0
    for i in range(len(word)):
        if word[i].lower() == 'x':
            countX += 1
        elif word[i].lower() == 'o':
            countO += 1
    if countX == countO:
        return True
    else:
        return False

print(XsEqualtoOs("GOiladx"))

def calc(number1, operator,number2):
    if operator == '+':
        return  number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    else:
        print("The operator that you entered isn't correct, Please enter a new one")
        operator = input("Enter a new operator: ")

print(calc(7, '-',7 ))

def discount(full_price, discount_percentage):
    return full_price * (discount_percentage/100)

print(discount(250, 30))

def justTheNum(list):
    new_list = []
    j = 0
    for i in range(len(list)):
        if list[i] == int:
            new_list[j] = list[i]
            j += 1
    return new_list

my_list = [1,4, 'gffeg', 'efw', 54, 2, '%$', '43veve', 43]
print(justTheNum(my_list))

