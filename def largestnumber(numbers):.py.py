def largestnumber(numbers):
    largest = numbers[0]  # assume first number is largest
    for num in numbers:
        if num > largest:
            largest = num  # update if you find something bigger
            print(num)
    numbers([3, 7, 1, 9, 4]) 
  