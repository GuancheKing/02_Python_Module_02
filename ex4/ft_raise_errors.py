def check_plant_health(
        plant_name: str,
        water_level: int,
        sunlight_hours: int
) -> None:
    """
    Validates plant inputs and raises ValueError when values are out of range
    """
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is"
                         " too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is"
                         " too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too"
                         " high (max 12)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too"
                         " low (min 2)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Runs several plant health checks and prints results without crashing
    """
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 7, 7)
    except ValueError as e:
        print(e)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 7, 7)
    except ValueError as e:
        print(e)
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 7)
    except ValueError as e:
        print(e)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 7, 0)
    except ValueError as e:
        print(e)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
