# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HelpdeskStage(models.Model):
    _inherit = "helpdesk.stage"

    is_unsatisfactory = fields.Boolean(
        string="Unsatisfactory",
        default=False,
        help="When a ticket moves to this stage, a project task can be created.",
    )
