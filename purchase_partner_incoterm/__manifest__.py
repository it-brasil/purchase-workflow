# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Default purchase incoterm per partner",
    "summary": "Add a an incoterm field for supplier and use it on purchase order",
    "version": "14.0.1.0.0",
    "category": "Purchase",
    "author": "IT Brasil",
    "license": "AGPL-3",
    "depends": [
        "account",
        "purchase",
    ],
    "website": "https://github.com/it-brasil/purchase-workflow",
    "data": ["views/partner_view.xml"],
    "installable": True,
}
