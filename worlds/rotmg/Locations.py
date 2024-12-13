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
    "Defeat Oryx": RealmLocationData(
        region="Realm",
        locked_item="Victory"
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
code_to_location_table = {data.address: name for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
