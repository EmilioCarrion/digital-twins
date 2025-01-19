permissions = {
    "127.0.0.1": ["Truck::get_status", "Role::FleetManager", "Role::MaintenanceStaff"]
}


def has_permission(user: str, permission: str) -> bool:
    return permission in permissions[user]
