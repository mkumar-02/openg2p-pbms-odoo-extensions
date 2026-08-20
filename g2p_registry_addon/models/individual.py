from odoo import models, fields

from .registry import G2PRegistry


class G2PRegisterIndividual(models.Model):
    _name = "g2p.register.individual"
    _description = "NSR Individual"
    _inherit = "g2p.registry"
    _table = "g2p_register_individuals"

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

    # G2PPerson fields
    foundational_id = fields.Char(string="Foundational ID", index=True)
    first_name = fields.Char(string="First Name")
    middle_name = fields.Char(string="Middle Name")
    last_name = fields.Char(string="Last Name")
    given_name = fields.Char(string="Given Name")
    prefix = fields.Char(string="Prefix")
    suffix = fields.Char(string="Suffix")
    gender = fields.Selection(
        selection=[
            ("MALE", "Male"),
            ("FEMALE", "Female"),
            ("OTHERS", "Others"),
            ("UNKNOWN", "Unknown"),
        ],
        string="Gender",
    )
    birth_date = fields.Date(string="Birth Date")
    phone_numbers = fields.Json(string="Phone Numbers")
    emails = fields.Json(string="Emails")
    marital_status = fields.Selection(
        selection=[
            ("SINGLE", "Single"),
            ("MARRIED", "Married"),
            ("DIVORCED", "Divorced"),
            ("WIDOWED", "Widowed"),
            ("SEPARATED", "Separated"),
            ("UNKNOWN", "Unknown"),
        ],
        string="Marital Status",
    )
    occupation = fields.Char(string="Occupation")
    income_level = fields.Char(string="Income Level")
    language_code = fields.Char(string="Language Code")
    registration_date = fields.Date(string="Registration Date")

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

    # NSR Individual – identity & evidence
    foundational_id_masked = fields.Char(string="Foundational ID (Masked)")
    foundational_id_verification_status = fields.Selection(
        selection=[
            ("VERIFIED", "Verified"),
            ("PENDING", "Pending"),
            ("FAILED", "Failed"),
            ("EXCEPTION", "Exception"),
        ],
        string="Foundational ID Verification Status",
    )
    identity_evidence_type = fields.Selection(
        selection=[
            ("FOUNDATIONAL_ID_VERIFIED", "Foundational ID Verified"),
            ("DOCUMENT", "Document"),
            ("NONE", "None"),
            ("EXCEPTION", "Exception"),
        ],
        string="Identity Evidence Type",
    )
    legacy_program_ids = fields.Json(string="Legacy Program IDs")

    # Names
    full_name = fields.Char(string="Full Name", index=True)
    alias_names = fields.Json(string="Alias Names")

    # Demographics
    estimated_age = fields.Integer(string="Estimated Age")
    age_method = fields.Selection(
        selection=[
            ("DOCUMENTED", "Documented"),
            ("ESTIMATED", "Estimated"),
        ],
        string="Age Method",
    )
    citizenship_category = fields.Selection(
        selection=[
            ("CITIZEN", "Citizen"),
            ("REFUGEE", "Refugee"),
            ("IDP", "IDP"),
            ("RETURNEE", "Returnee"),
            ("RESIDENT", "Resident"),
        ],
        string="Citizenship Category",
    )

    # Household membership
    relationship_to_head = fields.Selection(
        selection=[
            ("SELF", "Self"),
            ("SPOUSE", "Spouse"),
            ("CHILD", "Child"),
            ("PARENT", "Parent"),
            ("SIBLING", "Sibling"),
            ("OTHER_RELATIVE", "Other Relative"),
            ("NON_RELATIVE", "Non Relative"),
        ],
        string="Relationship to Head",
    )
    residency_status = fields.Selection(
        selection=[
            ("USUAL_MEMBER", "Usual Member"),
            ("TEMPORARY", "Temporary"),
            ("ABSENT", "Absent"),
        ],
        string="Residency Status",
    )
    dependency_indicator = fields.Boolean(string="Dependency Indicator")

    # Contact
    preferred_contact_method = fields.Selection(
        selection=[
            ("CALL", "Call"),
            ("SMS", "SMS"),
            ("VIA_LOCAL_OFFICE", "Via Local Office"),
            ("NONE", "None"),
        ],
        string="Preferred Contact Method",
    )
    contact_person_name = fields.Char(string="Contact Person Name")

    # Vulnerability & inclusion
    disability_status = fields.Selection(
        selection=[
            ("YES", "Yes"),
            ("NO", "No"),
            ("UNKNOWN", "Unknown"),
        ],
        string="Disability Status",
    )
    plw_status = fields.Boolean(string="PLW Status")
    plw_status_date = fields.Date(string="PLW Status Date")
    orphanhood_flag = fields.Boolean(string="Orphanhood Flag")
    chronic_illness_flag = fields.Boolean(string="Chronic Illness Flag")
    displacement_status = fields.Selection(
        selection=[
            ("HOST_COMMUNITY", "Host Community"),
            ("IDP", "IDP"),
            ("RETURNEE", "Returnee"),
            ("REFUGEE", "Refugee"),
        ],
        string="Displacement Status",
    )
    pastoralist_classification = fields.Selection(
        selection=[
            ("PASTORALIST", "Pastoralist"),
            ("SEMI_PASTORALIST", "Semi-Pastoralist"),
            ("SETTLED", "Settled"),
        ],
        string="Pastoralist Classification",
    )
    high_mobility_indicator = fields.Boolean(string="High Mobility Indicator")

    # Livelihood
    primary_livelihood = fields.Selection(
        selection=[
            ("AGRICULTURE", "Agriculture"),
            ("LIVESTOCK", "Livestock"),
            ("FISHING", "Fishing"),
            ("WAGE_LABOR", "Wage Labor"),
            ("SELF_EMPLOYMENT", "Self Employment"),
            ("GOVERNMENT_EMPLOYEE", "Government Employee"),
            ("PRIVATE_SECTOR_EMPLOYEE", "Private Sector Employee"),
            ("BUSINESS_TRADE", "Business / Trade"),
            ("REMITTANCE", "Remittance"),
            ("PENSION", "Pension"),
            ("UNEMPLOYED", "Unemployed"),
            ("OTHER", "Other"),
        ],
        string="Primary Livelihood",
    )
    secondary_livelihood = fields.Selection(
        selection=[
            ("AGRICULTURE", "Agriculture"),
            ("LIVESTOCK", "Livestock"),
            ("FISHING", "Fishing"),
            ("WAGE_LABOR", "Wage Labor"),
            ("SELF_EMPLOYMENT", "Self Employment"),
            ("GOVERNMENT_EMPLOYEE", "Government Employee"),
            ("PRIVATE_SECTOR_EMPLOYEE", "Private Sector Employee"),
            ("BUSINESS_TRADE", "Business / Trade"),
            ("REMITTANCE", "Remittance"),
            ("PENSION", "Pension"),
            ("UNEMPLOYED", "Unemployed"),
            ("OTHER", "Other"),
        ],
        string="Secondary Livelihood",
    )
    employment_status = fields.Selection(
        selection=[
            ("EMPLOYED", "Employed"),
            ("SELF_EMPLOYED", "Self Employed"),
            ("UNEMPLOYED", "Unemployed"),
            ("STUDENT", "Student"),
            ("RETIRED", "Retired"),
            ("OTHER", "Other"),
        ],
        string="Employment Status",
    )
    coping_strategies_index = fields.Integer(string="Coping Strategies Index")
