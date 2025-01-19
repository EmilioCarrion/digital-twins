from dataclasses import dataclass
from shapely import Polygon, Point
### Value Sets


@dataclass
class Zone:
    vertices: list[tuple[float, float]]

    def contains(self, coordinate):
        return Polygon(self.vertices).contains(Point(coordinate))


@dataclass
class MaintenanceDetail:
    status: str


class MaintenanceDetails(list[MaintenanceDetail]):
    def unresolved(self) -> "MaintenanceDetails":
        return MaintenanceDetails(
            [item for item in self if item.status == "unresolved"]
        )

    def count(self) -> int:
        return len(self)


class LocationHistory(list[tuple[float, float]]):
    def unique(self) -> "LocationHistory":
        return LocationHistory(set(self))

    def count(self) -> int:
        return len(self)


### Entities


@dataclass
class Truck:
    thing_id: str
    latitude: float
    longitude: float
    status: str

    @classmethod
    def from_ditto(cls, ditto_entity) -> "Truck":
        return cls(
            thing_id=ditto_entity["thingId"],
            latitude=ditto_entity["attributes"]["latitude"],
            longitude=ditto_entity["attributes"]["longitude"],
            status=ditto_entity["attributes"]["status"],
        )

    def get_status(self) -> str:
        return self.status

    def get_location(self) -> tuple[float, float]:
        return (self.latitude, self.longitude)

    def getMaintenanceDetails(self) -> MaintenanceDetails:
        # Search for maintenance details in db
        return MaintenanceDetails()

    def getLast15MinLocations(self) -> LocationHistory:
        # Search for history in db
        return LocationHistory()
