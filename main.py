for elem in range(101):
    if elem % 3 == 0:
        if elem % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
        if elem % 5 == 0:
            print("Buzz")
        else:
            print(elem)
