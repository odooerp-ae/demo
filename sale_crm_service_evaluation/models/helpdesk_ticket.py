# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, _


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    crm_lead_id = fields.Many2one(
        comodel_name="crm.lead",
        string="CRM Lead",
        ondelete="set null",
    )

    def action_create_project_task_wizard(self):
        """Open wizard to select project and create task."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Create Project Task"),
            "view_mode": "form",
            "res_model": "helpdesk.ticket.project.task.wizard",
            "target": "new",
            "context": {"default_ticket_id": self.id},
        }
