def garden_operations(error_type: str) -> None:
    """
    Triggers specific common Python errors depending on error_type.
    """
    if error_type == "value":
        int("abc")  # ValueError
    elif error_type == "zero":
        88 / 0  # ZeroDivisionError
    elif error_type == "file":
        filename = "missing.txt"
        open(filename, "r")  # FileNotFoundError
    elif error_type == "key":
        plants = {"cucumber": 18}
        plants["missing\\_plant"]  # KeyError
    # else:
    #    raise ValueError(f"Unknown error_type: {error_type}")


def test_error_types() -> None:
    """
    Tests and handles different Python error types without crashing.
    """
    print("=== Garden Error Types Demo ===")
    # ValueError
    print("\nTesting ValueError....")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    # ZeroDivisionError
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    # FileNotFoundError
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    # KeyError
    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    # Multiple errors
    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
        garden_operations("zero")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
