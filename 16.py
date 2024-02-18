import requests
# try:
#     requests.get("vfdfv:cds//vdsdv")
#
# except BaseException as e:
#     print("something went wrong")
#     print(e.args)
#     print(e.with_traceback)

while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a/ b
        print(result)
        break
    except ValueError:
        print("enter a correct number: ")
    except ZeroDivisionError:
        print("Can't divide by zero")
    except BaseException as r:
        print(r.args)


