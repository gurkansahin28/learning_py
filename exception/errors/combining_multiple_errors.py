try:
    value = int("not_a_number")  # Raises ValueError
except (ValueError, TypeError) as e:
    print("Caught a ValueError or TypeError:", e)