# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sales_person_max_discount = fields.Integer(string='Sales Person Max Discount',
                                               compute='_compute_discount', readonly=False, store=True)
    sales_manager_max_discount = fields.Integer(string='Sales Manager Max Discount', compute='_compute_discount',
                                                readonly=False, store=True)

    @api.onchange('categ_id')
    def _compute_discount(self):
        for rec in self:
            rec.sales_person_max_discount = rec.categ_id.sales_person_max_discount
            rec.sales_manager_max_discount = rec.categ_id.sales_manager_max_discount


class ProductCategory(models.Model):
    _inherit = 'product.category'

    sales_person_max_discount = fields.Integer(string='Sales Person Max Discount')
    sales_manager_max_discount = fields.Integer(string='Sales Manager Max Discount')
