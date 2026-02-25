def check_temperature(temp_str: str):
    temp_int = 0
    try:
        temp_int = int(temp_str)
        if temp_int >= 0 & temp_int <= 40:
            print(f"Testing temperature_ {temp_int}")
            print(f"Temperature {temp_int}ºC is perfect for plants!")
        else:
            if temp_int < 0:
                print(f"Testing temperature_ {temp_int}")
                print(f"Temperature {temp_str}ºC is too cold for plants"
                      " (min 0ºC)")
            elif temp_int > 40:
                print(f"Testing temperature_ {temp_int}")
                print(f"Temperature {temp_str}ºC is too hot for plants"
                      " (max 40ºC)")
    except TypeError:
        print(f"Testing temperature_ {temp_str}")
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    tests = ["25", "abc", "100", "-50"]
    for t in tests:
        check_temperature(t)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()