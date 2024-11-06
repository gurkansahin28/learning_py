try:
    import non_existent_module  # Raises ModuleNotFoundError
except ModuleNotFoundError as e:
    print("Caught a ModuleNotFoundError:", e)