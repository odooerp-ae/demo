# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    crm_lead_id = fields.Many2one(
        comodel_name="crm.lead",
        string="CRM Lead",
        ondelete="set null",
    )
