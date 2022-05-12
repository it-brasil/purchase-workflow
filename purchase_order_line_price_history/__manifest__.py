# Copyright 2020 Tecnativa - Ernesto Tejeda
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Purchase order line price history",
    "version": "14.0.1.0.0",
    "category": "Purchase Management",
    "author": "IT Brasil",
    "website": "https://github.com/it-brasil/purchase-workflow",
    "license": "AGPL-3",
    "depends": ["purchase"],
    "data": [
        "security/ir.model.access.csv",
        "wizards/purchase_order_line_price_history.xml",
        "views/purchase_views.xml",
    ],
    "installable": True,
}
