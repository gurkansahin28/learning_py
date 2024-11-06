try:
    data = [1, 2, 3]
    print(data[5])  # This will raise an IndexError
except Exception as e:
    if isinstance(e, IndexError):
        print("Caught an IndexError: List index out of range.")
    elif isinstance(e, KeyError):
        print("Caught a KeyError: Key not found in dictionary.")
    else:
        print(f"An unexpected error occurred: {e}")