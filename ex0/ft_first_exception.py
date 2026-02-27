def check_temperature(temp_str: str) -> int:
    """
    Convert string to int and check if temperature is valid for plants.

    Prints error if invalid or out of range (0–40°C).
    """
    print(f"Testing temperature: {temp_str}")
    temp_int = 0

    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    if 0 <= temp_int <= 40:
        print(f"Temperature {temp_str}°C is perfect for plants!\n")
        return temp_int
    elif temp_int < 0:
        print(f"Error: {temp_str}°C is too cold for plants"
              " (min 0°C)\n")
        return
    elif temp_int > 40:
        print(f"Error: {temp_str}°C is too hot for plants"
              " (max 40°C)\n")
        return


def test_temperature_input() -> None:
    """
    Run predefined test cases for check_temperature.

    Prints results to verify correct behavior.
    """
    tests = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")
    for t in tests:
        check_temperature(t)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
