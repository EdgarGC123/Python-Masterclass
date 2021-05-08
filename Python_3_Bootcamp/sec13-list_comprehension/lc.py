numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)


name = "colt"
[char.upper() for char in name]
friends = ["ashley", "matt", "michael"]
updated_friends = [friend[0].upper() for friend in friends]
updated_friends2 = [friend.capitalize() for friend in friends]
print(updated_friends2)


print([num * 10 for num in range(1, 6)])
print([bool(val) for val in [0, [], ""]])

numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list)


numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
num2 = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]
print(num2)
print(evens)
print(odds)


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(val) for val in l] for l in nested_list]

board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)
board2 = [["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]
print(board2)
