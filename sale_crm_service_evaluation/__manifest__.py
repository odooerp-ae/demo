# Copyright 2025
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sale CRM Service Evaluation",
    "version": "17.0.1.0.0",
    "category": "CRM",
    "summary": "Service evaluation workflow: CRM from Sale Order with survey, inquiry, helpdesk integration",
    "author": "Odoo Community",
    "website": "https://github.com/OCA/",
    "license": "AGPL-3",
    "depends": [
        "sale_management",
        "sale_crm",
        "crm",
        "survey",
        "project",
        "helpdesk_mgmt",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/crm_lead_views.xml",
        "views/crm_inquiry_line_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_stage_views.xml",
        "views/survey_invite_views.xml",
        "wizard/survey_send_wizard_views.xml",
        "wizard/helpdesk_ticket_wizard_views.xml",
        "wizard/project_task_wizard_views.xml",
    ],
    "installable": True,
}
