try:
    result = "text" + 5  # Raises TypeError (cannot add str and int)
except TypeError as e:
    print("Caught a TypeError:", e)