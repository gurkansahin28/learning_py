try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()  # Raises FileNotFoundError
except FileNotFoundError as e:
    print("Caught a FileNotFoundError:", e)