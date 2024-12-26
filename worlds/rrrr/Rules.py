from typing import Callable, Dict

from BaseClasses import CollectionState, MultiWorld


def has_weapon(state, player):
    return True

def has_ability(state, player):
    return True


def get_region_rules(player):
    return {
        "Realm -> Pirate's Cave":
            lambda state: has_weapon(state, player) or has_ability(state, player),
    }

def get_location_rules(player):
    return {
        "Ticket A":
            lambda state: True,
        "Defeat Jojo":
            lambda state: state.has("Ticket A", player)
    }
