def equal(numbers, n):
    target = 0
    for num in numbers:
        if num == n:
            target += 1
    
    print (target)

equal([1, 2, 3, 2, 2, 4], 2)  # should return 3