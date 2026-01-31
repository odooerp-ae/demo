# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model_create_multi
    def create(self, vals_list):
        orders = super().create(vals_list)
        for order in orders:
            if not order.opportunity_id and order.partner_id:
                order._create_crm_lead_from_sale()
        return orders

    def _create_crm_lead_from_sale(self):
        """Create a CRM lead when a sale order is created and link it."""
        self.ensure_one()
        Lead = self.env["crm.lead"]
        lead = Lead.create({
            "name": f"{self.name} - {self.partner_id.name}",
            "partner_id": self.partner_id.id,
            "type": "opportunity",
            "user_id": self.user_id.id if self.user_id else self.env.user.id,
        })
        self.opportunity_id = lead.id
