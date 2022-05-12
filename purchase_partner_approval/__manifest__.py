# Copyright 2022 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Purchase Partner Approval",
    "summary": "Control Partners that can be used in Purchase Orders",
    "version": "14.0.1.0.0",
    "website": "https://github.com/it-brasil/purchase-workflow",
    "category": "Purchase Management",
    "author": "IT Brasil",
    "license": "AGPL-3",
    "installable": True,
    "maintainers": ["dreispt"],
    "development_status": "Alpha",
    "depends": [
        "partner_stage",  # oca/product-attribute
        "purchase_exception",
    ],
    "data": [
        "data/exception_rule.xml",
        "data/init_puchase_ok.xml",
        "views/res_partner_stage.xml",
        "views/res_partner.xml",
    ],
}
