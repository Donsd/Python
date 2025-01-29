# lists
letters = ['a', 'b', 'c']
matrix = [[0, 1], [2, 3]]
zeros = [0]*10
print(zeros)
combined = zeros+letters
print(combined)
# in this list we can store different data types

# we can create 0 to 19 numbered list
numbers = list(range(20))
print(numbers)
chars = list("Hello world")
# also we can create character list using strings
print(chars)

#  accessing elements in list
print(letters[0])
letters[0] = 'A'
print(letters)


# list unpacking
numbers = [1, 2, 3]
first, second, third = numbers
print(first, second, third)
number = [1, 2, 3, 4, 5, 6, 7]
first, second, *other = number
print(other, first, second)
first, *other, last = number
print(first, other, last)
