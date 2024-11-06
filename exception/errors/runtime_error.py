try:
    raise RuntimeError("Something went wrong.")  # Raises RuntimeError
except RuntimeError as e:
    print("Caught a RuntimeError:", e)