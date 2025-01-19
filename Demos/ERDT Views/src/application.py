from client import DittoClient

from model import Truck


from model import Zone


ditto_client = DittoClient()


def get_active_trucks() -> list[Truck]:
    entities = ditto_client.query(Truck)
    matching_entities = []
    for entity in entities:
        if entity.get_status() == "active":
            matching_entities.append(entity)
    return matching_entities


def get_trucks_due_for_maintenance() -> list[Truck]:
    entities = ditto_client.query(Truck)
    matching_entities = []
    for entity in entities:
        if entity.getMaintenanceDetails().unresolved().count() > 0:
            matching_entities.append(entity)
    return matching_entities


def get_trucks_idle_for_15_min() -> list[Truck]:
    entities = ditto_client.query(Truck)
    matching_entities = []
    for entity in entities:
        if entity.getLast15MinLocations().unique().count() == 1:
            matching_entities.append(entity)
    return matching_entities


def get_trucks_inside_zone(zone: Zone) -> list[Truck]:
    entities = ditto_client.query(Truck)
    matching_entities = []
    for entity in entities:
        if zone.contains(entity.get_location()):
            matching_entities.append(entity)
    return matching_entities
