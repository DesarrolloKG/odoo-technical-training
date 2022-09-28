# -*- coding:utf-8 -*-

from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_session_product = fields.Boolean(string="Use as session product", 
                                        help="Check this box tu use this as a product for session fee",
                                        default=False)
    

