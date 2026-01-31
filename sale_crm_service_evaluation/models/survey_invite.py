# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SurveyInvite(models.Model):
    _inherit = "survey.invite"

    crm_lead_id = fields.Many2one(
        comodel_name="crm.lead",
        string="CRM Lead",
        ondelete="set null",
    )

    def _prepare_answers(self, partners, emails):
        answers = super()._prepare_answers(partners, emails)
        if self.crm_lead_id:
            answers.write({"crm_lead_id": self.crm_lead_id.id})
        return answers
