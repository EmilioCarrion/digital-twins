from dataclasses import dataclass
from fastapi import FastAPI, Request, HTTPException

from application import get_active_trucks

from application import get_trucks_due_for_maintenance

from application import get_trucks_idle_for_15_min

from application import get_trucks_inside_zone


from model import Truck


from model import Zone


from security import has_permission

app = FastAPI()


@app.post("/get_active_trucks")
async def get_active_trucks_view(
    request: Request,
) -> list[Truck]:
    if not has_permission(request.client.host, "Truck::get_status"):
        raise HTTPException(status_code=403, detail="Permission denied")

    entities = get_active_trucks()
    return entities


@app.post("/get_trucks_due_for_maintenance")
async def get_trucks_due_for_maintenance_view(
    request: Request,
) -> list[Truck]:
    if not has_permission(request.client.host, "Role::MaintenanceStaff"):
        raise HTTPException(status_code=403, detail="Permission denied")

    entities = get_trucks_due_for_maintenance()
    return entities


@app.post("/get_trucks_idle_for_15_min")
async def get_trucks_idle_for_15_min_view(
    request: Request,
) -> list[Truck]:
    if not has_permission(request.client.host, "Role::FleetManager"):
        raise HTTPException(status_code=403, detail="Permission denied")

    entities = get_trucks_idle_for_15_min()
    return entities


@app.post("/get_trucks_inside_zone")
async def get_trucks_inside_zone_view(request: Request, zone: Zone) -> list[Truck]:
    if not has_permission(request.client.host, "Truck::get_location"):
        raise HTTPException(status_code=403, detail="Permission denied")

    entities = get_trucks_inside_zone(zone)
    return entities
