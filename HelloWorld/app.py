import math
print("hello world!")
print("*"*10)
x = 1
y = 1
unit_price = 3
d = 10
print("Hello word", d, x)
course = "Programming Language"
print(len(course))
print(course[0:12])
print(course[-2])

courese_1 = 'python "language'
courese_2 = "python \"language"
# \"
# \'
# \n
# \\
print(courese_1)
print(courese_2)

first = "mosh"
second = "Hamedani"
full = first+" "+second
full1 = f"{first} {second}"
print(full)
print(full1)

course = "   Python Programming   "
print(course.upper())
print(course.lower())
print(course.strip())
print(course.find("Pro"))  # find method output index of the character
print(course.replace("P", "j"))
print("Pro" in course)  # this is return thruth of the expression
print("swift" not in course)  # this is return thruth of the expression
# course.upper() is a method of the strings. It means different function of do on the strings
# this methods don't affect to the original string variable

#  numbers
x = 1
x = 1.1
x = 1+2j
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)


x = x+3
x += 3
print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))


# x = input("x: ")
# y = int(x)+1
# print(f"this is value of x: {x} and value of y: {y}")


print(bool(""))
print(bool("False"))

# falsy expression := "", 0 , None
# truth expression := others

print("this is a comparison operators")
# comparison operators
print(10 > 2)
print(10 < 2)
print(10 >= 2)
print(10 <= 2)
print(10 == 2)
print(10 != 2)
print(10 == "10")

print("this is string comparison operators")
# string comparison
print("bag" > "apple")
print("bag" == "BAG")
print(ord("b"))
