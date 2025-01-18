temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink more water")
elif temperature > 20:
    print("It's nise ")
else:
    print("It's cold!")
print("Done")


# normal conditional statements
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

print(message)


# thernay operators
message = "Eligible" if age >= 18 else "Not eligible"
print(message)


# locical operators
# and, or ,not
high_income = True
good_credit = True

if high_income and good_credit:
    print('Eligible')
else:
    print('Not eligible')


# chaining comparison operators
age = 44
if 18 <= age < 65:
    print("You are eligible for this session")
