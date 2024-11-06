# Defining a custom exception class
class CustomError(Exception):
    pass

# Raising the custom exception
def check_positive(num):
    if num < 0:
        raise CustomError("Negative numbers are not allowed!")

try:
    check_positive(-5)
except CustomError as e:
    print(f"Custom exception caught: {e}")