from typing import NamedTuple, Callable, List, Dict
from BaseClasses import CollectionState


class RealmRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, RealmRegionData] = {
    "Menu": RealmRegionData(["Nexus"]),
    "Nexus": RealmRegionData(["Realm"]),
    "Realm": RealmRegionData([]),
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit
