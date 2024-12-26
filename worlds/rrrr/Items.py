from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class RRRRItem(Item):
    game = "Rocket Robot Recomp Rando"


class RRRRItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable = lambda options: True


item_data_table: Dict[str, RRRRItemData] = {
    # ~ "Stray Fairy (Clock Town)": RRRRItemData(
        # ~ code=0x1,
        # ~ type=ItemClassification.progression,
        # ~ can_create=lambda options: options.fairysanity.value
    # ~ ),
    "Ticket A": RRRRItemData(
        code=0x1,
        type=ItemClassification.progression
    ),
    "Token (1)": RRRRItemData(
        code=0x2,
        type=ItemClassification.filler,
        can_create=lambda options: False
    ),
    "Victory": RRRRItemData(
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
code_to_item_table = {data.code: name for name, data in item_data_table.items() if data.code is not None}
