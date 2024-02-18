# for i in range(5):
#     print("Hello "+ str(i))
#
# for i in range(10):
#     print("You are number " +str(i))

def my_printer(prefix, ammount_of_times):
    for i in range(ammount_of_times):
        print(prefix + str(i))

def mul_five(my_number):
    result = my_number*5
    return result

my_printer("Hello ",5)
my_printer("You are number ", 10)

print(mul_five(5))

