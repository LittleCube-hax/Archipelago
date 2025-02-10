from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class RealmItem(Item):
    game = "Realm of the Mad God"


class RealmItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    num_exist: int = 1
    can_create: Callable = lambda options: True


item_data_table: Dict[str, RealmItemData] = {
    # ~ "Stray Fairy (Clock Town)": RealmItemData(
        # ~ code=0x1,
        # ~ type=ItemClassification.progression,
        # ~ can_create=lambda options: options.fairysanity.value
    # ~ ),
    "LittleCube": RealmItemData(
        code=0x310c,
        type=ItemClassification.progression,
        num_exist=13
    ),
    "Steel Dagger": RealmItemData(
        code=0xa14,
        type=ItemClassification.filler,
        num_exist=2
    ),
    "Victory": RealmItemData(
        type=ItemClassification.progression,
        can_create=lambda options: False
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
code_to_item_table = {data.code: name for name, data in item_data_table.items() if data.code is not None}
