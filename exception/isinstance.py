try:
    # Some code that may raise exceptions
    x = "123"
    result = int(x) / 0  # This will raise a ZeroDivisionError
except Exception as e:
    if isinstance(e, ZeroDivisionError):
        print("Caught a ZeroDivisionError: Cannot divide by zero.")
    elif isinstance(e, ValueError):
        print("Caught a ValueError: Invalid conversion.")
    else:
        print(f"An unexpected error occurred: {e}")