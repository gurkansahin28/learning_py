try:
    num = 5
    num.append(3)  # Raises AttributeError (int has no 'append' method)
except AttributeError as e:
    print("Caught an AttributeError:", e)