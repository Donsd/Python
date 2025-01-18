for number in range(3):
    print("Attempt", number+1, (number + 1)*".")
for number in range(1, 4):
    print("Attempt", number, (number)*".")
for number in range(1, 10, 2):
    print("Attempt", number, (number)*".")

# for else
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times but didn't successful")
# else statement is worked when the for loop is completely worked
# when for loop break else statement is not work

# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# iterator
print(type(range(5)))
# range object is iterator. It is complex object type.
# strings,lists are also iterable objects


for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)


# while loops
number = 100
while number > 0:
    print(number)
    number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)


# exercise
for number in range(1, 10):
    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")
