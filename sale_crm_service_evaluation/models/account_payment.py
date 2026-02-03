# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    sale_order_id = fields.Many2one(
        comodel_name="sale.order",
        string="Sale Order",
        ondelete="set null",
        index=True,
        help="Optional link to a sale order for this payment.",
    )
