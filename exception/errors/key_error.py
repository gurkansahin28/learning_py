try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])  # Raises KeyError (key not found)
except KeyError as e:
    print("Caught a KeyError:", e)