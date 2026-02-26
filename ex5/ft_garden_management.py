

class GardenError(Exception):
    """
    Base exception for garden-related problems.
    """
    pass


class NotAPlantError(GardenError):
    """
    Raised when a Plant is called by a method or function but it doesn't exists (yet)
    """
    pass


class PlantError(GardenError):
    """
    Raised when there is a plant-related problem such as name cannot be empty
    """
    pass


class SunError(GardenError):
    """
    Raised when there is a sun-related problem, too much sunlight or not enough
    """
    pass


class WaterError(GardenError):
    """
    Raised when there is a watering-related problem, too much or not enough water
    """
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = 0
        self.sunlight_hours = 0


class GardenManager:
    def __init__(self, owner: str, plants: dict[Plant], water_tank: int):
        self.owner = owner
        self.plants = {}
        self.water_tank = 200

    def add_plant(self, plant: Plant):
        self.plants[plant] = plant

    def watering(self, plant: Plant, water_plant: int) -> None:
        self.water_tank -= self.water_plant
        if not self.plants[plant]:
            raise NotAPlantError(f"There isn't {plant} plant in the GardenManager")
        self.plants[plant].water_level += self.water_plant

    def check_plant_health(
        self,
        plant: Plant,
    ) -> None:
        """
        Validates plant inputs and raises ValueError when values are out of range
        """
        if not self.plants[plant].plant_name:
            raise PlantError("Plant name cannot be empty!")
        if self.plants[plant].water_level > 10:
            raise WaterError(f"Water level {self.plants[plant].water_level} is"
                            " too high (max 10)")
        if self.plants[plant].water_level < 1:
            raise WaterError(f"Water level {self.plants[plant].water_level} is"
                            " too low (min 1)")
        if self.plants[plant].sunlight_hours > 12:
            raise SunError("Sunlight hours "
                            f"{self.plants[plant].sunlight_hours} is"
                            " too high (max 12)")
        if self.plants[plant].sunlight_hours < 2:
            raise SunError("Sunlight hours "
                            f"{self.plants[plant].sunlight_hours} is too"
                            " low (min 2)")
        if self.water_tank < 0:
            raise GardenError("Not enough water in tank")
        # print(f"Plant '{plant_name}' is healthy!")

def test_plant_checks() -> None:
    """
    Runs several plant health checks and prints results without crashing
    """
    print("\nAdding plants to garden...")
    plants = {}
    manager = GardenManager("Pepo", plants, 100)
    tomato = Plant("tomato", 5, 8)
    manager.add_plant(tomato)
    manager.add_plant("lettuce", 15, 5)
    manager.add_plant("", 5, 8)
    print("\nWatering plants...")
    manager.watering("tomato", 1)
    manager.watering("lettuce", 1)
    # manager.watering("lettuce", 100)
    print("Garden management system test complete!")

if __name__ == "__main__":
    print("=== Garden Management System ===")
    test_plant_checks()


