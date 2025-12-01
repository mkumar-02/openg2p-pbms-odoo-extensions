from odoo import models, fields
from datetime import date

class G2PRegistryWorker(models.Model):
    _name = "g2p.registry.worker"
    _description = "Registry Worker"
    _inherit = "g2p.registry"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Phone", required=True)

    province_id = fields.Integer(string="Province ID")
    district_id = fields.Integer(string="District ID")
    constituency_id = fields.Integer(string="Constituency ID")
    ward_id = fields.Integer(string="Ward ID")
    worker_age = fields.Integer(string="Worker Age")
    nature_of_employement = fields.Selection(
        selection=[("employee", "Employee"), ("self_employed", "Self Employed")],
    )
    months_without_job = fields.Integer(string="Months Without Job")
    duration_of_job_seeking = fields.Integer(string="Duration of Job Seeking")
    relocation_year = fields.Selection(
        selection=lambda self: [(str(year), str(year)) for year in range(1950, date.today().year + 1)][::-1],
    )
    duration_calculate = fields.Char(string="Duration Calculate")
    relocation_period_str = fields.Char(string="Relocation Period Str")
    relocation_month = fields.Integer()
    hh_has_disabilities = fields.Selection(
        selection=[("yes", "Yes"), ("no", "No")],
    )
    gender = fields.Selection(
        selection=[("male", "Male"), ("female", "Female")],
    )
    