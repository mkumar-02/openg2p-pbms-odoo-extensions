from enum import Enum
from odoo import models, fields


class G2PTargetModelMapping:

    MODEL_MAPPING = {
        "farmer": "g2p.register.farmer",
        "households": "g2p.register.households",
        "individual": "g2p.register.individual",
        "household": "g2p.register.household",
    }

    # Physical tables in the connected Farmer / NSR database.
    # Both household types use g2p_register_households because PBMS points at
    # only one registry instance at a time.
    TABLE_MAPPING = {
        "farmer": "g2p_register_farmers",
        "households": "g2p_register_households",
        "individual": "g2p_register_individuals",
        "household": "g2p_register_households",
    }

    @classmethod
    def get_target_model_name(cls, key):
        return cls.MODEL_MAPPING.get(key)

    @classmethod
    def get_target_table_name(cls, key):
        return cls.TABLE_MAPPING.get(key)


class G2PRegistryType(Enum):
    FARMER = "farmer"
    HOUSEHOLDS = "households"
    INDIVIDUAL = "individual"
    HOUSEHOLD = "household"

    @classmethod
    def selection(cls):
        return [(member.value, member.name.replace("_", " ").title()) for member in cls]
