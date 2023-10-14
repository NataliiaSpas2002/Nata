# Topic 10
# Task 1
def oops():
    raise IndexError("This is an IndexError")
def catch_error():

    try:
        oops()
    except IndexError as e:
        print(f"Caught an IndexError: {e}")
    except Exception as e:
        print(f"Caught an exception: {e}")

print(catch_error())

def more_positive():
    try:
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = (a ** 2) / b
        return result
    except ValueError as e:
        print(f"Error: {e}")
        return None

result = more_positive()
print(result)