class GardenError(Exception):
    """
    Base exception for garden-related problems.
    """
    pass


class PlantError(GardenError):
    """
    Raised when there is a plant-related problem.
    """
    pass


class WaterError(GardenError):
    """
    Raised when there is a watering-related problem.
    """
    pass


def trigger_plant_error(plant_name: str) -> None:
    """
    Raises a PlantError for the given plant.
    """
    raise PlantError(f"The {plant_name} plant is wilting!")


def trigger_water_error() -> None:
    """
    Raises a WaterError when the tank is empty or insufficient
    """
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:

    print("=== Custom Garden Errors Demo ===\n")
    # PlantError
    try:
        print("Testing PlantError...")
        trigger_plant_error("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    # WaterError
    try:
        print("Testing WaterError...")
        trigger_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    # All Errors
    print("Testing catching all garden errors...")
    try:
        trigger_plant_error("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        trigger_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
