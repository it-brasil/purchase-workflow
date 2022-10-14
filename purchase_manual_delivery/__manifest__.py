# Copyright 2022 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Purchase Manual Delivery",
    "summary": """
        Prevents pickings to be auto generated upon Purchase Order confirmation
        and adds the ability to manually generate them as the supplier confirms
        the different purchase order lines.
    """,
    "version": "14.0.1.0.1",
    "license": "AGPL-3",
    "author": "IT Brasil",
    "website": "https://github.com/it-brasil/purchase-workflow",
    "depends": ["purchase_stock"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/create_manual_stock_picking.xml",
        "views/purchase_order_views.xml",
        "views/res_config_view.xml",
    ],
}
