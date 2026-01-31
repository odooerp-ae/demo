# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmInquiryLine(models.Model):
    _name = "crm.inquiry.line"
    _description = "CRM Inquiry Line"

    question = fields.Text(string="Question", required=True)
    resolution = fields.Text(string="Resolution")
    status = fields.Selection(
        selection=[
            ("ongoing", "Ongoing"),
            ("closed", "Closed"),
        ],
        string="Status",
        default="ongoing",
        required=True,
    )
    crm_lead_id = fields.Many2one(
        comodel_name="crm.lead",
        string="CRM Lead",
        required=True,
        ondelete="cascade",
    )
