from typing import NamedTuple, Callable, List, Dict
from BaseClasses import CollectionState


class RRRRRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, RRRRRegionData] = {
    "Menu": RRRRRegionData(["Nexus"]),
    "Nexus": RRRRRegionData(["Realm"]),
    "Realm": RRRRRegionData(["Pirate's Cave"]),
    "Pirate's Cave": RRRRRegionData([]),
}

def get_exit(region, exit_name):
    for exit in region.exits:
        if exit.connected_region.name == exit_name:
            return exit
