# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestSaleCrmServiceEvaluation(TransactionCase):
    def setUp(self):
        super().setUp()
        self.partner = self.env["res.partner"].create({
            "name": "Test Partner",
            "email": "test@example.com",
        })

    def test_sale_order_creates_crm_lead(self):
        """Test that creating a sale order creates a linked CRM lead."""
        order = self.env["sale.order"].create({
            "partner_id": self.partner.id,
        })
        self.assertTrue(order.opportunity_id)
        self.assertEqual(order.opportunity_id.partner_id, self.partner)

    def test_service_evaluation_satisfied_flow(self):
        """Test satisfied flow: button opens survey wizard."""
        lead = self.env["crm.lead"].create({
            "name": "Test Lead",
            "partner_id": self.partner.id,
            "type": "opportunity",
            "service_evaluation": "satisfied",
        })
        action = lead.action_send_survey_wizard()
        self.assertEqual(action["res_model"], "crm.lead.survey.send.wizard")
        self.assertEqual(action["context"]["default_crm_lead_id"], lead.id)

    def test_service_evaluation_inquiry_flow(self):
        """Test inquiry flow: can add inquiry lines."""
        lead = self.env["crm.lead"].create({
            "name": "Test Lead",
            "partner_id": self.partner.id,
            "type": "opportunity",
            "service_evaluation": "inquiry",
        })
        line = self.env["crm.inquiry.line"].create({
            "crm_lead_id": lead.id,
            "question": "Test question?",
            "resolution": "Test resolution",
            "status": "closed",
        })
        self.assertEqual(line.crm_lead_id, lead)

    def test_service_evaluation_unsatisfied_flow(self):
        """Test unsatisfied flow: button opens helpdesk wizard."""
        lead = self.env["crm.lead"].create({
            "name": "Test Lead",
            "partner_id": self.partner.id,
            "type": "opportunity",
            "service_evaluation": "unsatisfied",
        })
        action = lead.action_create_helpdesk_ticket_wizard()
        self.assertEqual(action["res_model"], "crm.lead.helpdesk.ticket.wizard")
