def check_temperature(temp_str: str):
    print(f"Testing temperature: {temp_str}")
    temp_int = 0
    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    if 0 <= temp_int <= 40:
        print(f"Temperature {temp_int}°C is perfect for plants!\n")
    elif temp_int < 0:
        print(f"Error: {temp_str}ºC is too cold for plants"
              " (min 0ºC)\n")
    elif temp_int > 40:
        print(f"Error {temp_str}ºC is too hot for plants"
              " (max 40ºC)\n")


def test_temperature_input():
    tests = ["25", "abc", "100", "-50"]
    print("=== Garden Temperature Checker ===\n")
    for t in tests:
        check_temperature(t)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
