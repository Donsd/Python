def greet():
    print("Hi there")
    print("Welcome aboard")


greet()


# parameterized function
def greet1(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet1("shashanka", "denuwan")
# these are arguments


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Mosh")
print(message)
# all function returns None by default. If function have return something then it will return that thing


def increament(number, by):
    return number + by


print(increament(2, by=3))
# by = 3 is keyword argument


# default parameters
def increment(number, by=1):
    return number + by
    # all default parameters must be in end of the parameters list


print(increment(2))


# variabel number of arguments

def multiply(*numbers):  # if we want to give list of same parameters we can use *
    print(numbers)  # arguments are get as tuple (it is like list but it can't change)
    total = 1
    for number in numbers:
        total += number
    print(total)


multiply(2, 3, 4, 5)

# get dictionary as argument


def save_user(**user):
    print(user)  # this is get as a dictionary
    print("ID of the user: ", user["id"])


save_user(id=1, name="John", age=22)

# variables which are inside of the function are called local variable. It can access only inside of the function
# variables which are outside of the functions are called global variable.It can access anywhere
# same named local variable and global variable are different. when we call the variable.It gives value of global variable
message = 'a'


def greet_local(name):
    message = 'b'


greet_local("shashanka")
print(message)

# if we want to change value to local variable value we want to use global keyword.It is a bad practice


def greet_global(name):
    global message
    message = 'b'


greet_global("shashanka")
print(message)
