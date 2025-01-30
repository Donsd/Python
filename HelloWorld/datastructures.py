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
print(first, second, third)  # 1 2 3
number = [1, 2, 3, 4, 5, 6, 7]
first, second, *other = number
print(other, first, second)   # [3,4,5,6,7] 1 2
first, *other, last = number
print(first, other, last)  # 1 [2,3,4,5,6] 7


for letter in letters:
    print(letter)
for index, letter in enumerate(letters):
    # print(letter)
    print(index, letter)
    # in this case return tuple.It is like list but we can change the values

# add elements
letters.append('d')
print(letters)
letters.insert(0, '-')
print(letters)

# remove elements
letters.pop()  # remove last element
print(letters)
letters.remove('A')  # remove first occurance of 'A'
print(letters)
del letters[0:2]  # remove first two elements
print(letters)

# find elements
letters = ['a', 'b', 'c']
if 'd' in letters:
    print(letters.index('d'))  # return index of 'd'

# sorting elements
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)


# different data stuctures we can use varias method to handle
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)
items.sort(key=lambda item: item[1])
print(items)


# mapping
prices = []
for item in items:
    prices.append(item[1])
print(prices)
# using map function
x = map(lambda item: item[1], items)
print(x)  # it is a map object
for item in x:
    print(item)

y = list(map(lambda item: item[1], items))
print(y)
# list comprehension. It is more readable and easy to understand than map function
s = [item[1] for item in items]
print(s)

# filter elements
z = list(filter(lambda item: item[1] >= 10, items))
print(z)
r = [item for item in items if item[1] >= 10]
print(r)  # `list comprehension. It is more readable and easy to understand than filter function


list1 = [1, 2, 3]
list2 = [10, 20, 30]

# zip function
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
print(list(zip('abc', list1, list2)))
