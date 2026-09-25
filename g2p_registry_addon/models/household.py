from odoo import models, fields

from .registry import G2PRegistry


class G2PRegisterHousehold(models.Model):
    """Farmer Registry household (farmer-registry 1.2)."""

    _name = "g2p.register.households"
    _description = "Farmer Register Household"
    _inherit = "g2p.registry"
    _table = "g2p_register_households"

    # G2PRegister fields
    functional_record_id = fields.Char(string="Functional Record ID", index=True)
    link_internal_record_id = fields.Char(string="Link Internal Record ID", index=True)
    link_foundational_id = fields.Char(string="Link Foundational ID", index=True)
    record_name = fields.Char(string="Record Name")
    record_image_storage_id = fields.Text(string="Record Image Storage ID")
    created_by = fields.Char(string="Created By")
    created_at = fields.Datetime(string="Created At")
    last_approved_at = fields.Datetime(string="Last Approved At")
    last_approved_by = fields.Char(string="Last Approved By")
    search_text = fields.Text(string="Search Text")
    record_status = fields.Selection(
        selection=[
            ("active", "Active"),
            ("inactive", "Inactive"),
            ("archived", "Archived"),
        ],
        string="Record Status",
        default="active",
    )
    record_status_reason = fields.Char(string="Record Status Reason")

    # G2PGeo fields
    latitude = fields.Char(string="Latitude")
    longitude = fields.Char(string="Longitude")
    altitude = fields.Char(string="Altitude")
    plus_code = fields.Char(string="Plus Code", index=True)
    address_line_1 = fields.Char(string="Address Line 1")
    address_line_2 = fields.Char(string="Address Line 2")
    postal_code = fields.Char(string="Postal Code", index=True)
    country_code = fields.Char(string="Country Code", index=True)
    geo_lowest_level_value_id = fields.Char(string="Geo Lowest Level Value ID", index=True)
    geo_code_hierarchy_json = fields.Json(string="Geo Code Hierarchy")

    # Farmer household domain (farmer-registry 1.2)
    household_head = fields.Char(string="Household Head")
    size_of_group = fields.Integer(string="Size of Group")
    number_of_children = fields.Integer(string="Number of Children")
    number_of_elderly_members = fields.Integer(string="Number of Elderly Members")
    number_of_female_members = fields.Integer(string="Number of Female Members")
    number_of_male_members = fields.Integer(string="Number of Male Members")
    other_land_owner = fields.Boolean(string="Other Land Owner")
