class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error!")  # Raises CustomError
except CustomError as e:
    print("Caught a CustomError:", e)