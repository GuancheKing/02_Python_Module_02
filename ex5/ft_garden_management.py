class GardenError(Exception):
    """
    Base exception for garden-related problems
    """
    pass


class NotAPlantError(GardenError):
    """
    Raised when a plant name is not registered in the manager
    """
    pass


class PlantError(GardenError):
    """
    Raised when there is a plant-related problem (e.g., empty name)
    """
    pass


class SunError(GardenError):
    """
    Raised when sunlight hours are out of range
    """
    pass


class WaterError(GardenError):
    """
    Raised when water level is out of range
    """
    pass


class Plant:
    """
    Stores plant status data.
    """
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """
    Manages plants by name and handles garden operations with custom errors
    """
    def __init__(self, owner: str, water_tank: int = 200) -> None:
        self.owner = owner
        self.plants: dict[str, Plant] = {}
        self.water_tank = water_tank

    def add_plant(self, plant: Plant) -> None:
        """
        Adds a plant to the manager, rejecting empty names
        """
        if not plant.name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[plant.name] = plant
        print(f"Added {plant.name} successfully")

    def watering(self, plant_name: str, water_amount: int) -> None:
        """
        Waters a plant by name and updates tank and plant levels
        """
        if plant_name not in self.plants:
            raise NotAPlantError(f"There isn't {plant_name} plant"
                                 " in the GardenManager")
        if self.water_tank < water_amount:
            raise GardenError("Not enough water in tank")
        self.water_tank -= water_amount
        self.plants[plant_name].water_level += water_amount

    def check_plant_health(self, plant_name: str) -> None:
        """
        Checks a plant by name and raises custom errors if
        values are out of range
        """
        if plant_name not in self.plants:
            raise NotAPlantError(f"There isn't {plant_name} plant"
                                 " in the GardenManager")
        plant = self.plants[plant_name]

        if not plant.name:
            raise PlantError("Plant name cannot be empty!")
        if plant.water_level > 10:
            raise WaterError(f"Water level {plant.water_level} is"
                             " too high (max 10)")
        if plant.water_level < 1:
            raise WaterError(f"Water level {plant.water_level} is"
                             " too low (min 1)")
        if plant.sunlight_hours > 12:
            raise SunError("Sunlight hours "
                           f"{plant.sunlight_hours} is"
                           " too high (max 12)")
        if plant.sunlight_hours < 2:
            raise SunError("Sunlight hours "
                           f"{plant.sunlight_hours} is too"
                           " low (min 2)")


def test_plant_checks() -> None:
    """
    Demonstrates a simple garden management system with error recovery
    """
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    manager = GardenManager("Pepo", water_tank=5)
    for plant in [
        Plant("tomato", 4, 8),
        Plant("lettuce", 14, 5),
        Plant("", 5, 8)
    ]:
        try:
            manager.add_plant(plant)
        except GardenError as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    print("Opening watering system")
    try:
        for name, amount in [
            ("tomato", 1),
            ("lettuce", 1),
        ]:
            try:
                manager.watering(name, amount)
                print(f"Watering {name} - success")
            except GardenError as e:
                print(f"Error watering {name}: {e}")
    finally:
        print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    for name in ["tomato", "lettuce"]:
        try:
            manager.check_plant_health(name)
            plant = manager.plants[name]
            print(f"{name}: healthy (water: {plant.water_level},"
                  f" sun: {plant.sunlight_hours})")
        except GardenError as e:
            print(f"Error checking {name}: {e}")

    print("\nTesting error recovery...")
    try:
        manager.watering("tomato", 101)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_plant_checks()
