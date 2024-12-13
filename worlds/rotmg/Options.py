from dataclasses import dataclass

from typing import Dict

from Options import Choice, Option, Toggle, StartInventoryPool, DeathLink, PerGameCommonOptions


class LogicDifficulty(Choice):
    """Set the logic difficulty used when generating."""
    display_name = "Logic Difficulty"
    option_easy = 0
    #option_normal = 1
    #option_obscure_glitchless = 2
    #option_glitched = 3
    option_no_logic = 4
    default = 0


@dataclass
class RealmOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    logic_difficulty: LogicDifficulty
