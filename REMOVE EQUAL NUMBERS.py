def remove(numbers):
    list = []
    for n in numbers:
        if n not in list:
            list.append(n)
    print(list)

remove([1, 2, 2, 3, 3, 4])  # should return [1, 2, 3, 4]