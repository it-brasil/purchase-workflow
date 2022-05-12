# Copyright (C) 2021 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

{
    "name": "Purchase Advance Payment",
    "version": "14.0.1.0.1",
    "author": "IT Brasil",
    "website": "https://github.com/it-brasil/purchase-workflow",
    "category": "Purchase",
    "license": "AGPL-3",
    "summary": "Allow to add advance payments on purchase orders",
    "depends": ["purchase"],
    "data": [
        "wizard/purchase_advance_payment_wizard_view.xml",
        "views/purchase_view.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
}
