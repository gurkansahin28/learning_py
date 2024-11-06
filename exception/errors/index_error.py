try:
    my_list = [1, 2, 3]
    print(my_list[5])  # Raises IndexError (index out of range)
except IndexError as e:
    print("Caught an IndexError:", e)