# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    service_evaluation = fields.Selection(
        selection=[
            ("satisfied", "Satisfied"),
            ("inquiry", "Inquiry"),
            ("unsatisfied", "Unsatisfied"),
        ],
        string="Service Evaluation",
        copy=False,
    )

    # Inquiry lines (when service_evaluation = inquiry)
    inquiry_line_ids = fields.One2many(
        comodel_name="crm.inquiry.line",
        inverse_name="crm_lead_id",
        string="Inquiry Lines",
    )

    # Helpdesk tickets (when service_evaluation = unsatisfied)
    helpdesk_ticket_ids = fields.One2many(
        comodel_name="helpdesk.ticket",
        inverse_name="crm_lead_id",
        string="Helpdesk Tickets",
    )

    # Survey responses (when service_evaluation = satisfied)
    survey_user_input_ids = fields.One2many(
        comodel_name="survey.user_input",
        inverse_name="crm_lead_id",
        string="Survey Responses",
    )

    # Project tasks (created from helpdesk when ticket goes to unsatisfactory)
    task_ids = fields.One2many(
        comodel_name="project.task",
        inverse_name="crm_lead_id",
        string="Project Tasks",
    )

    # Sale order lines (computed from order_ids for display in notebook)
    sale_order_line_ids = fields.Many2many(
        comodel_name="sale.order.line",
        string="Sale Order Lines",
        compute="_compute_sale_order_line_ids",
        help="Order lines from linked sale orders",
    )

    @api.depends("order_ids", "order_ids.order_line")
    def _compute_sale_order_line_ids(self):
        for lead in self:
            lead.sale_order_line_ids = lead.order_ids.mapped("order_line")

    def action_send_survey_wizard(self):
        """Open wizard to select survey template and send."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Send Survey"),
            "view_mode": "form",
            "res_model": "crm.lead.survey.send.wizard",
            "target": "new",
            "context": {"default_crm_lead_id": self.id},
        }

    def action_create_helpdesk_ticket_wizard(self):
        """Open wizard to select helpdesk team and create ticket."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Create Helpdesk Ticket"),
            "view_mode": "form",
            "res_model": "crm.lead.helpdesk.ticket.wizard",
            "target": "new",
            "context": {"default_crm_lead_id": self.id},
        }
