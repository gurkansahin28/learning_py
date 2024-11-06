try:
    num = int("not_a_number")  # Raises ValueError
except ValueError as e:
    print("Caught a ValueError:", e)