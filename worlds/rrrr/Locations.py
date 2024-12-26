from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld


class RRRRLocation(Location):
    game = "Rocket Robot Recomp Rando"


class RRRRLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable = lambda options: True
    locked_item: Optional[str] = None


location_data_table: Dict[str, RRRRLocationData] = {
    # ~ "Link's Inventory (Kokiri Sword)": RRRRLocationData(
        # ~ region="Clock Town",
        # ~ address=0x3469420000037
    # ~ ),
    "First Ticket": RRRRLocationData(
        region="Pirate's Cave",
        address=0x1
    ),
    "Defeat Jojo": RRRRLocationData(
        region="Realm",
        locked_item="Victory"
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
code_to_location_table = {data.address: name for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
