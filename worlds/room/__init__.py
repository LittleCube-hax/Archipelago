from typing import List
from typing import Dict

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import RoomItem, item_data_table, item_table
from .Locations import RoomLocation, location_data_table, location_table, locked_locations
from .Options import room_options
from .Regions import region_data_table
#from .Rules import get_button_rule


class RoomWebWorld(WebWorld):
    theme = "partyTime"
    
    setup_en = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to playing Room.",
        language="English",
        file_name="guide_en.md",
        link="guide/en",
        authors=["LittleCube"]
    )
    
    tutorials = [setup_en]


class RoomWorld(World):
    """A dynamic text-adventure."""

    game = "Room"
    data_version = 1
    web = RoomWebWorld()
    option_definitions = room_options
    location_name_to_id = location_table
    item_name_to_id = item_table

    def generate_early(self):
        pass
    
    def create_item(self, name: str) -> RoomItem:
        return RoomItem(name, item_data_table[name].type, item_data_table[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[RoomItem] = []
        item_pool_count: Dict[str, int] = {}
        for name, item in item_data_table.items():
            if name not in item_pool_count:
                item_pool_count[name] = 0
            if item.code and item.can_create(self.multiworld, self.player) and (item_pool_count[name] < item.num_exist):
                item_pool.append(self.create_item(name))
                item_pool_count[name] += 1

        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name and location_data.can_create(self.multiworld, self.player)
            }, RoomLocation)
            region.add_exits(region_data_table[region_name].connecting_regions)

        # Place locked locations.
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(self.multiworld, self.player):
                continue

            locked_item = self.create_item(location_data_table[location_name].locked_item)
            self.multiworld.get_location(location_name, self.player).place_locked_item(locked_item)

        # Set priority location for the Big Red Button!
        #self.multiworld.priority_locations[self.player].value.add("The Big Red Button")

    def get_filler_item_name(self) -> str:
        return "Mints"

    def set_rules(self) -> None:
        #button_rule = get_button_rule(self.multiworld, self.player)
        self.multiworld.get_location("Cabinet", self.player).access_rule = lambda state: state.has("A Small Key", self.player)
        #self.multiworld.get_location("In the Player's Mind", self.player).access_rule = button_rule

        # Do not allow button activations on buttons.
        #self.multiworld.get_location("The Big Red Button", self.player).item_rule =\
        #    lambda item: item.name != "Button Activation"

        # Completion condition.
        self.multiworld.completion_condition[self.player] = lambda state: state.has("A Trophy", self.player)

    def fill_slot_data(self):
        return {
            #"color": getattr(self.multiworld, "color")[self.player].current_key
        }
