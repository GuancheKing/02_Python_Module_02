class InvalidError(Exception):
    """
    Custom error for invalid plant
    """
    pass


def water_plants(plant_list: list) -> None:
    """
    Waters all plants in the list and ensures cleanup with finally.
    """
    error_track = False
    print("Opening watering system")
    try:
        for p in plant_list:
            if p is None:
                raise InvalidError(f"{p} - invalid plant")
            water(p)
    except InvalidError as e:
        print(f"Error: Cannot water {e}")
        error_track = True
    finally:
        print("Closing watering system (cleanup)")
    if not error_track:
        print("Watering completed successfully!")


def water(plant: str) -> None:
    """
    Prints watering message for a plant.
    """
    print(f"Watering {plant}")


def test_watering_system() -> None:
    """
    Tests normal and error scenarios for the watering system.
    """
    normal_list = ["tomato", "lettuce", "carrots"]
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    water_plants(normal_list)
    error_list = ["tomato", None]
    print("\nTesting with error...")
    water_plants(error_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
