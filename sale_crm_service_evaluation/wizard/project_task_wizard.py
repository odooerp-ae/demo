# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, _
from odoo.exceptions import UserError


class ProjectTaskWizard(models.TransientModel):
    _name = "helpdesk.ticket.project.task.wizard"
    _description = "Create Project Task from Helpdesk Ticket"

    ticket_id = fields.Many2one(
        comodel_name="helpdesk.ticket",
        string="Helpdesk Ticket",
        required=True,
        ondelete="cascade",
    )
    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
        required=True,
    )

    def action_create_task(self):
        """Create a project task linked to the helpdesk ticket and CRM lead."""
        self.ensure_one()
        ticket = self.ticket_id
        task_vals = {
            "name": f"{ticket.name}",
            "description": ticket.description,
            "project_id": self.project_id.id,
            "partner_id": ticket.partner_id.id if ticket.partner_id else False,
        }
        if ticket.crm_lead_id:
            task_vals["crm_lead_id"] = ticket.crm_lead_id.id
        task = self.env["project.task"].create(task_vals)
        return {
            "type": "ir.actions.act_window",
            "name": _("Project Task"),
            "view_mode": "form",
            "res_model": "project.task",
            "res_id": task.id,
            "target": "current",
        }
