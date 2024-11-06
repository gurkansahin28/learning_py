try:
    result = 10 / 0  # Raises ZeroDivisionError
except ZeroDivisionError as e:
    print("Caught a ZeroDivisionError:", e)