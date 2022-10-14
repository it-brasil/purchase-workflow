# Copyright 2017 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Purchase Order Triple Discount",
    "version": "14.0.1.1.0",
    "category": "Purchase Management",
    "author": "IT Brasil",
    "website": "https://github.com/it-brasil/purchase-workflow",
    "license": "AGPL-3",
    "summary": "Manage triple discount on purchase order lines",
    "depends": [
        "purchase_discount",
        "account_invoice_triple_discount",
    ],
    "data": [
        "views/purchase_order_report.xml",
        "views/product_supplierinfo_view.xml",
        "views/purchase_view.xml",
        "views/res_partner_view.xml",
    ],
    "installable": True,
}
