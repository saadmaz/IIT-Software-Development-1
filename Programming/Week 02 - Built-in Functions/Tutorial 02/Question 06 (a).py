try:
    n = input("Please enter an integer: ")
    n = int(n)
    print(n)
except ValueError:
    print("Requires a valid integer!")
