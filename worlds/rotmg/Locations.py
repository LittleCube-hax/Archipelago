from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld


class RealmLocation(Location):
    game = "Realm of the Mad God"


class RealmLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable = lambda options: True
    locked_item: Optional[str] = None


location_data_table: Dict[str, RealmLocationData] = {
    # ~ "Link's Inventory (Kokiri Sword)": RealmLocationData(
        # ~ region="Clock Town",
        # ~ address=0x3469420000037
    # ~ ),
    # ~ "Pirate's Cave Chest Item #1": RealmLocationData(
        # ~ region="Pirate's Cave",
        # ~ address=0x1
    # ~ ),
    # ~ "Pirate's Cave Dreadstump #1": RealmLocationData(
        # ~ region="Pirate's Cave",
        # ~ address=0x2
    # ~ ),
    # ~ "Pirate's Cave Dreadstump #2": RealmLocationData(
        # ~ region="Pirate's Cave",
        # ~ address=0x3
    # ~ ),
    "Apple 1": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E00,
    ),
    "Apple 2": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E01,
    ),
    "Apple 3": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E02,
    ),
    "Apple 4": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E03,
    ),
    "Apple 5": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E04,
    ),
    "Apple 6": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E05,
    ),
    "Apple 7": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E06,
    ),
    "Apple 8": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E07,
    ),
    "Apple 9": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E08,
    ),
    "Apple 10": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E09,
    ),
    "Apple 11": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E0A,
    ),
    "Apple 12": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E0B,
    ),
    "Apple 13": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E0C,
    ),
    "Apple 14": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E0D,
    ),
    "Apple 15": RealmLocationData(
        region="DA ALVIN ZONE",
        address=0x574E0E,
    ),
    "Defeat Oryx": RealmLocationData(
        region="Realm",
        locked_item="Victory"
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
code_to_location_table = {data.address: name for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
