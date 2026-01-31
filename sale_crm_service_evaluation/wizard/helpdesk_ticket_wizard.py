# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, _
from odoo.exceptions import UserError


class HelpdeskTicketWizard(models.TransientModel):
    _name = "crm.lead.helpdesk.ticket.wizard"
    _description = "Create Helpdesk Ticket from CRM Lead"

    crm_lead_id = fields.Many2one(
        comodel_name="crm.lead",
        string="CRM Lead",
        required=True,
        ondelete="cascade",
    )
    team_id = fields.Many2one(
        comodel_name="helpdesk.team",
        string="Helpdesk Team",
        required=True,
    )

    def action_create_ticket(self):
        """Create a helpdesk ticket linked to the CRM lead."""
        self.ensure_one()
        lead = self.crm_lead_id
        if not lead.partner_id:
            raise UserError(_("The CRM lead must have a contact (partner) to create a ticket."))
        ticket = self.env["helpdesk.ticket"].create({
            "name": f"{lead.name} - {lead.partner_id.name}",
            "description": lead.description or "",
            "partner_id": lead.partner_id.id,
            "partner_name": lead.partner_id.name,
            "partner_email": lead.partner_id.email,
            "team_id": self.team_id.id,
            "crm_lead_id": lead.id,
        })
        return {
            "type": "ir.actions.act_window",
            "name": _("Helpdesk Ticket"),
            "view_mode": "form",
            "res_model": "helpdesk.ticket",
            "res_id": ticket.id,
            "target": "current",
        }
