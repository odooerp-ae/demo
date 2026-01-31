# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SurveySendWizard(models.TransientModel):
    _name = "crm.lead.survey.send.wizard"
    _description = "Send Survey from CRM Lead"

    crm_lead_id = fields.Many2one(
        comodel_name="crm.lead",
        string="CRM Lead",
        required=True,
        ondelete="cascade",
    )
    survey_id = fields.Many2one(
        comodel_name="survey.survey",
        string="Survey Template",
        required=True,
    )

    def action_send_survey(self):
        """Open the standard survey invite wizard with pre-filled data."""
        self.ensure_one()
        if not self.crm_lead_id.partner_id:
            raise UserError(_("The CRM lead must have a contact (partner) to send a survey."))
        template = self.env.ref("survey.mail_template_user_input_invite", raise_if_not_found=False)
        return {
            "type": "ir.actions.act_window",
            "name": _("Send Survey"),
            "view_mode": "form",
            "res_model": "survey.invite",
            "target": "new",
            "context": {
                "default_survey_id": self.survey_id.id,
                "default_partner_ids": [(6, 0, self.crm_lead_id.partner_id.ids)],
                "default_template_id": template.id if template else False,
                "default_email_layout_xmlid": "mail.mail_notification_light",
                "default_send_email": self.survey_id.access_mode == "token",
                "default_crm_lead_id": self.crm_lead_id.id,
            },
        }
