from typing import Callable, Dict

from BaseClasses import CollectionState, MultiWorld


def has_weapon(state, player):
    return True

def has_ability(state, player):
    return True


def get_region_rules(player):
    return {
        # ~ "Realm -> Pirate's Cave":
            # ~ lambda state: has_weapon(state, player) or has_ability(state, player),
    }

def get_location_rules(player):
    return {
        # ~ "Pirate's Cave Chest Item #1":
            # ~ lambda state: True,
        # ~ "Pirate's Cave Dreadstump #1":
            # ~ lambda state: has_weapon(state, player) and has_ability(state, player),
        # ~ "Pirate's Cave Dreadstump #2":
            # ~ lambda state: has_weapon(state, player) and has_ability(state, player),
        "Defeat Oryx":
            lambda state: True
    }
