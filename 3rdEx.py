#Third Class - Exercise
#1
# a = 1 / 0

#2
try:
    a = 1 / 0
except ZeroDivisionError:
    print("You can't divide a number by zero!")
# 3 - yes, youwill create x = 1 and then will print "finally"

#4 - we will catch all types of exceptions
#5 - this type is a genneral one, and we can't learn the details about the error that wer got
# we don't know how to take care of it properly
#6 - for 'IOError' exception - when we'll try to use input/output operators fails for some reasons
# for 'ZeroDivisionError' - when we try to divide by zero.

#7

my_file = open("words.txt", 'w')
my_file.close()

#8
my_file = open("words.txt", 'w')
my_file.write("Gilad Ouzan")
my_file.close()

#9
my_file = open("words.txt", 'r')
file = my_file.readlines()
print(file)
my_file.close()

#10
my_file = open("words.txt", 'a', encoding='utf-8')
my_file.write("\n")
my_file.writelines("גילעד אוזן")
my_file.close()

my_file = open("words.txt", 'r', encoding='utf-8')
file = my_file.readlines()
print(file)

#challenge
from PIL import Image, ImageDraw

def create_image():

    # Image sizes
    width, hight = 400, 400
    # BG color
    background_color = (160, 200, 150)
    image = Image.new("RGB", (width, hight),background_color)
    draw = ImageDraw.Draw(image)
    draw.rectangle((50, 50, 250, 150), fill=(160, 80, 96))
    image.save("image.png")

create_image()

