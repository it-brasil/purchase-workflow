# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Purchase Work Acceptance Evaluation",
    "version": "14.0.2.0.0",
    "category": "Purchase Management",
    "author": "IT Brasil",
    "license": "AGPL-3",
    "website": "https://github.com/it-brasil/purchase-workflow",
    "depends": ["purchase_work_acceptance"],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/res_config_settings_views.xml",
        "views/work_acceptance_evaluation_views.xml",
        "views/work_acceptance_views.xml",
        "report/work_acceptance_evaluation_report.xml",
    ],
    "demo": ["demo/evaluation_data.xml"],
    "maintainers": ["kittiu"],
    "installable": True,
    "development_status": "Alpha",
}
