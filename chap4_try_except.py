try:
    a = input("Type a number:")
    b = input("Type another:")

    a = int(a)
    b = int(b)

    print(a / b)

except ZeroDivisionError:
    print("Please do not input \"0\" at second input.")

except ValueError:
    print("Please input numbers.  Characters are not allowed.")