# Example using map to square numbers
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))

print(squares)


# Example using filter to find even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)
