# -*- coding: utf-8 -*-
{
    'name': "Giầy Duy Hoàng",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nguyen Cong Giang",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/data_category_and_provider.xml',
        'data/data_product.xml',
        'data/data_users.xml',
        'data/data_group_product.xml',
        'data/data_group_product_detail.xml',
        'data/data_sale_order.xml',
        'data/data_sale_order_detail.xml',
        'data/sequance/generate_code_data.xml',
        'view/menu.xml',
        'view/res_partner.xml',
        'view/sale_order_view.xml',
        'view/sale_order_detail_view.xml',
        'view/product.xml',
        'view/group_product.xml',
        'view/group_product_detail.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}